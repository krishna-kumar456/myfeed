<template>
  <div>
    <p>{{ title }}</p>
    <ul>
      <li v-for="todo in todos" :key="todo.id" @click="increment">
        {{ todo.id }} - {{ todo.content }}
      </li>
    </ul>
    <p>Count: {{ todoCount }} / {{ meta.totalCount }}</p>
    <p>Active: {{ active ? "yes" : "no" }}</p>
    <p>Clicks on todos: {{ clickCount }}</p>
    <p>Response Message : {{ state.info }}</p>
  </div>
</template>

<script lang="ts">
import {
  reactive,
  defineComponent,
  PropType,
  computed,
  ref,
  toRef,
  Ref
} from "@vue/composition-api";
import axios from "axios";
import { Todo, Meta } from "./models";

function useClickCount() {
  const clickCount = ref(0);
  function increment() {
    clickCount.value += 1;
    return clickCount.value;
  }

  return { clickCount, increment };
}

function useDisplayTodo(todos: Ref<Todo[]>) {
  const todoCount = computed(() => todos.value.length);
  return { todoCount };
}

function loadData() {
  const state = reactive({
    info: null,
    loading: true,
    errored: false
  });
  axios
    .get("http://localhost:8081/")
    .then(response => {
      state.info = response.data.message;
      console.log(state.info)
    })
    .catch(() => {
      console.error("Something went wrong")
    })

  return { state };
}
export default defineComponent({
  name: "CompositionComponent",
  props: {
    title: {
      type: String,
      required: true
    },
    todos: {
      type: (Array as unknown) as PropType<Todo[]>,
      default: () => []
    },
    meta: {
      type: (Object as unknown) as PropType<Meta>,
      required: true
    },
    active: {
      type: Boolean
    }
  },
  setup(props) {
    return { ...useClickCount(), ...useDisplayTodo(toRef(props, "todos")), ...loadData() };
  }
});
</script>
