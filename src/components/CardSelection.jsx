// CardSelection.js

import React, { useState } from "react";

const CardSelection = ({ territories, category, onSelection }) => {
    const [selectedCards, setSelectedCards] = useState([]);

    const handleCardSelection = (card) => {
        if (selectedCards.includes(card)) {
            setSelectedCards(selectedCards.filter(c => c !== card));
        } else {
            setSelectedCards([...selectedCards, card]);
        }
        onSelection([...selectedCards, card], category);
    }

    return (
        <div className="p-4">
            <h2 className="font-bold mb-4">{category}</h2>
            <div className="grid grid-cols-3 gap-4">
                {territories.map((territory, index) => (
                    <img
                        key={index}
                        src={`images/${category}/${territory}.png`}
                        className={`${selectedCards.includes(territory) ? 'ring-2 ring-blue-500' : ''} cursor-pointer`}
                        alt={territory}
                        onClick={() => handleCardSelection(territory)}
                    />
                ))}
            </div>
        </div>
    );
}

export default CardSelection;
