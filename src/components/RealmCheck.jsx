// RealmCheck.js

import React from "react";

const RealmCheck = ({ realmsData, selectedCards }) => {
    const checkForRealm = () => {
        // ... check if any realm has been won and return realm
    }

    const realmWon = checkForRealm();

    return (
        <div className="p-4">
            <h2 className="font-bold mb-4">Check Realms</h2>
            {realmWon && <p>You've won {realmWon}!</p>}
            <button
                className="px-4 py-2 bg-blue-500 text-white rounded"
                onClick={checkForRealm}
            >
                Check
            </button>
        </div>
    );
}

export default RealmCheck;
