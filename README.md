# 🧠 Open Trivia Quiz (Terminal Edition) - v2.1

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![Version](https://img.shields.io/badge/Version-2.1-green)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Language](https://img.shields.io/badge/Language-English-lightgrey)
![Status](https://img.shields.io/badge/Status-Stable-brightgreen)
![API](https://img.shields.io/badge/API-Open%20Trivia%20DB-9cf)
![DB](https://img.shields.io/badge/Database-Supabase-3fcf8e?logo=supabase)
![Connection](https://img.shields.io/badge/Supabase%20Connection-Active-success)

A **terminal-based trivia game** that connects to the [Open Trivia Database API](https://opentdb.com/)  
and integrates with **Supabase** to store player data, scores, and statistics.  
This version introduces user profiles, persistent scores, and improved game logic.

---

## 🚀 Features (v2.1)
- ✅ Player registration and login system (via Supabase)
- ✅ Score saving and leaderboard tracking
- ✅ Selectable difficulty and category
- ✅ Dynamic question loading from Open Trivia DB
- ✅ Clean MVC structure (Models, Views, Controllers)
- ✅ Loading animations and progress bar
- ✅ Clear, interactive terminal UI

---

## 📋 Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Features](#-features-v20)
- [Planned Features](#-planned-features)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🧩 Project Structure
```
TRIVIA-QUIZ-APP/
│
├── src/
│   ├── main.py                # Entry point
│   ├── Controllers/
│   │   ├── quiz_controller.py
│   │   └── quiz_controller.py
│   ├── Models/
│   │   ├── api_model.py       # Handles Open Trivia DB requests
│   │   └── supabase_model.py  # Handles Supabase database actions
│   ├── Views/
│   │   └── ui.py              # Terminal UI components
│   └── utils/                 # (optional) Helper functions, constants, etc.
│
├── .env
├── README.md
├── requirements.txt
└── LICENSE
```

---

## ⚙️ Installation

### Setup
1. Clone this repository:
```bash
git clone https://github.com/OrellanaJheremiasT/TRIVIA-QUIZ-APP.git
cd TRIVIA-QUIZ-APP/src
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```
---

## ▶️ Usage
Run the game from the terminal:
```bash
python main.py
```

Then:
1. Enter your player name (or log in if already registered)
2. Choose category and difficulty
3. Play and see your score saved automatically 🎯

---

---

## 🔮 Planned Features
Future updates (v3.0+) will include:
- 🏆 Global leaderboard display
- 🎨 Improved terminal UI experience

---

## 🤝 Contributing
Contributions are welcome!  
You can:
- Report bugs via **Issues**
- Suggest new features
- Submit **Pull Requests**

Please follow the MVC organization used in `/src`.

---

## 🧾 License
This project is licensed under the **MIT License** — see the LICENSE file for details.

**Version:** 2.1 (Stable)  
**Author:** [OrellanaJheremiasT](https://github.com/OrellanaJheremiasT)  
**Repository:** [github.com/OrellanaJheremiasT/TRIVIA-QUIZ-APP](https://github.com/OrellanaJheremiasT/TRIVIA-QUIZ-APP)
