gota-desktop/
├── assets/ # Game resources
│ ├── sprites/ # Cell/food textures
│ ├── shaders/ # Optional GLSL for effects
│ └── sounds/ # Sound effects
│
├── docs/ # Documentation
│ ├── ARCHITECTURE.md # Design decisions
│ ├── API.md # Interface specs
│ └── GAME_RULES.md # Mechanics and rules
│
├── src/ # Source code
│ ├── core/ # Engine-agnostic code
│ │ ├── ecs/ # Entity Component System
│ │ │ ├── entity.py
│ │ │ └── systems/
│ │ │ ├── physics.py
│ │ │ ├── rendering.py
│ │ │ └── collision.py
│ │ │
│ │ ├── game/ # Game logic
│ │ │ ├── cell.py
│ │ │ ├── world.py
│ │ │ ├── spawner.py # Handles spawning of entities
│ │ │ └── game_state.py # Manages game state transitions
│ │ │
│ │ ├── ui/ # User Interface Elements
│ │ │ ├── menu.py
│ │ │ ├── hud.py
│ │ │ └── scoreboard.py
│ │ │
│ │ └── utils/ # Helpers
│ │ ├── vectors.py
│ │ ├── timers.py
│ │ └── math_utils.py
│ │
│ ├── pygame/ # PyGame-specific
│ │ ├── input.py # Mouse/keyboard
│ │ ├── viewport.py # Multi-window
│ │ └── renderer.py # Drawing
│ │
│ ├── ai/ # AI interface
│ │ ├── recorder.py # Game state logs
│ │ ├── base_agent.py # Parent class for all AIs
│ │ ├── basic_ai.py # Simple AI logic
│ │ ├── rl_agent.py # Reinforcement Learning agent
│ │ └── pathfinding.py # Optional pathfinding logic
│ │
│ ├── network/ # Networking for multiplayer
│ │ ├── client.py
│ │ ├── server.py
│ │ └── protocols.py
│ │
│ └── database/ # Data persistence
│ ├── player_data.py
│ └── high_scores.py
│
├── tests/ # Testing
│ ├── unit/
│ │ ├── test_cell.py
│ │ ├── test_physics.py
│ │ └── test_ai.py
│ └── integration/
│ ├── test_world.py
│ ├── test_collision.py
│ └── test_network.py
│
├── scripts/ # Utility scripts
│ ├── build.py # Packaging
│ ├── profile.py # Performance analysis
│ └── migrate.py # Database migrations
│
├── main.py # Entry point
├── requirements.txt # Dependencies
├── config.yaml # Configuration settings
└── .env # Environment variables
