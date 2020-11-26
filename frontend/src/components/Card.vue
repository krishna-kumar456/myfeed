<template>
  <div class="card">
     <q-card class="my-card" flat bordered>
      <q-card-section horizontal>
        <q-card-section class="q-pt-xs">
          <div class="text-overline">{{ info.id }}</div>
          <div class="text-h5 q-mt-sm q-mb-xs">{{ info.title }}</div>
          <div class="text-caption text-grey">
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

      <!-- <q-card-actions>
        <q-btn flat round icon="event" />
        <q-btn flat>
          7:30PM
        </q-btn>
        <q-btn flat color="primary">
          Reserve
        </q-btn>
      </q-card-actions> -->
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