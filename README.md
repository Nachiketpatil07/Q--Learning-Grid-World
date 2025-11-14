# Q--Learning-Grid-World
A reinforcement learning project using Q-learning to navigate an agent through a grid-based environment towards a goal while optimizing rewards

🏴‍☠️ Treasure Hunt RL — Pirates of the Caribbean Edition
⚓ “Not all treasure is silver and gold, mate.” — Captain Jack Sparrow

Treasure Hunt RL is a reinforcement learning adventure inspired by the legendary Pirates of the Caribbean universe.
A lone pirate (your RL agent) must navigate a dangerous grid-world filled with curses, sea monsters, whirlpools, and deadly traps — all while seeking the ultimate treasure chest.

Powered by Q-learning, the agent learns to survive like a true pirate of the high seas.

🗺️ The Pirate Grid World

Your grid-world resembles a map charted by the Brethren Court:

Starting Point: Tortuga (bottom-left corner)

Destination: Isla de Muerta treasure 🏝️💰

Dangers Inspired by the Seas:

🔥 Cursed zones (Hell States)

🐍 Sea monsters (Kraken-like dangers)

🌊 Treacherous waters

🧱 Blocked reefs

👻 Ghost pirate tiles (if applicable)

Symbol	Meaning
🏴‍☠️	Captain Jack (the RL Agent)
💰	Treasure (Goal)
🔥	Cursed Hell State
🐍	Monster / Kraken zone
🌊	Sea tile
🧱	Impassable reef

Your pirate must learn the smartest way through dangerous Caribbean waters to reach the treasure.

🏆 Reward System — Like a Pirate's Code

The rewards follow the Code of the Pirate Brethren:

Event / Tile	Reward	Pirate Meaning
💰 Treasure Found	+20	“Aye! Gold in the chest!”
🔥 Cursed Hell State	–5	“Beware the curse of the Black Pearl!”
🐍 Monster Attacked	–3	“Touched by the Kraken.”
🚶 Normal Movement	–0.01	Wasted effort / rum
🚫 Invalid Move	–1	“That’s not how compass points.”

This shaping ensures the agent behaves like Jack Sparrow:
avoiding danger while chasing the biggest reward.

⚙️ Learning Parameters
Parameter	Value
Learning Rate (α)	0.1
Discount Factor (γ)	0.9
Exploration Strategy	ε-Greedy
ε Decay	Exponential
Episodes	(you can add your exact number)
⚔️ How the Pirate Learns (Q-Learning)

Your agent starts inexperienced — like Will Turner before he met Jack.
Through trial, error, curses, and loot, it learns the rules of the Caribbean:

Takes an action (North, South, East, West)

Observes the reward (gold or danger)

Updates its Q-table:

Q(s, a) ← Q(s, a) + α [R + γ max(Q(s')) − Q(s, a)]


Over time, it:

avoids cursed zones

escapes monsters

navigates smarter

optimizes its path to the Isle of Treasure

Eventually the pirate becomes a master of the seas, consistently reaching the treasure like a seasoned captain.

🎮 Caribbean-Themed Visualization

All sprites in /assets/ bring the world to life:

Pirate Agent → Jack Sparrow sprite

Hell states → Cursed flames

Treasure chest → Golden loot

Monster tiles → Sea serpent / Kraken

Sea tiles → Ocean waves

If you want, I can help you add an animated GIF of your game.

📦 Installation

Clone the project:

git clone https://github.com/Nachiketpatil07/Q--Learning-Grid-World.git
cd Q--Learning-Grid-World


Install required packages:

pip install -r requirements.txt


Run the project:

python src/main.py

📊 Results from the High Seas

As the pirate learns:

Fewer cursed tiles entered

Shorter routes to treasure

Q-values stabilize

Rewards per episode steadily rise

Your pirate transforms from a rum-loving wanderer to a deadly-accurate treasure hunter, worthy of the Black Pearl.

🏴‍☠️ Future Enhancements (Pirate Expansion Pack)

⚔️ Davy Jones AI (an enemy agent)

🛳️ Multi-agent crew system

🪝 Deep Q-Learning for complex seas

🌪️ Storm or whirlpool dynamic hazards

📜 Procedurally generated treasure maps

👑 Author

Developed by Nachiket Patil
Inspired by Reinforcement Learning and the world of Pirates of the Caribbean.

“The problem is not the problem. The problem is your attitude about the problem.”
— Captain Jack Sparrow

If you enjoyed this project, leave a ⭐ on the repo!
