<template>
  <div class="about">
    <h1>{{ message }}</h1>
  </div>
</template>
<script lang="ts" setup>
import axios from "axios";
import { ref } from "vue";

const message = ref("");

axios
  .get("http://127.0.0.1:8080/", { withCredentials: true })
  .then((response: any) => {
    const res = response.data;
    message.value = res["message"];
  })
  .catch((e) => {
    console.log(e);
  });
</script>

<style>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>
