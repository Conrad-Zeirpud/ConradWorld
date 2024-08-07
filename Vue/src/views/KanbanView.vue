<script setup>
import { onBeforeMount } from "vue";
import { useKanbanStore } from "@/stores/kanbanStore";
import { storeToRefs } from "pinia";
import Header from "../components/Header.vue";

// Utilisation du store Kanban
const useKanban = useKanbanStore();
const { columns } = storeToRefs(useKanban);

// Récupération des colonnes avant que le composant soit monté
onBeforeMount(() => {
  useKanban.fetchColumns();
});
</script>

<template>
  <Header />
  <h1>Liste des colonnes</h1>
  <ul>
    <li v-for="(column, index) in columns" :key="index">{{ column }}</li>
  </ul>
</template>

<style scoped></style>
