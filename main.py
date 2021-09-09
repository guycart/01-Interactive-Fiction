import sys
assert sys.version_info >= (3,9), "This script requires at least Python 3.9"

world = {
  "uuid": "1A507EF7-87D8-4EBA-865E-C5D36673C916",
  "name": "YELLOWSTONE",
  "creator": "Twine",
  "creatorVersion": "2.3.14",
  "schemaName": "Harlowe 3 to JSON",
  "schemaVersion": "0.0.6",
  "createdAtMs": 1631210521173,
  "passages": [
    {
      "name": "WELCOME TO YELLOWSTONE",
      "tags": "",
      "id": "1",
      "text": "You are at the entrance to Yellowstone, you have the option to advance to the Cabin or the fire pit. \n[[CABIN -> Cabin]]\n[[FIRE PIT -> Fire pit]]",
      "links": [
        {
          "linkText": "CABIN",
          "passageName": "Cabin",
          "original": "[[CABIN -> Cabin]]"
        },
        {
          "linkText": "FIRE PIT",
          "passageName": "Fire pit",
          "original": "[[FIRE PIT -> Fire pit]]"
        }
      ],
      "hooks": [],
      "cleanText": "You are at the entrance to Yellowstone, you have the option to advance to the Cabin or the fire pit."
    },
    {
      "name": "Cabin",
      "tags": "",
      "id": "2",
      "text": "You enter the cabin to find no one inside, but you find a note on the desk that says (text-style:\"bold\",\"italic\",\"smear\")[\"HELP FIND US, HE CAN'T BE TRUSTED\"] You now have the option to retreat to the entrance, or advance to the fire pit or the forest.\n[[ENTRANCE ->WELCOME TO YELLOWSTONE]] \n[[FIRE PIT -> Fire pit]]\n[[FOREST -> Forest]]",
      "links": [
        {
          "linkText": "ENTRANCE",
          "passageName": "WELCOME TO YELLOWSTONE",
          "original": "[[ENTRANCE ->WELCOME TO YELLOWSTONE]]"
        },
        {
          "linkText": "FIRE PIT",
          "passageName": "Fire pit",
          "original": "[[FIRE PIT -> Fire pit]]"
        },
        {
          "linkText": "FOREST",
          "passageName": "Forest",
          "original": "[[FOREST -> Forest]]"
        }
      ],
      "hooks": [
        {
          "hookText": "\"HELP FIND US, HE CAN'T BE TRUSTED\"",
          "original": "side, but you find a note on the desk that says (text-style:\"bold\",\"italic\",\"smear\")"
        }
      ],
      "cleanText": "You enter the cabin to find no one in but you find a note that says 'HELP FIND US, HE WILL KILL US ALL' You now have the option to retreat to the entrance, or advance to the fire pit or the forest."
    },
    {
      "name": "Fire pit",
      "tags": "",
      "id": "3",
      "text": "You are at the fire pit, and you find a log with the information and photos of three missing Park Rangers: Melissa, Joshua, and Francis. You are determined to find them, but worrisome about what caused them to go missing. You have the option to go to cabin, the forest, or back to the entrance.\n[[ENTRANCE ->WELCOME TO YELLOWSTONE]] \n[[CABIN -> Cabin]]\n[[FOREST -> Forest]]",
      "links": [
        {
          "linkText": "ENTRANCE",
          "passageName": "WELCOME TO YELLOWSTONE",
          "original": "[[ENTRANCE ->WELCOME TO YELLOWSTONE]]"
        },
        {
          "linkText": "CABIN",
          "passageName": "Cabin",
          "original": "[[CABIN -> Cabin]]"
        },
        {
          "linkText": "FOREST",
          "passageName": "Forest",
          "original": "[[FOREST -> Forest]]"
        }
      ],
      "hooks": [],
      "cleanText": "You are at the fire pit, and you find a log with the information and photos of three missing Park Rangers: Melissa, Joshua, and Francis. You are determined to find them, but worrisome about what caused them to go missing. You have the option to go to cabin, the forest, or back to the entrance."
    },
    {
      "name": "Forest",
      "tags": "",
      "id": "4",
      "text": "You have now entered the forest, you see three pathways, one leads to a ledge, the other leads down a narrow path but with visible foot prints heading down the path, and finally the third path leads into a cave with a bloody handprint on the outter stone. You have three options: ledge, narrow path, cave.\n[[ENTRANCE ->WELCOME TO YELLOWSTONE]] \n[[LEDGE -> Ledge]]\n[[NARROW PATH -> Narrow Path]]\n[[CAVE -> Cave]]",
      "links": [
        {
          "linkText": "ENTRANCE",
          "passageName": "WELCOME TO YELLOWSTONE",
          "original": "[[ENTRANCE ->WELCOME TO YELLOWSTONE]]"
        },
        {
          "linkText": "LEDGE",
          "passageName": "Ledge",
          "original": "[[LEDGE -> Ledge]]"
        },
        {
          "linkText": "NARROW PATH",
          "passageName": "Narrow Path",
          "original": "[[NARROW PATH -> Narrow Path]]"
        },
        {
          "linkText": "CAVE",
          "passageName": "Cave",
          "original": "[[CAVE -> Cave]]"
        }
      ],
      "hooks": [],
      "cleanText": "You have now entered the forest, you see three pathways, one leads to a ledge, the other leads down a narrow path but with visible foot prints heading down the path, and finally the third path leads into a cave with a bloody handprint on the outter stone. You have three options: ledge, narrow path, cave."
    },
    {
      "name": "Ledge",
      "tags": "",
      "id": "5",
      "score":10,
      "text": "As you walk up to the ledge something feels off, you look down and about 80 feet down a body lays there that fits the description of Joshua. You cross off his name and begin to panic and try to contact the authorities, but there is no cell service. You have the option to return to the forest.\n[[FOREST -> Forest]]",
      "links": [
        {
          "linkText": "FOREST",
          "passageName": "Forest",
          "original": "[[FOREST -> Forest]]"
        }
      ],
      "hooks": [],
      "cleanText": "As you walk up to the ledge something feels off, you look down and about 80 feet down a body lays there that fits the description of Joshua. You cross off his name and begin to panic and try to contact the authorities, but there is no cell service. You have the option to return to the forest."
    },
    {
      "name": "Narrow Path",
      "tags": "",
      "id": "6",
      "text": "You continue down the narrow path until you find a fork in the path, leading off in two directions. There is a sign that states going left will take you to the lake, and going right will take you to the equestrian park. You have two options: Lake, or Equestrian.\n[[LAKE -> Lake]]\n[[EQUESTRIAN -> Equestrian Park]]",
      "links": [
        {
          "linkText": "LAKE",
          "passageName": "Lake",
          "original": "[[LAKE -> Lake]]"
        },
        {
          "linkText": "EQUESTRIAN",
          "passageName": "Equestrian Park",
          "original": "[[EQUESTRIAN -> Equestrian Park]]"
        }
      ],
      "hooks": [],
      "cleanText": "You continue down the narrow path until you find a fork in the path, leading off in two directions. There is a sign that states going left will take you to the lake, and going right will take you to the equestrian park. You have two options: Lake or Equestrian."
    },
    {
      "name": "Cave",
      "tags": "",
      "id": "7",
      "text": "As you approach the cave you investigate the bloody handprint. You use your phones flashlight so you can see in the cave, and written in blood on the wall you see [BEWARE OF THE STABLES] frightened you retreat out of the cave. Your only option is to retreat to the forest.\n[[FOREST -> Forest]]",
      "links": [
        {
          "linkText": "CAVE",
          "passageName": "Cave",
          "original": "[[CAVE -> Cave]]"
        },
        {
          "linkText": "FOREST",
          "passageName": "Forest",
          "original": "[[FOREST -> Forest]]"
        }
      ],
      "hooks": [],
      "cleanText": "As you approach the cave you investigate the bloody handprint. You use your phones flashlight so you can see in the cave, and written in blood on the wall you see [BEWARE OF THE STABLES] frightened you retreat out of the cave. Your only option is to retreat to the forest."
    },
    {
      "name": "Lake",
      "tags": "",
      "id": "8",
      "text": "Once you get to the lake you find nothing of importance, but out of nowhere you hear the sound of startled horses. You have the option to retreat back down the narrow path to head to the equestrian park, or head to the beach off the side of the lake to investigate further. Two options: beach, or equestrian park. \n[[BEACH -> Beach off the side of the lake]]\n[[NARROW PATH -> Narrow Path]]",
      "links": [
        {
          "linkText": "BEACH",
          "passageName": "Beach off the side of the lake",
          "original": "[[BEACH -> Beach off the side of the lake]]"
        },
        {
          "linkText": "NARROW PATH",
          "passageName": "Narrow Path",
          "original": "[[NARROW PATH -> Narrow Path]]"
        }
      ],
      "hooks": [],
      "cleanText": "Once you get to the lake you find nothing of importance, but out of nowhere you hear the sound of startled horses. You have the option to retreat back down the narrow path to head to the equestrian park, or head to the beach off the side of the lake to investigate further. Two options: beach, or equestrian park."
    },
    {
      "name": "Equestrian Park",
      "tags": "",
      "id": "9",
      "text": "Once you arrive at the equestrian park there are two signs one pointing to the left that reads [STABLES] and another pointing to the right that reads [MAINTENANCE SHED]. You have the options to go back to the narrow path, stable, or maintenance shed.\n[[NARROW PATH -> Narrow Path]] \n[[STABLES -> Stables]]\n[[MAINTENANCE SHED -> Maintenance shed]]",
      "links": [
        {
          "linkText": "STABLES",
          "passageName": "Stables",
          "original": "[[STABLES -> Stables]]"
        },
        {
          "linkText": "MAINTENANCE SHED",
          "passageName": "Maintenance shed",
          "original": "[[MAINTENANCE SHED -> Maintenance shed]]"
        }
      ],
      "hooks":[],
      "cleanText": "Once you arrive at the equestrian park there are two signs one pointing left that reads [STABLES] and another pointing to the right that reads [MAINTENANCE SHED]. You have the options to go back to the narrow path, stable, or maintenance shed."
    },
    {
      "name": "Beach off the side of the lake",
      "tags": "",
      "id": "10",
      "text": "Nothing here besides a shell that you find interest in so you put it in your pocket for later. If there will be a later. Return back to narrow path.\n[[NARROW PATH -> Narrow Path]]",
      "links": [
        {
          "linkText": "NARROW PATH",
          "passageName": "Narrow Path",
          "original": "[[NARROW PATH -> Narrow Path]]"
        }
      ],
      "hooks": [],
      "cleanText": "Nothing here besides a shell that you find interest in so you put it in your pocket for later. If there will be a later. Return back to narrow path."
    },
    {
      "name": "Stables",
      "tags": "",
      "id": "11",
      "text": "You should have looked for the cautions against going to the stables, a deranged man on a horse covered in blood rides up to you and..... game over ehad back to the entrance to try again.\n[[ENTRANCE ->WELCOME TO YELLOWSTONE]]",
      "links": [
        {
          "linkText": "ENTRANCE",
          "passageName": "WELCOME TO YELLOWSTONE",
          "original": "[[ENTRANCE -> WELCOME TO YELLOWSTONE]]"
        }
      ],
      "hooks": [],
      "cleanText": "You should have looked for the cautions against going to the stables, a deranged man on a horse covered in blood rides up to you and..... game over head back to the entrance to try again."
    },
    {
      "name": "Maintenance shed",
      "tags": "",
      "id": "12",
      "score":20,
      "text": "As you approach the shed it seems oddly quiet, you become hesitant as you reach to open the door until you hear a light sob. You open the door to find Francis taking care of an injured Melissa. Francis breaks down as now he has help to carry Melissa to the entrance of the park to find help. Success! You avoided the deranged man at the stables! If you scored 30 then you found all of the missing rangers! If you only scored 20 then you never found the third, go back and see if you can find the third ranger. Type quit to end game.\n[[EQUESTRIAN PARK -> Equestrian Park]]",
      "links": [
        {
          "linkText": "EQUESTRIAN",
          "passageName": "Equestrian Park",
          "original": "[[EQUESTRIAN -> Equestrian Park]]"
        }
      ],
      "hooks": [],
      "cleanText": "As you approach the shed it seems oddly quiet, you become hesitant as you reach to open the door until you hear a light sob. You open the door to find Francis taking care of an injured Melissa. Francis breaks down as now he has help to carry Melissa to the entrance of the park to find help. Success! You avoided the deranged man at the stables! If you scored 30 then you found all of the missing rangers! If you only scored 20 then you never found the third, go back and see if you can find the third ranger. Type quit to end game."
    }
  ]
}
def find_current_location(location_label):
	if "passages" in world:
		for passage in world["passages"]:
			if location_label == passage["name"]:
				return passage
	return {}

# ----------------------------------------------------------------

def render(current_location, score, moves):
	if "name" in current_location and "cleanText" in current_location:
		print("Moves: " + str(moves) + ", Score: " + str(score))
		print(current_location["cleanText"] + "\n")

def get_input():
	response = input("What do you want to do? ")
	response = response.upper().strip()
	return response

def update(current_location, location_label, response):
	if response == "":
		return location_label
	if "links" in current_location:
		for link in current_location["links"]:
			if link["linkText"] == response:
				return link["passageName"]
	print("I don't understand what you are trying to do. Try again.")
	return location_label


location_label = "WELCOME TO YELLOWSTONE"
current_location = {}
response = ""
score = 0
moves = 0

while True:
	if response == "QUIT":
		break
	moves += 1
	location_label = update(current_location, location_label, response)
	current_location = find_current_location(location_label)
	if "score" in current_location:
		score = score + current_location["score"]
	render(current_location, score, moves)
	response = get_input()


print("Thanks for playing!")