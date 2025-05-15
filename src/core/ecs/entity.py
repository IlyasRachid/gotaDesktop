import uuid

class Entity:
    """
    Represents a single game object in the ECS (Entity Component System).
    Each entity can have multiple components attached to it, defining its behavior and attributes.
    """

    def __init__(self):
        self.id = uuid.uuid4().hex
        self._components = {}

    def add_component(self, component_type, component):
        """Attaches a component to the entity."""
        if not isinstance(component, component_type):
            raise TypeError(f"Component must be of type {component_type.__name__}")
        self._components[component_type] = component

    def get_component(self, component_type):
        """Retrieves a component of the specified type from the entity."""
        return self._components.get(component_type, None)

    def remove_component(self, component_type):
        """Removes a component of the specified type from the entity."""
        if component_type in self._components:
            del self._components[component_type]

    def has_component(self, component_type):
        """Checks if the entity has a specific component."""
        return component_type in self._components

