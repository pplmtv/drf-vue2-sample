<template>
  <!-- ヘッダーナビゲーション -->
  <div id="header">
    <b-navbar type="dark" variant="dark">
      <a class="navbar-brand" href="/">DRF Sample</a>
      <b-navbar-nav class="ml-auto" v-if="$route.meta.requiresAuth">
        <b-nav-item-dropdown right v-if="isLoggedIn">
          <template v-slot:button-content>{{ username }}</template>
          <b-dropdown-item href="#" v-on:click="clickLogout">
            ログアウト
          </b-dropdown-item>
        </b-nav-item-dropdown>
        <b-nav-item href="# v-on:click=clickLogin" v-else>
          ログイン
        </b-nav-item>
      </b-navbar-nav>
    </b-navbar>
  </div>
</template>

<script>
export default {
  computed: {
    username: function() {
      return this.$store.state.auth.username;
    },
    isLoggedIn: function() {
      return this.$store.state.auth.isLoggedIn;
    }
  },
  methods: {
    // ログアウトリンク押下
    clickLogout: function() {
      this.$store.dispatch("auth/logout");
      this.$store.dispatch("message/setInfoMessage", {
        message: "ログアウトしました。"
      });
      this.$router.replace("/login");
    },
    // ログインリンク押下
    clickLogin: function () {
      this.$store.dispatch("message/clearMessages");
      this.$router.replace("/login");
    }
  }
};
</script>
