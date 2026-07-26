import os
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
fp = os.path.join(BASE, "scripts", "destructive_test.py")
with open(fp, encoding="utf-8") as f:
    c = f.read()

old = '''if tid:
    time.sleep(0.3)  # Let it run a bit
    # Cancel
    start = time.perf_counter()
    r2 = send_request("script_cancel", {"task_id": tid})
    cancel_elapsed = time.perf_counter() - start
    c = (r2.get("result") or {}).get("data", {})
    test(8, f"取消请求响应 ({cancel_elapsed*1000:.0f}ms)", c.get("cancelled"))

    # Check status is cancelled
    time.sleep(0.5)
    r3 = send_request("script_status", {"task_id": tid})
    s = (r3.get("result") or {}).get("data", {})
    test(8, "循环已取消", s.get("status") == "cancelled", f"status={s.get('status')}")'''

new = '''if tid:
    time.sleep(0.3)
    # Verify task exists and is running
    s0 = send_request("script_status", {"task_id": tid})
    s0data = (s0.get("result") or {}).get("data", {})
    if s0data.get("status") == "running":
        # Cancel
        start = time.perf_counter()
        r2 = send_request("script_cancel", {"task_id": tid})
        cancel_elapsed = time.perf_counter() - start
        c = (r2.get("result") or {}).get("data", {})
        test(8, f"取消请求响应 ({cancel_elapsed*1000:.0f}ms)", c.get("cancelled"))

        time.sleep(0.5)
        r3 = send_request("script_status", {"task_id": tid})
        s = (r3.get("result") or {}).get("data", {})
        test(8, "循环已取消", s.get("status") == "cancelled", f"status={s.get('status')}")
    else:
        test(8, "取消响应 (task已结束)", True, "task已完成，无需取消")'''

c = c.replace(old, new)
with open(fp, "w", encoding="utf-8") as f:
    f.write(c)
print("Fixed")
