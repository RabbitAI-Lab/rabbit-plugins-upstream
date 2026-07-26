"""
Tests for script generation, template system, and validation.
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
print("Test: Script Generation & Templates & Validation")
print("=" * 60)

# 1. Template system
print("\n[1] Template System")
from daemon.script_gen.templates.registry import list_templates, load_template
tpls = list_templates()
test("Templates available", len(tpls) >= 5)
for t in tpls:
    test(f"  Template: {t['name']}", "params" in t)

# 2. Load template with params
script = load_template("capture_window", {
    "window_title": "Notepad",
    "save_path": r"C:\temp\test.png",
})
test("capture_window loaded", script is not None)
test("  title substituted", script["steps"][1]["params"]["title"] == "Notepad")
test("  path substituted", "test.png" in script["steps"][3]["params"]["path"])
test("  duration is float", isinstance(script["steps"][2]["params"]["duration"], float))
test("  duration value 1.0", script["steps"][2]["params"]["duration"] == 1.0)

# 3. Template with defaults
script2 = load_template("type_to_window", {"window_title": "Calc", "text": "hello"})
test("type_to_window loaded", script2 is not None)
test("  has if step", script2["steps"][5]["action"] == "if")
test("  enter_after default True", script2["steps"][5]["condition"] is True)

# 4. Missing required param
try:
    load_template("capture_window", {})
    test("Missing param error", False)
except ValueError:
    test("Missing param error", True)

# 5. Unknown template
try:
    load_template("nonexistent", {})
    test("Unknown template error", False)
except KeyError:
    test("Unknown template error", True)

# 6. JSON Schema validation
print("\n[2] JSON Schema Validation")
from daemon.script_gen.generator import validate_script
v = validate_script({"steps": [{"action": "sleep", "params": {"duration": 1}}]})
test("Valid simple script", v["valid"])
v = validate_script({"steps": [{"action": "nonexistent"}]})
test("Invalid action caught", not v["valid"])
v = validate_script({"steps": [{"action": "if", "then": [{"action": "nop"}]}]})
test("If missing condition caught", not v["valid"])
v = validate_script({"steps": [{"action": "loop", "body": [{"action": "nop"}]}]})
test("Loop missing times/while caught", not v["valid"])
v = validate_script({"steps": [{"action": "set"}]})
test("Set missing var caught", not v["valid"])

# 7. LLM client
print("\n[3] LLM Client")
from daemon.script_gen.llm_client import is_configured, config_help, extract_json
test("LLM not configured in test env", not is_configured())
help_text = config_help()
test("Help text has LLM_API_KEY", "LLM_API_KEY" in help_text)
test("Help text has LLM_BASE_URL", "LLM_BASE_URL" in help_text)
extracted = extract_json("Here:\n```json\n{\"steps\": []}\n```")
test("Extract json from fence", "steps" in extracted)
extracted2 = extract_json('{"steps": []}')
test("Extract bare json", "steps" in extracted2)

# 8. Generator without LLM
print("\n[4] Generator (no LLM)")
from daemon.script_gen.generator import generate_script
result = generate_script("open notepad and type hello")
test("Generator returns error", not result.get("valid"))
test("  error is LLM_NOT_CONFIGURED", "LLM_NOT_CONFIGURED" in result.get("error", ""))

# 9. Server dispatcher
print("\n[5] Server Dispatcher")
with open(os.path.join(BASE, "daemon", "server.py"), encoding="utf-8") as f:
    server_code = f.read()
for method in ["script_generate", "script_generate_and_run",
               "script_list_templates", "script_load_template"]:
    ok = method in server_code and "handle_" + method in server_code
    test(f"Dispatcher: {method}", ok)

# 10. _safe_eval has image_find
print("\n[6] Safe Eval Functions")
from daemon.script_engine.engine import _SAFE_LOCALS
expected_fns = {"window_exists", "pixel_color", "image_find", "window_list"}
actual_fns = set(_SAFE_LOCALS.keys())
test(f"All safe functions ({len(actual_fns)}/4)", expected_fns == actual_fns)

# Summary
print("\n" + "=" * 60)
total = PASS + FAIL
print(f"Results: {PASS}/{total} passed, {FAIL} failed")
if FAIL: print("[FAIL] Some tests failed!")
else: print("[OK] All tests passed!")
print("=" * 60)
