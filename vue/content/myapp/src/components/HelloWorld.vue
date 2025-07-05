<template>
  <v-container>
    <v-card>
      <v-card-title>名前の入力</v-card-title>
      <v-card-text>
        <v-text-field v-model="name" label="名前を入れて「送信する」を押してください">
        </v-text-field>
      </v-card-text>
      <v-divider></v-divider>
      <v-card-actions>
        <v-btn text color="primary" v-on:click="submitForm">
          送信する
        </v-btn>
      </v-card-actions>
    </v-card>

    <v-card class="mt-5">
      <v-card-title>あなたのアバター</v-card-title>
      <v-card-text>
        <div v-if="avatarResult.avatar_url" class="mb-4 text-center">
          <img :src="avatarResult.avatar_url" alt="Personal Avatar" width="100" height="100">
        </div>
        <h4>{{ message }}</h4>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script type="module">
import axios from 'axios';

export default {
  name: 'HelloWorld',
  data: () => ({
    name: 'test',
    message: 'ここにアバターが表示されます',
    avatarResult: { // アバターURLを保持するオブジェクト
      name: '',
      avatar_url: null,
    },
  }),
  methods: {
    submitForm: async function () {
      // 既存の挨拶APIを呼び出し
      const greetingRes = await axios.post('http://localhost:8080/api/greetings', { 'name': this.name });
      this.message = greetingRes.data.message;

      // アバターAPIを呼び出し
      if (this.name) {
        await this.fetchAvatar(this.name);
      } else {
        this.avatarResult = { name: '', avatar_url: null };
      }
    },
    // アバターURLを取得するメソッド
    fetchAvatar: async function (name) {
      this.avatarResult = { name: name, avatar_url: null }; // 結果をリセット
      if (!name) return;

      try {
        const res = await axios.get(`http://localhost:8080/api/avatar/${name}`);
        this.avatarResult = res.data;
      } catch (error) {
        console.error("アバターAPI呼び出しエラー:", error);
        this.avatarResult.avatar_url = null;
      }
    }
  }
};
</script>