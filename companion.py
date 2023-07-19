import streamlit as st

realms_data = {
    'Sunfire Plains': {
        'Bronze': 'Redwood Basin',
        'Silver': 'Beryl Boglands',
        'Gold': 'Quartz Castle'
    },
    'Aquaflow Basin': {
        'Bronze': 'Jasper Lakes',
        'Silver': 'Aquamarine Waters',
        'Gold': 'Diamond Falls'
    },
    'Earthshaper Peaks': {
        'Bronze': 'Ashen Steppes',
        'Silver': 'Malachite Marshes',
        'Gold': 'Peridot Palace'
    },
    'Galeshield Coast': {
        'Bronze': 'Obsidian Coast',
        'Silver': 'Aquamarine Waters',
        'Gold': 'Alexandrite Archipelago'
    },
    'Lifegrove Woods': {
        'Bronze': 'Ironwood Woods',
        'Silver': 'Jade Jungles',
        'Gold': 'Ruby Ruins'
    },
    'Frostwatch Tundra': {
        'Bronze': 'Basalt Caves',
        'Silver': 'Tourmaline Tundras',
        'Gold': 'Sapphire Sanctum'
    },
    'Starsight Arctic': {
        'Bronze': 'Sandstone Gulch',
        'Silver': 'Azurite Arctic',
        'Gold': 'Aquamarine Abyss'
    },
    'Ethersong Meadows': {
        'Bronze': 'Juniper Meadows',
        'Silver': 'Moonstone Meadows',
        'Gold': 'Moonstone Monastery'
    },
    'Spiritstream Waters': {
        'Bronze': 'Quartzite Peaks',
        'Silver': 'Rhodonite Rivers',
        'Gold': 'Opal Oracle'
    },
    'Harmony Springs': {
        'Bronze': 'Siltstone Valley',
        'Silver': 'Sardonyx Springs',
        'Gold': 'Tanzanite Temple'
    }
}

# Load images
def load_images(category, territories):
    images = {}
    for territory in territories:
        images[territory] = f'images/{category}/{territory.replace(" ", "_")}.png'
    return images

# Define Territories
bronze = ['Redwood Basin', 'Ashen Steppes', 'Juniper Meadows', 'Obsidian Coast', 'Flint Quarries', 'Ironwood Woods', 'Jasper Lakes', 'Agate Cliffs', 'Siltstone Valley', 'Claystone Hills', 'Quartzite Peaks', 'Sandstone Gulch', 'Basalt Caves', 'Pumice Plains', 'Shale Slopes']
silver = ['Beryl Boglands', 'Malachite Marshes', 'Aquamarine Waters', 'Moonstone Meadows', 'Onyx Overlook', 'Zircon Zephyrlands', 'Tourmaline Tundras', 'Jade Jungles', 'Chrysocolla Cliffs', 'Lapis Lazuli Lakes', 'Azurite Arctic', 'Rhodonite Rivers', 'Spinel Savannahs', 'Tanzanite Taigas', 'Sardonyx Springs']
gold = ['Quartz Castle', 'Diamond Falls', 'Peridot Palace', 'Alexandrite Archipelago', 'Ruby Ruins', 'Sapphire Sanctum', 'Aquamarine Abyss', 'Moonstone Monastery', 'Opal Oracle', 'Jade Jungle', 'Rhodonite Ridge', 'Spinel Springs', 'Tanzanite Temple', 'Sardonyx Sanctuary', 'Lapis Lazuli Land']

# Load images
bronze_images = load_images('bronze', bronze)
silver_images = load_images('silver', silver)
gold_images = load_images('gold', gold)

# The main app
def main():
    st.title("Elemental Clash - Territory Tracker")

    # Define columns
    col1, col2, col3 = st.columns(3)

    with col1:
        st.header("Bronze Territories")
        bronze_selection = st.multiselect("Select won territories", options=bronze)
        for territory in bronze_selection:
            st.image(bronze_images[territory], width=70)

    with col2:
        st.header("Silver Territories")
        silver_selection = st.multiselect("Select won territories", options=silver)
        for territory in silver_selection:
            st.image(silver_images[territory], width=70)

    with col3:
        st.header("Gold Territories")
        gold_selection = st.multiselect("Select won territories", options=gold)
        for territory in gold_selection:
            st.image(gold_images[territory], width=70)

    if st.button('Check'):
        # Once selections are made, check if they form a Realm
        check_for_realm(bronze_selection, silver_selection, gold_selection)

# Check if selected territories form a Realm
def check_for_realm(bronze_selection, silver_selection, gold_selection):
    for realm, territories in realms_data.items():
        if territories['Bronze'] in bronze_selection and territories['Silver'] in silver_selection and territories['Gold'] in gold_selection:
            st.success(f"You have won the {realm} realm!")
if __name__ == "__main__":
    main()
