<template>
  <q-page class="row items-center justify-evenly">
    <api-component></api-component>
  </q-page>
</template>

<script lang="ts">
  import ApiComponent from 'components/ApiComponent.vue';
  export default {
    name: 'ApiIndex',
    components: { ApiComponent },
    setup() {
        let state = "";
      return {
        state
      };
    }
  }
</script>