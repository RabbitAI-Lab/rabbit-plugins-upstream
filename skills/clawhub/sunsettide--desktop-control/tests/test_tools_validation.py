"""
Test tool call parameter validation layer.
"""
import sys, os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)

PASS = 0; FAIL = 0
def test(name, ok, detail=""):
    global PASS, FAIL
    if ok: PASS += 1; print(f"  [OK] {name}")
    else: FAIL += 1; print(f"  [FAIL] {name}  {detail}")

print("=" * 60)
print("Test: Tool Call Parameter Validation")
print("=" * 60)

from daemon.tools.executor import execute_tool_call, execute_tool_calls, _validate_arguments, _REQUIRED_PARAMS

# 1. Verify required params schema covers major tools
required_tools = {
    "find_text": ["text"],
    "click_text": ["text"],
    "type_to_text": ["text", "input"],
    "mouse_move": ["x", "y"],
    "keyboard_type": ["text"],
    "keyboard_press": ["key"],
    "window_focus": ["title"],
    "goal_run": ["goal"],
}
for tool, expected_params in required_tools.items():
    actual = _REQUIRED_PARAMS.get(tool, [])
    test(f"_REQUIRED_PARAMS has {tool}", tool in _REQUIRED_PARAMS and actual == expected_params,
         f"expected {expected_params}, got {actual}")

# 2. Missing required param returns error BEFORE handler
result = execute_tool_call("find_text", {})
test("find_text missing 'text'", "error" in result and "Missing required" in result["error"],
     result.get("error", ""))

result = execute_tool_call("mouse_move", {"x": 100})
test("mouse_move missing 'y'", "error" in result and "Missing required" in result["error"])

result = execute_tool_call("keyboard_type", {})
test("keyboard_type missing 'text'", "error" in result and "Missing required" in result["error"])

# 3. Valid params pass through to handler
result = execute_tool_call("window_list", {})
test("window_list (no required params)", "result" in result,
     f"got {list(result.keys())}")

# 4. Batch with missing params
batch = execute_tool_calls([
    {"id": "c1", "name": "find_text", "arguments": {}},
    {"id": "c2", "name": "window_list", "arguments": {}},
])
results = batch.get("results", [])
test("batch c1 finds missing param", len(results) >= 1 and "error" in results[0])
test("batch c2 still executes", len(results) >= 2 and "result" in results[1],
     f"got {list(results[1].keys()) if len(results) > 1 else 'N/A'}")

# 5. stop_on_error stops after first failure
batch2 = execute_tool_calls([
    {"id": "c3", "name": "find_text", "arguments": {}},
    {"id": "c4", "name": "window_list", "arguments": {}},
], stop_on_error=True)
res2 = batch2.get("results", [])
test("stop_on_error stops at first failure", len(res2) == 1,
     f"got {len(res2)} results")

# 6. Schema summary
test(f"_REQUIRED_PARAMS covers {len(_REQUIRED_PARAMS)} tools", len(_REQUIRED_PARAMS) >= 10)

# Summary
print()
total = PASS + FAIL
print(f"Results: {PASS}/{total} passed, {FAIL} failed")
if FAIL: print("[FAIL] Some tests failed!")
else: print("[OK] All tests passed!")
print("=" * 60)
