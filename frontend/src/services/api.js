import axios from "axios";
import store from "@/store";

const api = axios.create({
    baseURL: process.env.VUE_APP_ROOT_API,
    // baseURL: "http://127.0.0.1:8000/api/v1/",
    timeout: 5000,
    headers: {
        "Content-Type": "application/json",
        "X-Requested-With": "XMLHttpRequest"
    }
});

// 共通処理
api.interceptors.request.use(
    config => {
        // メッセージをクリア
        console.log("message clear.");
        console.log("process.env.VUE_APP_ROOT_API",process.env.VUE_APP_ROOT_API);
        store.dispatch("message/clearMessages");
        // 認証用トークンがあればリクエストヘッダに加える
        const token = localStorage.getItem("access");
        // console.log("token",localStorage.getItem("access"));
        if (token) {
            config.headers.Authorization = "JWT " + token;
            return config;
        }
        return config;
    },
    error => {
        return Promise.reject(error);
    }
);

// 共通エラー処理
api.interceptors.response.use(
    response => {
        console.log("DEBUG api.interceptors.response.use");
        console.log("status:",response.status);
        // console.log("data:",response.data);
        return response;
    },
    error => {
        console.log("error.response=", error.response);
        const status = error.response ? error.response.status : 500;

        // エラーの内容に応じてstoreのメッセージを更新
        let message;
        if (status === 400) {
            // バリデーションNG
            const messages = [].concat.apply([], Object.values(error.response.data));
            store.dispatch("message/setWarningMessages", { messages: messages });
        } else if (status === 401) {
            // 認証エラー
            const token = localStorage.getItem("access");
            if (token != null) {
                message = "ログイン有効期限切れ"
            } else {
                message = "認証エラー";
            }
            store.dispatch("auth/logout");
            store.dispatch("message/setErrorMessage", {message: message});
        } else if (status === 403) {
            // 権限エラー
            message = "権限エラーです。";
            store.dispatch("message/setErrorMessage", { message: message });
        } else {
            // その他のエラー
            message = "想定外のエラーです";
            store.dispatch("message/setErrorMessage", { message: message });
        }
        return Promise.reject(error);
    }
);

export default api;
