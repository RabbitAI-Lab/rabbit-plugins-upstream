#!/usr/bin/env python3
"""Local-only web UI for authorized server scans and explicitly confirmed fixes.

Run: python scripts/web_ui.py [--host 127.0.0.1] [--port 8765]
The UI binds loopback only. Do not expose this service to a network.
"""
import argparse
import hmac
import json
import os
import re
import secrets
import subprocess
import sys
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse

SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_ROOT = SCRIPT_DIR.parent
TOKEN = secrets.token_urlsafe(32)
SESSIONS = {}
SESSION_TTL = 1800
LOCK = threading.Lock()
MAX_BODY = 64 * 1024

PAGE = r'''<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Server Security Guard</title>
<style>
:root{color-scheme:dark;--bg:#10151c;--panel:#18212c;--line:#2a3949;--text:#e8eef5;--muted:#9aabbd;--accent:#55c2a3;--warn:#e8b45b;--bad:#ef7272}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--text);font:15px/1.5 system-ui,"Segoe UI",sans-serif}main{max-width:1050px;margin:32px auto;padding:0 18px}h1{font-size:25px;margin:0 0 4px}.sub{color:var(--muted);margin:0 0 22px}.bar,.card{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:16px;margin:12px 0}.row{display:flex;gap:12px;align-items:end;flex-wrap:wrap}label{display:block;color:var(--muted);font-size:13px;margin-bottom:5px}input[type=text],input[type=number]{background:#0e141b;border:1px solid var(--line);border-radius:7px;color:var(--text);padding:10px 12px;font:inherit}#target{width:min(520px,80vw)}button{border:0;border-radius:7px;background:var(--accent);color:#08130f;font-weight:700;padding:10px 16px;cursor:pointer}button:disabled{opacity:.45;cursor:not-allowed}.secondary{background:#2b3c4e;color:var(--text)}.danger{background:var(--bad);color:#270b0b}.meta{color:var(--muted);font-size:13px}.finding{border-top:1px solid var(--line);padding:13px 2px;display:grid;grid-template-columns:24px 90px 1fr;gap:8px}.sev{font-size:12px;font-weight:700}.CRITICAL,.HIGH{color:var(--bad)}.MEDIUM{color:var(--warn)}.LOW,.INFO{color:var(--muted)}.evidence{font:12px ui-monospace,monospace;color:#b5c4d2;white-space:pre-wrap;overflow-wrap:anywhere;margin-top:4px}.actions{display:flex;gap:10px;align-items:center;flex-wrap:wrap;margin-top:14px}.status{margin:14px 0;padding:11px;border-radius:8px;background:#111923;white-space:pre-wrap}.hidden{display:none}.notice{color:var(--warn);font-size:13px}.check{margin:0}.modal{position:fixed;inset:0;background:#000b;display:grid;place-items:center;padding:18px}.modalbox{max-width:500px;width:100%;background:var(--panel);border:1px solid var(--line);padding:20px;border-radius:12px}.modalbox input{width:100%;margin:10px 0}.right{margin-left:auto}@media(max-width:600px){.finding{grid-template-columns:24px 70px 1fr}}
</style></head><body><main><h1>服务器安全防护</h1><p class="sub">仅供已授权服务器使用 · 服务只监听本机 · 默认先预览，修复须再次明确确认</p>
<section class="bar"><div class="row"><div><label for="target">目标</label><input id="target" type="text" value="local" placeholder="local 或 ssh://user@host[:port]" autocomplete="off"></div><div><label for="scope">扫描范围</label><select id="scope" style="background:#0e141b;color:var(--text);padding:10px;border:1px solid var(--line);border-radius:7px"><option>all</option><option>config</option><option>service</option><option>port</option><option>patch</option><option>ssh</option></select></div><button id="scan">开始扫描</button></div><p class="notice">修复会修改远端系统。先检查扫描证据与 dry-run 命令；仅对你有授权的主机执行。</p></section>
<div id="status" class="status hidden"></div><section id="results" class="card hidden"></section>
</main><div id="modal" class="modal hidden"><div class="modalbox"><h2>确认实际修复</h2><p id="confirmText">将对目标执行实际系统变更。确认已审核所选项及 dry-run 命令。</p><label for="phrase">输入 APPLY 才能继续</label><input id="phrase" type="text" autocomplete="off"><div class="actions"><button class="secondary right" id="cancel">取消</button><button class="danger" id="apply" disabled>执行修复</button></div></div></div>
<script>
(()=>{const token=location.hash.slice(1);history.replaceState(null,"",location.pathname);const $=s=>document.querySelector(s);let scanData=null,scanKey=null;
async function api(path,body){const r=await fetch(path,{method:body?"POST":"GET",headers:{"Authorization":"Bearer "+token,...(body?{"Content-Type":"application/json"}:{})},body:body?JSON.stringify(body):undefined});const d=await r.json();if(!r.ok)throw Error(d.error||`HTTP ${r.status}`);return d}
function show(msg){$('#status').textContent=msg;$('#status').classList.remove('hidden')}
$('#scan').onclick=async()=>{const target=$('#target').value.trim();if(!target)return show('请输入目标');$('#scan').disabled=true;$('#results').classList.add('hidden');show('扫描中…');try{scanData=await api('/api/scan',{target,scope:$('#scope').value});scanKey=scanData.scan_id;render(scanData)}catch(e){show('扫描失败：'+e.message)}finally{$('#scan').disabled=false}};
function render(d){const fs=d.findings||[];let html=`<h2>扫描结果</h2><p class="meta">目标：${esc(d.target)} · ${esc(d.timestamp)} · 共 ${fs.length} 项</p>`;if(!fs.length)html+='<p>未发现已实现规则命中的问题。未实现的检查项仍需人工核查。</p>';for(const f of fs){const safe=!!f.auto_fixable;html+=`<div class="finding"><input class="check" type="checkbox" data-id="${esc(f.id)}" ${safe?'':'disabled'} ${safe?'checked':''}><div class="sev ${esc(f.severity)}">${esc(f.severity)}<br>${esc(f.id)}</div><div><strong>${esc(f.title)}</strong>${safe?'':' <span class="meta">· 不支持自动修复</span>'}<div class="evidence">${esc(f.evidence||'')}</div></div></div>`}html+=`<div class="actions"><span class="meta">默认选中可自动修复项，可按需取消选择。</span><button id="preview">生成修复预览</button></div><div id="previewBox"></div>`;$('#results').innerHTML=html;$('#results').classList.remove('hidden');show('扫描完成。');$('#preview').onclick=preview}
async function preview(){const ids=[...document.querySelectorAll('.check:checked')].map(e=>e.dataset.id);if(!ids.length)return show('没有选择可自动修复项。');show('生成 dry-run 预览…');try{const d=await api('/api/preview',{scan_id:scanKey,items:ids});let h='<h3>Dry-run 预览（尚未改动系统）</h3>';for(const r of d.results||[]){h+=`<div class="finding"><span></span><div class="sev">${esc(r.status)}</div><div><strong>${esc(r.item_id)}</strong><div class="evidence">${esc((r.commands||[]).join('\n'))}</div><div class="meta">${esc(r.message||'')}</div></div></div>`}h+='<div class="actions"><span class="notice">确认前请核对目标、项目、命令与回滚方式。</span><button class="danger" id="openConfirm">确认并修复所选项</button></div>';$('#previewBox').innerHTML=h;show('Dry-run 完成，系统尚未改动。');$('#openConfirm').onclick=()=>{$('#phrase').value='';$('#apply').disabled=true;$('#modal').classList.remove('hidden')}}catch(e){show('预览失败：'+e.message)}}
$('#phrase').oninput=()=>$('#apply').disabled=$('#phrase').value.trim()!=='APPLY';$('#cancel').onclick=()=>$('#modal').classList.add('hidden');
$('#apply').onclick=async()=>{const ids=[...document.querySelectorAll('.check:checked')].map(e=>e.dataset.id);$('#apply').disabled=true;show('正在执行实际修复…');try{const d=await api('/api/apply',{scan_id:scanKey,items:ids,confirmation:$('#phrase').value.trim()});$('#modal').classList.add('hidden');const box=$('#previewBox');let h='<h3>执行结果</h3>';for(const r of d.results||[]){h+=`<div class="finding"><span></span><div class="sev">${esc(r.status)}</div><div><strong>${esc(r.item_id)}</strong><div class="evidence">${esc((r.commands||[]).join('\n'))}</div><div class="meta">${esc(r.message||'')}</div><div class="evidence">回滚：${esc((r.rollback_commands||[]).join('\n')||'无')}</div></div></div>`}box.innerHTML=h;show('执行完成；请检查各项状态与回滚信息。')}catch(e){show('执行失败：'+e.message)}finally{$('#apply').disabled=$('#phrase').value.trim()!=='APPLY'}};
function esc(x){return String(x??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]))}
})();
</script></body></html>'''


def valid_target(target):
    import sys
    sys.path.insert(0, str(SCRIPT_DIR))
    import _common
    _common.parse_target(target)
    return target


def run_script(name, args, timeout=180):
    path = SCRIPT_DIR / name
    p = subprocess.run([sys.executable, str(path), *args], capture_output=True,
                       text=True, encoding="utf-8", errors="replace", timeout=timeout,
                       cwd=str(SKILL_ROOT))
    if p.returncode != 0:
        raise RuntimeError((p.stderr.strip() or p.stdout.strip() or f"{name} failed")[-3000:])
    try:
        return json.loads(p.stdout)
    except json.JSONDecodeError as e:
        raise RuntimeError(f"{name} 输出非 JSON: {e}; {p.stderr[-1000:]}")


def purge_sessions():
    now = time.time()
    with LOCK:
        for key in list(SESSIONS):
            if now - SESSIONS[key]["created"] > SESSION_TTL:
                del SESSIONS[key]


class Handler(BaseHTTPRequestHandler):
    server_version = "ServerSecurityGuardUI/1.0"

    def log_message(self, fmt, *args):
        sys.stderr.write("[web-ui] " + (fmt % args) + "\n")

    def _json(self, code, obj):
        data = json.dumps(obj, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Content-Security-Policy", "default-src 'none'; style-src 'unsafe-inline'; script-src 'unsafe-inline'; connect-src 'self'; base-uri 'none'; frame-ancestors 'none'")
        self.end_headers()
        self.wfile.write(data)

    def _authorized(self):
        host = self.headers.get("Host", "").split(":", 1)[0].strip("[]").lower()
        if host not in ("127.0.0.1", "localhost", "[::1]", "::1"):
            return False
        origin = self.headers.get("Origin")
        if origin:
            parsed = urlparse(origin)
            if parsed.hostname not in ("127.0.0.1", "localhost", "::1"):
                return False
        supplied = self.headers.get("Authorization", "")
        return supplied.startswith("Bearer ") and hmac.compare_digest(supplied[7:], TOKEN)

    def _body(self):
        try:
            size = int(self.headers.get("Content-Length", "0"))
        except ValueError:
            raise ValueError("invalid Content-Length")
        if size <= 0 or size > MAX_BODY:
            raise ValueError("request body size out of range")
        data = json.loads(self.rfile.read(size).decode("utf-8"))
        if not isinstance(data, dict):
            raise ValueError("JSON object required")
        return data

    def do_GET(self):
        if self.path != "/":
            return self._json(404, {"error": "not found"})
        body = PAGE.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("Referrer-Policy", "no-referrer")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Content-Security-Policy", "default-src 'none'; style-src 'unsafe-inline'; script-src 'unsafe-inline'; connect-src 'self'; base-uri 'none'; frame-ancestors 'none'")
        self.end_headers()
        self.wfile.write(body)

    def do_POST(self):
        if not self._authorized():
            return self._json(403, {"error": "forbidden: local access token required"})
        try:
            body = self._body()
            route = urlparse(self.path).path
            purge_sessions()
            if route == "/api/scan":
                target = valid_target(str(body.get("target", "")))
                scope = str(body.get("scope", "all"))
                if scope not in ("all", "config", "service", "port", "patch", "ssh"):
                    raise ValueError("invalid scan scope")
                result = run_script("vuln_scan.py", ["--target", target, "--scope", scope])
                scan_id = secrets.token_urlsafe(24)
                with LOCK:
                    SESSIONS[scan_id] = {"created": time.time(), "target": target, "scan": result}
                return self._json(200, {"scan_id": scan_id, "target": target,
                                        "timestamp": result.get("timestamp"),
                                        "findings": result.get("findings", []),
                                        "summary": result.get("summary", {}),
                                        "total": result.get("total", 0),
                                        "errors": result.get("errors", [])})
            if route in ("/api/preview", "/api/apply"):
                scan_id = str(body.get("scan_id", ""))
                with LOCK:
                    session = SESSIONS.get(scan_id)
                if not session or time.time() - session["created"] > SESSION_TTL:
                    raise ValueError("scan session missing or expired; rescan first")
                available = {f["id"] for f in session["scan"].get("findings", [])
                             if f.get("auto_fixable", True)}
                items = body.get("items")
                if not isinstance(items, list) or not items or len(items) > 80:
                    raise ValueError("select one or more repair item IDs")
                items = list(dict.fromkeys(str(x) for x in items))
                if any(x not in available for x in items):
                    raise ValueError("selected item was not marked auto-fixable in this scan")
                with __import__("tempfile").TemporaryDirectory(prefix="ssg-web-") as td:
                    inp = Path(td) / "scan.json"
                    inp.write_text(json.dumps(session["scan"], ensure_ascii=False), encoding="utf-8")
                    args = ["--target", session["target"], "--input", str(inp), "--items", ",".join(items)]
                    if route == "/api/preview":
                        result = run_script("vuln_fix.py", args)
                        return self._json(200, result)
                    if body.get("confirmation") != "APPLY":
                        raise ValueError("explicit APPLY confirmation required")
                    # Recompute preview immediately before applying; refuse stale/unexpected plans.
                    preview = run_script("vuln_fix.py", args)
                    expected = {x for x in items}
                    if {r.get("item_id") for r in preview.get("results", [])} != expected:
                        raise ValueError("preview no longer matches selected items; review again")
                    applied = run_script("vuln_fix.py", args + ["--apply"])
                    return self._json(200, applied)
            return self._json(404, {"error": "not found"})
        except (ValueError, RuntimeError, subprocess.TimeoutExpired) as e:
            return self._json(400, {"error": str(e)})
        except Exception as e:
            self.log_error("request failed: %s", e)
            return self._json(500, {"error": "internal error"})

    def log_error(self, fmt, *args):
        sys.stderr.write("[web-ui] ERROR " + (fmt % args) + "\n")


def main():
    parser = argparse.ArgumentParser(description="Loopback-only web UI for server-security-guard")
    parser.add_argument("--host", default="127.0.0.1", help="loopback address only (default 127.0.0.1)")
    parser.add_argument("--port", type=int, default=8765)
    args = parser.parse_args()
    if args.host not in ("127.0.0.1", "localhost", "::1"):
        parser.error("security policy: bind to loopback only; do not expose this UI to a network")
    server = ThreadingHTTPServer((args.host, args.port), Handler)
    server.daemon_threads = True
    print(f"Local-only UI: http://{args.host}:{server.server_address[1]}/#{TOKEN}", flush=True)
    print("Keep this service on loopback; stop with Ctrl+C. Apply requires typing APPLY after reviewing dry-run.", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
