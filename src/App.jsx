// App.js

import React, { useState } from "react";
import CardSelection from "./components/CardSelection";
import RealmCheck from "./components/RealmCheck";

const App = () => {
  const [selectedCards, setSelectedCards] = useState({
    bronze: [],
    silver: [],
    gold: [],
  });

  const realmsData = {
    // fill this with your realms data
  };

  const handleCardSelection = (cards, category) => {
    setSelectedCards({
      ...selectedCards,
      [category]: cards,
    });
  };

  const bronzeTerritories = [
    "Redwood_Basin", "Ashen_Steppes", "Juniper_Meadows",
    "Obsidian_Coast", "Flint_Quarries", "Ironwood_Woods",
    "Jasper_Lakes", "Agate_Cliffs", "Siltstone_Valley",
    "Claystone_Hills", "Quartzite_Peaks", "Sandstone_Gulch",
    "Basalt_Caves", "Pumice_Plains", "Shale_Slopes",
  ];

  const silverTerritories = [
    "Beryl_Boglands", "Malachite_Marshes", "Aquamarine_Waters",
    "Moonstone_Meadows", "Onyx_Overlook", "Zircon_Zephyrlands",
    "Tourmaline_Tundras", "Jade_Jungles", "Chrysocolla_Cliffs",
    "Lapis_Lazuli_Lakes", "Azurite_Arctic", "Rhodonite_Rivers",
    "Spinel_Savannahs", "Tanzanite_Taigas", "Sardonyx_Springs",
  ];

  const goldTerritories = [
    "Quartz_Castle", "Diamond_Falls", "Peridot_Palace",
    "Alexandrite_Archipelago", "Ruby_Ruins", "Sapphire_Sanctum",
    "Aquamarine_Abyss", "Moonstone_Monastery", "Opal_Oracle",
    "Jade_Jungle", "Rhodonite_Ridge", "Spinel_Springs",
    "Tanzanite_Temple", "Sardonyx_Sanctuary", "Lapis_Lazuli_Land",
  ];

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-4">Realms Game Companion App</h1>
      <CardSelection
        territories={bronzeTerritories}
        category="bronze"
        onSelection={handleCardSelection}
      />
      <CardSelection
        territories={silverTerritories}
        category="silver"
        onSelection={handleCardSelection}
      />
      <CardSelection
        territories={goldTerritories}
        category="gold"
        onSelection={handleCardSelection}
      />
      <RealmCheck
        realmsData={realmsData}
        selectedCards={selectedCards}
      />
    </div>
  );
}

export default App;
