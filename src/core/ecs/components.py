"""
Centralized component definitions for the ECS system.
All game data attributes are defined here - no logic allowed.
"""

from dataclasses import dataclass
from typing import Tuple, Literal, Optional
import pygame

# --------------------------------------------------
# Core Component Types
# --------------------------------------------------

@dataclass
class Position:
    """2D world coordinates with optional rotation"""
    x: float = 0.0
    y: float = 0.0
    rotation: float = 0.0  # Degrees (0-360)

@dataclass
class Velocity:
    """Movement vector with optional angular velocity"""
    dx: float = 0.0  # Pixels/second
    dy: float = 0.0
    d_rotation: float = 0.0  # Degrees/second

# --------------------------------------------------
# Physics & Collision
# --------------------------------------------------

@dataclass
class Collider:
    """Circular collision area with layer filtering"""
    radius: float = 10.0
    layer: Literal['player', 'food', 'enemy'] = 'player'
    is_trigger: bool = False  # For non-physical collisions

@dataclass
class Rigidbody:
    """Physical properties for dynamics"""
    mass: float = 1.0
    friction: float = 0.1
    bounciness: float = 0.5

# --------------------------------------------------
# Rendering
# --------------------------------------------------

@dataclass
class Renderable:
    """Visual representation data"""
    color: Tuple[int, int, int] = (255, 0, 0)  # RGB
    radius: float = 10.0  # Derived from mass elsewhere
    z_index: int = 0  # Drawing order
    visible: bool = True

@dataclass
class Sprite:
    """Texture-based rendering"""
    image: Optional[pygame.Surface] = None
    source_rect: Optional[pygame.Rect] = None
    flip_x: bool = False

# --------------------------------------------------
# Gameplay Specific (Gota.io)
# --------------------------------------------------

@dataclass
class CellState:
    """Gota-specific cell properties"""
    mass: float = 100.0
    is_main_cell: bool = True  # For split cells
    split_cooldown: float = 0.0  # Seconds remaining
    last_split_time: float = 0.0

@dataclass
class PlayerControl:
    """Marks player-controlled entities"""
    mouse_sensitivity: float = 1.0
    current_target: Optional[Tuple[float, float]] = None

@dataclass
class AIControl:
    """AI-specific data"""
    behavior: Literal['wander', 'chase', 'flee'] = 'wander'
    target_entity_id: Optional[str] = None

# --------------------------------------------------
# Utility Components
# --------------------------------------------------

@dataclass
class Lifetime:
    """Time-based entity expiration"""
    remaining: float = 10.0  # Seconds
    timer: float = 0.0

@dataclass
class DebugInfo:
    """Development-only visualization"""
    show_colliders: bool = True
    show_velocity: bool = False