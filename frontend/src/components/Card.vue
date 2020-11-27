<template>
  <div class="card full-width row no-wrap justify-center items-center content-center q-pa-sm">
     <q-card class="my-card col-md-5" flat bordered>
      <q-card-section horizontal>
        <q-card-section class="q-pt-xs">
          <div class="text-h5 q-mt-sm q-mb-xs">{{ info.title }}</div>
          <div class="text-grey q-pt-xs">
            {{ info.summary }}
          </div>
        </q-card-section>

        <q-card-section class="col-5 flex flex-center">
          <q-img
            class="rounded-borders"
            v-bind:src= "info.image"
          />
        </q-card-section>
      </q-card-section>

      <q-separator />

      <q-card-actions>
        <q-btn flat color="primary" type="a" v-bind:href="info.url" target="_blank">
          Read Content
        </q-btn>
        <q-btn flat color="primary" type="a" v-bind:href="info.commentsurl" target="_blank" label="HN Comments">
          
          <q-badge color="red" floating>{{ info.descendants }} </q-badge>
        </q-btn>
      </q-card-actions>
    </q-card>
  </div>
</template>
<script lang="ts">
  import { computed, PropType } from '@vue/composition-api';
  import { Card } from "./models";
  export default {
    name: "Card",
    props: {
        info: {
            type: (Object as unknown) as PropType<Card>,
            required: true
        }
    }
  };
</script>
<style scoped>
p {
  color:#EDF2F4;
}
</style>