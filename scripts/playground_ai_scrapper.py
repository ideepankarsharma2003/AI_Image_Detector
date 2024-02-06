# topics for image generation 
topics_for_image_generation = [
    "Fantasy landscapes",
    "Futuristic cityscapes",
    "Underwater scenes",
    "Space exploration",
    "Post-apocalyptic worlds",
    "Steampunk aesthetics",
    "Magical creatures",
    "Historical battles",
    "Cybernetic organisms",
    "Ancient civilizations",
    "Robotic companions",
    "Time travel adventures",
    "Alien encounters",
    "Mythical beasts",
    "Virtual reality simulations",
    "Dystopian societies",
    "Alternate dimensions",
    "Superhero showdowns",
    "Medieval kingdoms",
    "Technological advancements",
    "Exploration of uncharted territories",
    "Interstellar voyages",
    "Industrial revolution settings",
    "Mythological gods and goddesses",
    "Apocalyptic catastrophes",
    "Extraterrestrial colonization",
    "Artificial intelligence uprising",
    "Survival in extreme environments",
    "Genetic manipulation experiments",
    "Mystical artifacts",
    "Space piracy adventures",
    "Surreal dreamscapes",
    "Conspiracy theories",
    "Parallel universes",
    "Time loop phenomena",
    "Invasion of Earth by alien forces",
    "Magical academies",
    "Pandemic aftermath scenarios",
    "Cloning experiments gone wrong",
    "Exploration of the multiverse",
    "Post-human evolution",
    "Techno-magic fusion worlds",
    "Cyber espionage missions",
    "Eco-friendly utopias",
    "Colonization of Mars",
    "Apocalyptic weather phenomena",
    "Mecha battles",
    "Ancient prophecies coming true",
    "Mutant creatures",
    "Spiritual journeys",
    "Transhumanist societies",
    "Nanotechnology revolutions",
    "Demonic invasions",
    "Cosmic horror encounters",
    "Cryptid sightings",
    "Bioengineering marvels",
    "Psychic abilities",
    "Exoplanet exploration",
    "UFO sightings",
    "Robot uprisings",
    "Magical heists",
    "Astronaut adventures",
    "Time-traveling detectives",
    "Urban legends",
    "Solar system colonization",
    "Underground rebellions",
    "Cataclysmic events",
    "Interdimensional travelers",
    "Alternate history scenarios",
    "Cybernetic enhancements",
    "Psychological thrillers",
    "Environmental disasters",
    "Alien abductions",
    "Conscious AI beings",
    "Mind-bending illusions",
    "Lost civilizations rediscovered",
    "Survival horror situations",
    "Unexplained phenomena",
    "Robotic revolutions",
    "Political intrigue in futuristic societies",
    "Mythical quests",
    "Dystopian futures",
    "Apocalyptic wastelands",
    "Zen Garden"
]

formatted_topics = [topic.replace(" ", "+") for topic in topics_for_image_generation]
url_pattern_topics = [f"https://playgroundai.com/search?q={topic}" for topic in formatted_topics]



# image urls
image_urls= []



import requests
import json
from tqdm import tqdm
from bs4 import BeautifulSoup



print(f"{'>'*20}[STARTED]{'<'*20}")
for url_topic in tqdm(url_pattern_topics):
    try:
        response= requests.get(url_topic)
        soup= BeautifulSoup(response.content.decode())
        main_tag= soup.find_all("script")[-1]
        content= main_tag.contents
        content= str(content[0])
        json_data= json.loads(content)
        for data in json_data["props"]["pageProps"]["data"]:
            image_urls.append(data['url'])
        
        
        
        
    except:
        print(url_topic)
    
    
    
with open("outputs/image_playground_ai_imageurls.json", "w") as f:
    json.dump(
        image_urls,
        f
    )
    
print(f"Total urls collected: {len(image_urls)}")
print(f"{'>'*20}[COMPLETED]{'<'*20}")
