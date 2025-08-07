#!/usr/bin/env python3
# type: ignore
"""
Test file with high chaos potential - deliberately messy to test chaos index
This file has inconsistent naming, lots of imports, and general complexity
Note: Type checking is intentionally disabled for this chaotic test file
"""

# Random imports to increase chaos (keeping only the used ones)
import os
import tempfile
from typing import Dict, Any, Union

# Some chaotic code patterns
class TemporaryUtilityClassForTestingChaosIndex:
    def __init__(self) -> None:
        self.data: Dict[str, Any] = {}
        self.backup_data: Dict[str, Any] = {}
        self.temp_data: Dict[str, Any] = {}
        self.old_data: Dict[str, Any] = {}
        
    def process_complicated_stuff(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        # Intentionally complex nested logic with type checking suppressed for chaos
        # type: ignore
        result: Dict[str, Any] = {}
        for key, value in input_data.items():
            if isinstance(value, dict):
                for nested_key, nested_value in value.items():
                    try:
                        if nested_key.startswith("temp_") or nested_key.endswith("_backup"):
                            # Complex processing that's hard to follow
                            processed = self._apply_transformation(nested_value)
                            result[f"{key}_{nested_key}_processed"] = processed
                    except AttributeError:
                        # Handle non-string keys gracefully
                        pass
            else:
                result[key] = value
        return result
    
    def _apply_transformation(self, data: Any) -> Union[str, int]:
        # More chaos
        if isinstance(data, str):
            return data.upper().replace(" ", "_").replace("-", "_")
        elif isinstance(data, int):
            return data * 42 + 1337
        else:
            return str(data)

# Global variables (chaotic)
GLOBAL_CHAOS_MULTIPLIER = 3.14159
TEMPORARY_STORAGE = []
OLD_DEPRECATED_VARIABLE = "should_be_removed"

def main() -> None:
    """Main function - also chaotic"""
    util = TemporaryUtilityClassForTestingChaosIndex()
    test_data: Dict[str, Any] = {
        "temp_config": {"backup_setting": "chaos"},
        "normal_data": 42
    }
    
    result = util.process_complicated_stuff(test_data)
    print(f"Chaos result: {result}")
    
    # Random file operations to increase chaos score
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmp:
        tmp.write("temporary chaos data")
        tmp_path = tmp.name
    
    os.unlink(tmp_path)
    
if __name__ == "__main__":
    main()
