<template>
  <div id="app">
    <form @submit="submitHandler">
      选择文件：<input type="file" name="file" :multiple="false" @change="onFileChange" />
      <button type="submit">提交</button>
    </form>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "App",
  data() {
    return {
      file: null,
    };
  },
  methods: {
    onFileChange(e) {
      var files = e.target.files || e.dataTransfer.files;
      if (!files.length) return;
      this.file = files[0]
    },
    submitHandler(e) {
      e.preventDefault();
      // form action="/upload" method="post" enctype="multipart/form-data"
      let bodyFormData = new FormData();
      bodyFormData.append("file", this.file);
      axios.post("/api/upload", bodyFormData, {
        headers: { "Content-Type": "multipart/form-data" }
      }).then(response => {
        console.log(response);
        if(response.data.code === 0) {
          alert("Success, server detected file size: "+response.data.size)
        } else {
          alert("Request failed: "+response.data.msg)
        }
      }).catch(err => {
        console.log(err)
      })
    },
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}
</style>
