<template>
  <div>
    <Header />
    <div id="main">
      <div id="leftSide">
        <h1>A propos de moi</h1>
        <h2>Présentation</h2>
        <p>
          Bonjour, Je suis Arthur-Conrad DUPRIEZ, un jeune ingénieur calcul et
          développeur basé à Marseille. Je me suis trouvé une réelle passion
          pour le développement informatique. C'est pourquoi j'adore me
          challenger avec de nouveaux projets en tout genre. J'ai conçu ce site
          pour permettre à ceux qui le visite d'en savoir plus sur moi, mon
          parcours et mes projets.
        </p>
        <h2>Compétences Techniques</h2>
        <div id="sticker-container">
          <Sticker imagePath="/vue.svg" titre="Vuejs 3" />
          <Sticker imagePath="/python.svg" titre="Python" />
          <Sticker imagePath="/HTML.png" titre="HTML 5" />
          <Sticker imagePath="/css.png" titre="Css 3" />
          <Sticker
            imagePath="/javascript.png"
            titre="Javascript 5"
          />
          <Sticker imagePath="/pinia.png" titre="Pinia" />
          <Sticker imagePath="/docker.png" titre="Docker" />
          <Sticker imagePath="/vba.svg" titre="VBA" />
          <Sticker imagePath="/word.svg" titre="Word" />
          <Sticker imagePath="/excel.png" titre="Excel" />
          <Sticker
            imagePath="/powerpoint.png"
            titre="Power point"
          />
          <Sticker imagePath="/git.png" titre="Git" />
          <Sticker imagePath="/sql.png" titre="PostgreSQL" />
          <Sticker imagePath="/minio.png" titre="MinIO" />
          
          <!-- <Sticker imagePath="../src/assets/excel.png" titre="Excel" /> -->
        </div>
        <h2>Projets</h2>
        <p>
          L'ensemble de mes projets sont réunis
          <RouterLink class="link" to="/app">Ici</RouterLink>
        </p>
      </div>  
        
      <div id="rightSide">
        <div ref="chartContainer"></div>
      </div>

      <div id="botSide">
        <h2>Compétences et Qualités personnelles</h2>
        <div id="qualite">
            <div id="arthur">
                <Carte front="A" back="Ambitieux"</Carte>
                <Carte front="R" back="Rigoureux"</Carte>
                <Carte front="T" back="Tenace"</Carte>
                <Carte front="H" back="Habile"</Carte>
                <Carte front="U" back="Unique"</Carte>   
                <Carte front="R" back="Résiliant"</Carte>                            
            </div>
                
            <div id="conrad">
                <Carte front="C" back="Créatif"</Carte>
                <Carte front="O" back="Observateur"</Carte>
                <Carte front="N" back="Novateur"</Carte>
                <Carte front="R" back="Rationnel"</Carte>
                <Carte front="A" back="Adaptable"</Carte>   
                <Carte front="D" back="Déterminé"</Carte> 
            </div>
        </div>
      </div>
      <Footer />

    </div>
  
  </div>
</template>

<script setup>
import Header from "../components/Header.vue";
import Sticker from "../components/commonTools/Sticker.vue";
import Carte from "../components/commonTools/CarteReverse.vue";
import Footer from "@/components/Footer.vue";

import { onMounted, ref } from "vue";
import Highcharts from "highcharts";
import HighchartsMore from "highcharts/highcharts-more"; // Import du module highcharts-more
import HighchartsTimeline from "highcharts/modules/timeline"; // Import du module timeline

// Initialisation des modules
HighchartsMore(Highcharts);
HighchartsTimeline(Highcharts);

// Définir les options du graphique
const chartOptions = {
  chart: {
    type: "timeline",
    inverted: true,
    height: "700px",
  },

  xAxis: {
    type: "datetime",
    visible: false,
  },

  yAxis: {
    gridLineWidth: 1,
    title: null,
    labels: {
      enabled: false,
    },
  },

  legend: {
    enabled: false,
  },

  title: {
    text: "Parcours et Expériences",
  },

  tooltip: {
    style: {
      width: 300,
    },
  },

  series: [
    {
      dataLabels: {
        allowOverlap: false,
        format:
          '<span style="color:{point.color}">● </span><span style="font-weight: bold;" > ' +
          "{point.x:%d %b %Y}</span><br/>{point.label}",
      },
      marker: {
        symbol: "circle",
      },
      useHTML: true,
      data: [
        // {
        //   x: Date.UTC(2014, 8, 9),
        //   name: "CPGE",
        //   label:
        //     "<b>Classe Préparatoire aux Grandes Ecoles</b> </br> Lycée du Hainaut, Valenciennes </br>France",
        //   description:
        //     "3 années durant lesquels j'ai pu construire mon bagage scientifique, </br> mais aussi découvrir l'univers du développement informatique avec en autre le language Python",
        //   color: "#FE9801",
        // },
        // {
        //   x: Date.UTC(2017, 8, 7),
        //   name: "ISMANS",
        //   label:
        //     "<b>Institut Supérieur des Matériaux du Mans</b> </br> Le Mans, France",
        //   description:
        //     "Période de 3 ans où j'ai approfondi mes connaissances dans le domaine de la mécanique et notament dans le calcul de structure",
        //   color: "#FE9801",
        //   onArea: false,
        // },
        {
          x: Date.UTC(2020, 8, 28),
          name: "SOM",
          label:
            "<b>Ingénieur Calcul</b> </br> SOM Calcul, Marseille </br> France",
          description:
            "Après un stage de fin d'études réussi, SOM Calcul Marseille me propose mon premier emploi. </br> C'est là-bas que je découvre le monde du travail",
          color: "#2096F2",
        },
        {
          x: Date.UTC(2021, 0, 11),
          name: "GRET",
          label:
            "<b>Ingénieur Calcul</b> </br> SOM Calcul (GRET), Marseille </br> France",
          description:
            "Au bout de quelques mois, on me propose de rejoindre le groupement d'étude GRET. </br> Cet entité a pour rôle de repondre au besoins exclusifs d'EDF",
          color: "#2096F2",
        },
        {
          x: Date.UTC(2023, 0, 2),
          name: "Cellules Méthodes",
          label:
            "<b>Ingénieur Calcul et développeur</b></br> SOM Calcul , Marseille </br> France",
          description:
            "Après deux ans au sein du GRET, je saisi l'opportunité de rejoindre la cellule methodes de l'entreprise. </br> C'est ici que ma cariere de développeur commence. On me forme aux outils du Web et je commence de vrais projets.",
          color: "#2096F2",
        },
        {
          x: Date.UTC(2023, 2, 10),
          name: "Formation WEB",
          label: "<b>Formation FrontEnd / BackEnd</b></br>Marseille, France",
          description:
            "Formation dans laquelle j'ai appris le développement FrontEnd avec le framework Vuejs 3 et le BackEnd avec Python. </br> La formation n'a durée que deux semaines mais cela m'a permis de voir les grands aspects. Il ne me restait plus qu'à expérimenté par mes propres moyens !!",
          color: "#008000",
        },
        {
          x: Date.UTC(2023, 6, 8),
          name: "Formation Gestion serveur",
          label: "<b>Formation Gestion des serveurs</b></br>Marseille, France",
          description:
            "Durant cette formation j'ai à appris à naviguer et utiliser un environnement linux. </br> J'ai aussi découvert comment héberger un site Web sur un serveur avec Docker",
          color: "#008000",
        },
      ],
    },
  ],
};

const chartContainer = ref(null);

onMounted(() => {
  if (chartContainer.value) {
    Highcharts.chart(chartContainer.value, chartOptions);
  }
});
</script>

<style scoped>
#main {
  width: 100%;
  /* background: linear-gradient(45deg ,var(--emerald-green-100), var(--blue-700)); */
  background: radial-gradient(circle, 
                                var(--blue-100), 
                                var(--blue-300), 
                                var(--blue-400), 
                                var(--blue-300), 
                                var(--blue-100));
  padding: 50px;
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
}
#leftSide {
  width: 50%;
  /* border: 1px solid brown; */
  border-radius: 15px;
  padding: 15px;
  margin: 15px;
  min-width: 400px;
  flex-grow: 1;
}

#sticker-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
}

#rightSide {
  width: 45%;
  position: relative;
  background-color: white;
  height: 800px;
  border: 1px solid brown;
  border-radius: 15px;
  padding: 15px;
  margin: 15px;
  min-width: 300px;
  flex-grow: 1;
}

#botSide{
    width: 95%;
    min-width: 650px;
    padding: 5px;
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
}

#qualite{
    width: 100%;
    /* background-color: var(--brown-100); */
    border-radius: 25px;
    padding: 5px;
    display: flex;
    /* flex-wrap: wrap; */
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

#arthur, #conrad{
    display: inline-flex;
    justify-content: space-around;
    flex-grow: 1;
    min-width: 600px;
    width: 45%;
    padding: 5px 0px;

}

h1 {
  color: var(--brown-300);
}

h2 {
  color: var(--brown-500);
  margin: 25px 0;
}

h3 {
  color: var(--brown-500);
  margin: 25px 50px;
}

p {
  color: var(--brown-900);
  margin: 5px 0;
  text-align: justify;
}
</style>
