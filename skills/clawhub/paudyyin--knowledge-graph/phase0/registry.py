"""
Entity Type Registry.

Central registry for all entity and relation types in the domain-kit ontology.
Supports dynamic registration and validation.
"""

from typing import Dict, List, Optional, Set
from .models import EntityType


# Default entity types from domain-kit base.json
DEFAULT_ENTITY_TYPES = {
    "Device": EntityType(
        name="Device",
        description="物理或逻辑设备",
        fields={
            "name": {"type": "string", "required": True},
            "model": {"type": "string", "required": True},
            "manufacturer": {"type": "string", "required": False},
            "specs": {"type": "object", "required": False},
            "capabilities": {"type": "array", "required": False},
        },
    ),
    "CodeTemplate": EntityType(
        name="CodeTemplate",
        description="可复用的代码模板",
        fields={
            "name": {"type": "string", "required": True},
            "language": {"type": "string", "required": True},
            "content": {"type": "string", "required": True},
            "parameters": {"type": "array", "required": False},
            "description": {"type": "string", "required": False},
        },
    ),
    "Constraint": EntityType(
        name="Constraint",
        description="约束规则（编码规范/设备限制）",
        fields={
            "rule": {"type": "string", "required": True},
            "scope": {"type": "string", "required": False},
            "severity": {"type": "string", "required": True},
            "rationale": {"type": "string", "required": False},
        },
    ),
    "Protocol": EntityType(
        name="Protocol",
        description="通信协议定义",
        fields={
            "name": {"type": "string", "required": True},
            "version": {"type": "string", "required": False},
            "message_format": {"type": "string", "required": False},
            "endpoints": {"type": "array", "required": False},
        },
    ),
    "BestPractice": EntityType(
        name="BestPractice",
        description="历史最佳实践",
        fields={
            "title": {"type": "string", "required": True},
            "content": {"type": "string", "required": True},
            "tags": {"type": "array", "required": False},
            "examples": {"type": "array", "required": False},
        },
    ),
    # v2.0 new types
    "Scenario": EntityType(
        name="Scenario",
        description="应用场景",
        fields={
            "name": {"type": "string", "required": True},
            "description": {"type": "string", "required": False},
            "industry": {"type": "string", "required": False},
        },
    ),
    "Parameter": EntityType(
        name="Parameter",
        description="设备/模板的配置参数",
        fields={
            "name": {"type": "string", "required": True},
            "data_type": {"type": "string", "required": True},
            "default_value": {"type": "string", "required": False},
            "range": {"type": "string", "required": False},
        },
    ),
    "Failure": EntityType(
        name="Failure",
        description="故障模式",
        fields={
            "name": {"type": "string", "required": True},
            "symptom": {"type": "string", "required": False},
            "root_cause": {"type": "string", "required": False},
            "solution": {"type": "string", "required": False},
        },
    ),
    # PLC-specific types found in actual data
    "PLC": EntityType(
        name="PLC",
        description="PLC控制器设备",
        fields={
            "model": {"type": "string", "required": True},
            "cpu_type": {"type": "string", "required": False},
            "memory_limit": {"type": "integer", "required": False},
            "io_capacity": {"type": "integer", "required": False},
            "supported_languages": {"type": "array", "required": False},
            "program_size_limit": {"type": "integer", "required": False},
        },
    ),
    "WCSDevice": EntityType(
        name="WCSDevice",
        description="WCS系统设备",
        fields={
            "name": {"type": "string", "required": True},
            "type": {"type": "string", "required": False},
        },
    ),
}

# Default relation types
DEFAULT_RELATION_TYPES = {
    "applies_to": {"from": "Constraint", "to": "Device", "description": "约束适用于某设备"},
    "generates": {"from": "Scenario", "to": "CodeTemplate", "description": "场景生成代码模板"},
    "depends_on": {"from": "CodeTemplate", "to": "Device", "description": "代码模板依赖某设备"},
    "compatible_with": {"from": "Device", "to": "Protocol", "description": "设备兼容某协议"},
    # v2.0 new relation types
    "used_in": {"from": "Device", "to": "Scenario", "description": "设备被用于某场景"},
    "has_parameter": {"from": "Device", "to": "Parameter", "description": "设备具有某参数"},
    "causes": {"from": "Failure", "to": "Failure", "description": "故障因果关系"},
    # Relations found in actual data
    "dispatches_to": {"from": "WCSDevice", "to": "Device", "description": "WCS调度到设备"},
}


class EntityTypeRegistry:
    """
    Central registry for entity and relation types.
    
    Provides:
    - Type registration and lookup
    - Validation of entities against their types
    - Introspection of the type system
    """

    def __init__(self):
        self._entity_types: Dict[str, EntityType] = {}
        self._relation_types: Dict[str, Dict] = {}
        # Load defaults
        for name, et in DEFAULT_ENTITY_TYPES.items():
            self.register_entity_type(et)
        for name, rt in DEFAULT_RELATION_TYPES.items():
            self.register_relation_type(name, rt)

    def register_entity_type(self, entity_type: EntityType) -> None:
        """Register a new entity type."""
        self._entity_types[entity_type.name] = entity_type

    def register_relation_type(self, name: str, definition: Dict) -> None:
        """Register a new relation type."""
        self._relation_types[name] = definition

    def get_entity_type(self, name: str) -> Optional[EntityType]:
        """Look up an entity type by name."""
        return self._entity_types.get(name)

    def get_relation_type(self, name: str) -> Optional[Dict]:
        """Look up a relation type definition."""
        return self._relation_types.get(name)

    def list_entity_types(self) -> List[str]:
        """List all registered entity type names."""
        return list(self._entity_types.keys())

    def list_relation_types(self) -> List[str]:
        """List all registered relation type names."""
        return list(self._relation_types.keys())

    def validate_entity(self, entity_type_name: str, data: Dict) -> List[str]:
        """Validate entity data against its registered type."""
        et = self.get_entity_type(entity_type_name)
        if et is None:
            return [f"Unknown entity type: {entity_type_name}"]
        return et.validate_entity(data)

    def is_valid_relation_type(self, relation_type: str) -> bool:
        """Check if a relation type is registered."""
        return relation_type in self._relation_types

    def get_all_entity_types(self) -> Dict[str, EntityType]:
        """Return all registered entity types."""
        return dict(self._entity_types)

    def get_all_relation_types(self) -> Dict[str, Dict]:
        """Return all registered relation types."""
        return dict(self._relation_types)
