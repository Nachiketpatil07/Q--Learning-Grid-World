# Q--Learning-Grid-World
A reinforcement learning project using Q-learning to navigate an agent through a grid-based environment towards a goal while optimizing rewards
Perfect — I’ll create a README **exactly similar in style, tone, structure, and emojis** to your friend’s One Piece–themed README, but tailored **100% to YOUR project** (Treasure Hunt Q-Learning with pirate theme + hell states + treasure + sea monsters).

Here is your **final polished README**, ready to paste into GitHub:

---

# 🏴‍☠️ **Treasure Hunt RL — Pirate Q-Learning Adventure**

## 📜 **Project Overview**

**Treasure Hunt RL** is a grid-world reinforcement learning adventure where a pirate agent must navigate through dangerous seas, hell zones, sea monsters, and obstacles to reach the **hidden treasure chest**.

Using **Q-learning**, the agent gradually learns:

* how to avoid danger
* how to take the safest path
* how to maximize rewards
* how to reach the treasure efficiently

The entire world is designed with pirate-themed sprites, making learning visual and interactive!

---

## 🌍 **The Grid World**

**Grid Size:** (add your grid size here — e.g. 10×10)
**Agent Movement:** Up, Down, Left, Right
**Start Location:** Bottom-left
**Treasure Location:** Top-right
**Environment Features:**

| Tile  | Meaning                     |
| ----- | --------------------------- |
| 💰    | Treasure (Goal)             |
| 🔥    | Hell state / Dangerous tile |
| 🐍    | Sea monster                 |
| 🌊    | Sea tile                    |
| 🧱    | Obstacle / Blocked tile     |
| 🏴‍☠️ | Pirate agent                |

The agent must **survive danger**, learn optimal routes, and reach the treasure while minimizing total penalties.

---

## 🏆 **Reward Structure**

| Event / Tile                 | Reward                        |
| ---------------------------- | ----------------------------- |
| 💰 **Reaching Treasure**     | **+20**                       |
| 🔥 **Entering Hell State**   | **–5**                        |
| 🐍 **Sea Monster**           | **–3** (or your actual value) |
| 🚶 **Normal Move**           | –0.01                         |
| 🚫 **Invalid Move**          | –1                            |
| ⭐ **Special Bonus (if any)** | +10                           |

This reward setup encourages the pirate to avoid danger and find the safest + shortest path.

---

## ⚙️ **Learning Parameters**

| Parameter            | Value                      |
| -------------------- | -------------------------- |
| Learning Rate (α)    | 0.1                        |
| Discount Factor (γ)  | 0.9                        |
| Exploration Strategy | ε-Greedy                   |
| ε Decay              | Exponential                |
| Episodes             | (add your count e.g. 1000) |

If you want, I can include the exact epsilon decay formula you used.

---

## 🚀 **How the Agent Learns**

1. The pirate spawns in the **bottom-left** corner.
2. It moves through the grid using an ε-greedy strategy.
3. Each move updates the Q-table using:

```
Q(s, a) ← Q(s, a) + α [ R + γ * max(Q(s’)) – Q(s, a) ]
```

4. The pirate learns:

   * to avoid hell state tiles
   * to bypass sea monsters
   * to minimize random wandering
   * to reach the treasure faster

After enough episodes, the pirate becomes **smart**, consistently taking the safest and most rewarding path.

---

## 🖥️ **Visualization (Sprites / Images)**

Your project uses images stored in `/assets/` to create a visualized grid:

* hell_state_1.png … hell_state_5.png
* reward / treasure sprites
* pirate_agent.png
* sea_tile.png

This makes the environment lively and perfect for demos.

If you want, I can help you add a **pygame animation / GIF preview** inside your README.

---

## 📦 **Installation & Setup**

Clone the repository:

```bash
git clone https://github.com/Nachiketpatil07/Q--Learning-Grid-World.git
cd Q--Learning-Grid-World
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the training or visualization:

```bash
python src/main.py
```

---

## 📊 **Results & Learning Progress**

* Q-table converges over episodes
* Agent learns danger zones
* Stops entering hell states
* Finds shortest + safest route
* Episode reward improves steadily

If you'd like, I can help you plot:

✔ Reward per episode
✔ Steps per episode
✔ Q-table heatmap
✔ Agent path visualizations

---

## 🎯 **Future Improvements**

* Deep Q-Learning (DQN)
* Randomized environments each episode
* Moving sea monsters (dynamic enemies)
* Multi-agent treasure hunting (Pirate Crew AI)
* Larger maps or procedural worlds

---

## 🖊️ **Author**

Developed by **Nachiket Patil**
Inspired by reinforcement learning and pirate-themed exploration 🏴‍☠️

If you like this project, consider ⭐ starring the repo!

---

# ⭐ If you want it even more like your friend’s version:

I can add:

* Story introduction ("East Blue → Grand Line" style for pirates)
* ASCII map of your grid
* Training GIFs
* Custom color sections
* Shields.io badges
* Professional project banner

Just tell me what theme or style you want (serious, fun, anime-style, fully pirate-themed, etc.).
