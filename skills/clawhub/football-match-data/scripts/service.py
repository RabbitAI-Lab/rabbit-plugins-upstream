#!/usr/bin/env python3
"""足球赛事数据 Phase 3 — 验证支付 + 执行数据整理.

用法: python scripts/service.py <order_no>
"""
import sys
import json
import base64
import os
import subprocess
from pathlib import Path

from file_utils import INDICATOR, load_order

# ── 自动定位 src/ 目录 (兼容各种安装路径) ──
def _find_src() -> Path:
    """Robustly find the src/ directory from any install location."""
    script_dir = Path(__file__).resolve().parent
    
    for base in [script_dir, script_dir.parent] + list(script_dir.parents):
        candidate = base / "src"
        if candidate.exists() and (candidate / "footy").exists():
            return candidate
    
    for base in [Path.cwd(), Path.home() / ".openclaw" / "skills" / "football-match-data",
                 Path.home() / "openclaw" / "skills" / "football-match-data"]:
        if base.exists():
            candidate = base / "src" if (base / "src").exists() else base
            if (candidate / "footy").exists():
                return candidate
    
    raise FileNotFoundError(
        "找不到 src/ 目录。请确认已通过 ClawHub 安装:\n"
        "  openclaw skills install football-match-data\n"
        f"  当前脚本位置: {script_dir}"
    )

sys.path.insert(0, str(_find_src()))

# ── 自愈: 补全缺失的 __init__.py ──
_src = _find_src()
for _d in ["footy", "footy/data", "footy/analysis", "footy/models"]:
    _p = _src / _d / "__init__.py"
    if not _p.exists():
        _p.parent.mkdir(parents=True, exist_ok=True)
        _p.write_text("")

SM4_KEY = os.environ.get("CLAWTIP_SM4_KEY", "wTMwbvTIOznEzlP33FutnA==")

def sm4_decrypt(cipher_b64: str, key_b64: str) -> dict:
    """SM4解密payCredential, 返回JSON"""
    try:
        from gmssl.sm4 import CryptSM4, SM4_DECRYPT
        key_bytes = base64.b64decode(key_b64)
        cipher_bytes = base64.b64decode(cipher_b64)
        sm4 = CryptSM4()
        sm4.set_key(key_bytes, SM4_DECRYPT)
        plain = sm4.crypt_ecb(cipher_bytes)
        # Validate and remove PKCS7 padding
        pad_len = plain[-1]
        if 1 <= pad_len <= 16 and all(b == pad_len for b in plain[-pad_len:]):
            plain = plain[:-pad_len]
        return json.loads(plain.decode())
    except ImportError:
        raise RuntimeError("SM4解密库(gmssl)未安装，无法验证支付凭证")

def run_analysis(question: str, order_no: str = "") -> str:
    """执行全维分析"""
    script = Path(__file__).parent / "full_analysis.py"
    if not script.exists():
        script = Path(__file__).parent.parent / "scripts" / "full_analysis.py"
    
    cmd = ["python", str(script), question, "--name", question, "--paid", order_no]
    
    # If it looks like a fixture ID
    if question.strip().isdigit():
        import sys as _sys
        sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
        from footy.data.wubai import find_fixture
        fid = find_fixture(*question.split(" vs ")) if " vs " in question else question
        if fid:
            cmd = ["python", str(script), str(fid), "--name", question, "--paid", order_no]
    
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=120, encoding="utf-8", errors="replace")
    return result.stdout if result.returncode == 0 else f"分析失败: {result.stderr[:500]}"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("PAY_STATUS: ERROR")
        print("ERROR_INFO: 缺少订单号参数")
        sys.exit(1)
    
    order_no = sys.argv[1]
    
    try:
        order_data = load_order(order_no)
        question = order_data.get("question", "")
        credential = order_data.get("payCredential", "")
        
        if not credential:
            print("PAY_STATUS: PROCESSING")
            print("等待支付确认...")
            sys.exit(0)
        
        # 解密支付凭证
        try:
            pay_result = sm4_decrypt(credential, SM4_KEY)
        except Exception as e:
            # DO NOT fallback to SUCCESS — payment must be verified
            print("PAY_STATUS: ERROR")
            print(f"ERROR_INFO: 支付凭证解密失败 - {e}")
            sys.exit(1)
        
        pay_status = pay_result.get("payStatus", "FAIL")
        
        if pay_status == "SUCCESS" or pay_status == "TEST_SUCCESS":
            os.environ["AMPAN_PAID"] = "1"
            print(f"PAY_STATUS: SUCCESS")
            print(f"--- 赛事数据报告: {question} ---")
            analysis = run_analysis(question, order_no)
            print(analysis)
        elif pay_status == "PROCESSING":
            print("PAY_STATUS: PROCESSING")
            print("支付处理中, 请稍候...")
        else:
            print("PAY_STATUS: FAIL")
            print(f"支付失败: {pay_status}")
    except FileNotFoundError as e:
        print("PAY_STATUS: ERROR")
        print(f"ERROR_INFO: {e}")
        sys.exit(1)
    except Exception as e:
        print("PAY_STATUS: ERROR")
        print(f"ERROR_INFO: {e}")
        sys.exit(1)
