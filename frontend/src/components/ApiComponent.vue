<template>
  <div>
    <p>Response Message : {{ state.info }}</p>
  </div>
</template>

<script lang="ts">
import {
  reactive,
  defineComponent,
} from "@vue/composition-api";
import axios from "axios";

function loadData() {
  const state = reactive({
    info: null,
    loading: true,
    errored: false
  });
  axios
    .get("http://localhost:8081/keywords")
    .then(response => {
      state.info = response.data.keywords;
      console.log(state.info)
    })
    .catch(() => {
      console.error("Something went wrong")
    })

  return { state };
}
export default defineComponent({
  name: "ApiComponent",
  props: {
   
  },
  setup(props) {
    return { ...loadData() };
  }
});
</script>
