import { defineStore } from "pinia";
import axios from "axios";
import { ref } from "vue";

export const useKanbanStore = defineStore("kanban", () => {
  const columns = ref([]);

  async function fetchColumns() {
    try {
      const response = await axios.get("http://127.0.0.1:8000/api/columns/");
      columns.value = response.data.map((column) => column.name);
    } catch (error) {
      console.error("Error fetching columns:", error);
    }
    console.log(columns.value);
  }

  return { columns, fetchColumns };
});
