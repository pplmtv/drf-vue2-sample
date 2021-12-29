<template>
  <div id="home-page">
    <GlobalHeader />
    <GlobalMessage />

    <!-- メインエリア -->
    <main class="container mt-5 p-5">
      <p class="h5 mb-5">ホーム</p>
      <b-form v-on:submit.prevent="submitSave">
        <div class="row form-group">
          <label class="col-sm-3 col-form-label">タイトル</label>
          <div class="col-sm-8">
            <b-input
              type="text"
              class="form-control"
              v-model="form.book.title"
              />
          </div>
        </div>
        <div class="row form-group">
          <label class="col-sm-3 col-form-label">価格</label>
          <div class="col-sm-8">
            <b-input
              type="text"
              class="form-control"
              v-model="form.book.price"
              />
          </div>
        </div>
        <div class="row text-center mt-5">
          <div class="col-sm-12">
            <b-button type="submit" variant="primary">
              {{ isCreated ? "更新" : "登録" }}
            </b-button>
          </div>
        </div>
      </b-form>
    </main>

    <!-- デバッグ -->
    <div class="m-5">
      <pre>form: {{ form }}</pre>
      <pre>state: {{ this.$store.state }}</pre>
    </div>
  </div>
</template>

<script>
import api from "@/services/api";
import GlobalHeader from "@/components/GlobalHeader.vue";
import GlobalMessage from "@/components/GlobalMessage.vue";
import axios from "axios";

export default {
  components: {
    GlobalHeader,
    GlobalMessage
  },
  data() {
    return {
      // 入力フォームの内容
      form: {
        book: {
          title: "",
          price: 0
        }
      }
    };
  },
  computed: {
    isCreated: function () {
      return this.form.book.id !== undefined;
    }
  },
  methods: {
    // 登録・更新ボタン押下
    submitSave: function() {
      // 本の登録・更新を実行
      console.log("create or update.");
      // console.log("token",localStorage.getItem("access"));
      ////////// DEBUG START //////////
      console.log("DEBUG START.");
      axios.get("http://127.0.0.1:8000/api/v1/books/")
    .then(response=>{
      console.log("DEBUG axios get success.");
      console.log("status:",response.status)
      // console.log("data:",response.data)
    })
    .catch(err=>{
      console.log("axiosGetErr",err)
    })

      axios.post("http://127.0.0.1:8000/api/v1/books/",{"title":"urasima tarou","price":2000,"created_at":"2021-12-07T06:41:56.325618+09:00"})
    .then(response=>{
      console.log("DEBUG axios post success.")
      console.log("status:",response.status)
      // console.log("data:",response.data);
    })
    .catch(err=>{
      console.log("axiosGetErr",err)
    })
    .finally(()=>{
      console.log("DEBUG END.");
    });
      ////////// DEBUG END //////////

      api({
        // 登録済みかどうかでHTTPメソッドとエンドポイントを切り替える
        method: this.isCreated ? "put" : "post",
        url: this.isCreated ? "/books/" + this.form.book.id + "/" : "/books/",
        data: {
          id: this.form.book.id,
          title: this.form.book.title,
          price: this.form.book.price
        }
      }).then(response => {
        // console.log("id",this.form.book.id);
        // console.log("title",this.form.book.title);
        // console.log("price",this.form.book.price);
        const message = this.isCreated ? "更新しました。" : "登録しました。";
        this.$store.dispatch("message/setInfoMessage", { message: message });
        this.form.book = response.data;
      });
    }
  }
};
</script>
