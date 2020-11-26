<template>
  <div>
    <!-- <p>Response Message : {{ state.info }}</p> -->
    <!-- <li v-for="info in state.info" :key="info.id">
        {{ info.id }} - {{ info.by }}
    </li> -->
    <card v-for="info in state.info" :info="info" :key="info.id" />
    
  </div>
</template>

<script lang="ts">
import {
  reactive,
  defineComponent,
} from "@vue/composition-api";
import axios from "axios";
import Card from "./Card.vue";

function loadData() {
  const state = reactive({
    info: null,
    loading: true,
    errored: false
  });
  axios
    .get("http://localhost:8081/best-hn")
    .then(response => {
      state.info = response.data.response
      console.log(state.info)
    })
    .catch(() => {
      console.error("Something went wrong")
    })

  return { state };
}
export default defineComponent({
  components: { Card },
  name: "ApiComponent",
  props: {

  },
  setup(props) {
    return { ...loadData() };
  }
});
</script>
