#!/usr/bin/env python3
"""
Engram warm recall daemon.

Keeps the ONNX embedding model + a normalized embedding matrix resident in
memory so recall/msgctx/quick/semantic calls skip the ~5s cold-start cost
(Python interpreter + 470MB ONNX model load) that a fresh `engram.py`
invocation pays every time.

Design (in-process invocation, see step 3 in the build brief):
  engram.py is loaded fresh via importlib from its file path (not a normal
  `import engram`, since engram/ isn't a package on sys.path by default and
  another agent is actively editing the file). To actually run a subcommand
  we do NOT hand-roll an argparse.Namespace per command -- engram.py's own
  main() builds the parser and dispatches via a cmd_map, and that shape is
  the most stable part of the file across edits. So we monkeypatch sys.argv
  to `["engram.py", <cmd>, *argv]` and call the loaded module's main()
  directly, capturing stdout. This means ANY subcommand engram.py supports
  works through the daemon for free, not just the four listed in the brief.

  The actual latency win comes from a second monkeypatch: embeddings.py's
  SemanticEngine is replaced (at the `embeddings` module level, which is
  cached in sys.modules and untouched by engram.py reloads) with
  WarmSemanticEngine, which reuses a class-level ONNX session/tokenizer and
  a class-level normalized (N, 384) float32 matrix for a single matmul
  instead of a per-row Python loop. Because engram.py's cmd_recall etc. do
  `from embeddings import SemanticEngine` *inside* each function body, this
  late-binding import resolves to our warm subclass automatically -- no
  edit to engram.py needed. The matrix is refreshed only when the
  embeddings table's row count or MAX(updated_at) changes since the last
  check (cheap COUNT/MAX query), so idle requests pay ~0 reload cost.

Fallback: if in-process invocation ever throws for reasons unrelated to a
single request (i.e. the daemon itself won't start, or reload of engram.py
fails hard), the client (bq.py) detects a dead/absent socket and execs the
plain `engram.py` CLI, so correctness never depends on the daemon being up.
"""

import contextlib
import importlib.util
import io
import json
import logging
import os
import signal
import socket
import sys
import time
import traceback

ENGRAM_DIR = os.path.dirname(os.path.abspath(__file__))
WORKSPACE = os.path.dirname(ENGRAM_DIR)
ENGRAM_PATH = os.path.join(ENGRAM_DIR, "engram.py")

# Engram: load paths from config
try:
    import bpconfig
    _cfg = bpconfig.load_config()
    DB_PATH = _cfg["db_path"]
    SOCK_PATH = _cfg["socket_path"]
    PID_PATH = _cfg["pid_path"]
    LOG_PATH = os.path.join(_cfg["logs_dir"], "engram-serve.log")
except Exception:
    DB_PATH = os.path.join(ENGRAM_DIR, "engram.db")
    SOCK_PATH = "/tmp/engram-serve.sock"
    PID_PATH = "/tmp/engram-serve.pid"
    LOG_PATH = os.path.join(WORKSPACE, "logs", "engram-serve.log")

IDLE_HEARTBEAT_SECS = 6 * 3600  # dead-man's switch: log at least once per 6h even when idle

if ENGRAM_DIR not in sys.path:
    sys.path.insert(0, ENGRAM_DIR)

logger = logging.getLogger("engram-serve")
logger.setLevel(logging.INFO)


def _setup_logging():
    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
    handler = logging.FileHandler(LOG_PATH)
    handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(message)s"))
    logger.addHandler(handler)
    # line-buffer the underlying stream
    try:
        handler.stream.reconfigure(line_buffering=True)
    except Exception:
        pass


# --------------------------------------------------------------------------
# Warm semantic engine: monkeypatches embeddings.SemanticEngine in place.
# --------------------------------------------------------------------------

def install_warm_semantic_engine():
    import embeddings as embeddings_mod
    import numpy as np

    BaseEngine = embeddings_mod.SemanticEngine
    EMBED_DIM = embeddings_mod.EMBED_DIM
    _unpack_vec = embeddings_mod._unpack_vec

    class WarmSemanticEngine(BaseEngine):
        _cls_session = None
        _cls_tokenizer = None
        _matrix = None          # (N, EMBED_DIM) float32, L2-normalized
        _node_ids = None        # (N,) int64
        _matrix_rowcount = None
        _matrix_max_updated = None

        def _load_model(self):
            cls = WarmSemanticEngine
            if cls._cls_session is None or cls._cls_tokenizer is None:
                super()._load_model()
                cls._cls_session = self._session
                cls._cls_tokenizer = self._tokenizer
                logger.info("warm engine: ONNX model + tokenizer loaded (cold)")
            else:
                self._session = cls._cls_session
                self._tokenizer = cls._cls_tokenizer

        def _refresh_matrix(self):
            cls = WarmSemanticEngine
            db = self._get_db()
            try:
                row = db.execute(
                    "SELECT COUNT(*) c, MAX(updated_at) m FROM embeddings"
                ).fetchone()
            finally:
                db.close()
            cnt, maxu = row["c"], row["m"]
            if (
                cls._matrix is not None
                and cnt == cls._matrix_rowcount
                and maxu == cls._matrix_max_updated
            ):
                return
            t0 = time.time()
            db = self._get_db()
            try:
                rows = db.execute("SELECT node_id, embedding FROM embeddings").fetchall()
            finally:
                db.close()
            if rows:
                ids = np.empty(len(rows), dtype=np.int64)
                mat = np.empty((len(rows), EMBED_DIM), dtype=np.float32)
                for i, r in enumerate(rows):
                    ids[i] = r["node_id"]
                    mat[i] = _unpack_vec(r["embedding"])
            else:
                ids = np.empty(0, dtype=np.int64)
                mat = np.empty((0, EMBED_DIM), dtype=np.float32)
            cls._node_ids = ids
            cls._matrix = mat
            cls._matrix_rowcount = cnt
            cls._matrix_max_updated = maxu
            logger.info(
                "warm engine: matrix (re)loaded rows=%d in %.1fms", len(rows), (time.time() - t0) * 1000
            )

        def search(self, query, top_k=10, min_score=0.25):
            self._refresh_matrix()
            cls = WarmSemanticEngine
            if cls._matrix is None or cls._matrix.shape[0] == 0:
                return []
            query_vec = self._embed_texts([query])[0]
            scores = cls._matrix @ query_vec
            order = np.argsort(-scores)
            results = []
            for i in order:
                s = float(scores[i])
                if s < min_score:
                    break
                results.append((int(cls._node_ids[i]), s))
                if len(results) >= top_k:
                    break
            return results

    embeddings_mod.SemanticEngine = WarmSemanticEngine
    return WarmSemanticEngine


# --------------------------------------------------------------------------
# engram.py loader (import-at-runtime, tolerant of concurrent edits)
# --------------------------------------------------------------------------

class EngramLoader:
    def __init__(self):
        self._module = None
        self._mtime = None
        self.load(initial=True)

    def load(self, initial=False):
        mtime = os.path.getmtime(ENGRAM_PATH)
        if not initial and self._module is not None and mtime == self._mtime:
            return self._module
        try:
            spec = importlib.util.spec_from_file_location("engram_live", ENGRAM_PATH)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
        except Exception:
            if self._module is not None:
                logger.error(
                    "reload of engram.py failed, keeping previous module:\n%s",
                    traceback.format_exc(),
                )
                return self._module
            raise
        if self._module is None:
            logger.info("engram.py loaded (mtime=%s)", mtime)
        else:
            logger.info("engram.py reloaded (mtime changed %s -> %s)", self._mtime, mtime)
        self._module = module
        self._mtime = mtime
        return self._module

    def maybe_reload(self):
        try:
            mtime = os.path.getmtime(ENGRAM_PATH)
        except OSError as e:
            logger.error("stat engram.py failed: %s", e)
            return self._module
        if mtime != self._mtime:
            return self.load()
        return self._module


def run_cli(module, argv):
    """Run engram.py's main() in-process with the given argv, capture stdout.

    Returns (output, exit_code). Output is exactly what engram.py would have
    printed to stdout -- no extra text is injected, so bq.py can reproduce it
    byte-for-byte."""
    old_argv = sys.argv
    sys.argv = ["engram.py"] + list(argv)
    buf = io.StringIO()
    exit_code = 0
    try:
        with contextlib.redirect_stdout(buf):
            try:
                module.main()
            except SystemExit as e:
                exit_code = 0 if e.code is None else e.code
    finally:
        sys.argv = old_argv
    return buf.getvalue(), exit_code


# --------------------------------------------------------------------------
# Server
# --------------------------------------------------------------------------

_running = True


def _handle_sigterm(signum, frame):
    global _running
    _running = False


def check_stale_pidfile():
    if not os.path.exists(PID_PATH):
        return
    try:
        with open(PID_PATH) as f:
            old_pid = int(f.read().strip())
        os.kill(old_pid, 0)  # raises if process doesn't exist
        print(f"engram-serve already running (pid {old_pid}); exiting.", file=sys.stderr)
        sys.exit(1)
    except (ValueError, ProcessLookupError, PermissionError, FileNotFoundError):
        if isinstance(sys.exc_info()[1], PermissionError):
            print(f"engram-serve already running (pid held by another user?); exiting.", file=sys.stderr)
            sys.exit(1)
        os.remove(PID_PATH)


def main():
    check_stale_pidfile()
    _setup_logging()
    logger.info("engram-serve starting (pid=%d)", os.getpid())

    with open(PID_PATH, "w") as f:
        f.write(str(os.getpid()))

    signal.signal(signal.SIGTERM, _handle_sigterm)
    signal.signal(signal.SIGINT, _handle_sigterm)

    install_warm_semantic_engine()
    loader = EngramLoader()

    # Warmup: force ONNX model load + first matrix build now, off the request path.
    try:
        t0 = time.time()
        import embeddings as embeddings_mod
        warm_engine = embeddings_mod.SemanticEngine(DB_PATH)
        warm_engine.search("warmup", top_k=1)
        logger.info("warmup search complete in %.0fms", (time.time() - t0) * 1000)
    except Exception:
        logger.error("warmup failed (will retry lazily per-request):\n%s", traceback.format_exc())

    if os.path.exists(SOCK_PATH):
        os.remove(SOCK_PATH)
    srv = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    srv.bind(SOCK_PATH)
    os.chmod(SOCK_PATH, 0o600)
    srv.listen(8)
    srv.settimeout(1.0)  # so the accept loop can notice SIGTERM / idle heartbeat
    logger.info("listening on %s", SOCK_PATH)

    last_heartbeat = time.time()

    try:
        while _running:
            try:
                conn, _ = srv.accept()
            except socket.timeout:
                if time.time() - last_heartbeat > IDLE_HEARTBEAT_SECS:
                    logger.info("heartbeat: idle, daemon alive (pid=%d)", os.getpid())
                    last_heartbeat = time.time()
                continue
            except OSError:
                if not _running:
                    break
                raise

            last_heartbeat = time.time()
            with conn:
                try:
                    handle_conn(conn, loader)
                except Exception:
                    logger.error("connection handler crashed:\n%s", traceback.format_exc())
    finally:
        logger.info("shutting down (pid=%d)", os.getpid())
        try:
            srv.close()
        except Exception:
            pass
        for p in (SOCK_PATH, PID_PATH):
            try:
                os.remove(p)
            except FileNotFoundError:
                pass


def handle_conn(conn, loader):
    conn.settimeout(10.0)
    chunks = []
    while True:
        data = conn.recv(65536)
        if not data:
            break
        chunks.append(data)
        if data.endswith(b"\n") or len(data) < 65536:
            break
    raw = b"".join(chunks)
    if not raw:
        return

    t0 = time.time()
    cmd = "?"
    try:
        req = json.loads(raw.decode("utf-8"))
        cmd = req.get("cmd", "?")
        argv = req.get("argv")
        if argv is None:
            # Back-compat / spec-shaped form: {"cmd": "...", "args": {...}}
            argv = [cmd] + _args_dict_to_argv(req.get("args", {}))
        else:
            argv = [cmd] + list(argv)

        module = loader.maybe_reload()
        output, exit_code = run_cli(module, argv)
        elapsed_ms = (time.time() - t0) * 1000
        reply = {"ok": True, "output": output, "exit_code": exit_code, "elapsed_ms": elapsed_ms}
        logger.info("cmd=%s elapsed_ms=%.1f exit_code=%d", cmd, elapsed_ms, exit_code)
    except Exception:
        elapsed_ms = (time.time() - t0) * 1000
        tb = traceback.format_exc()
        logger.error("cmd=%s FAILED elapsed_ms=%.1f\n%s", cmd, elapsed_ms, tb)
        reply = {"ok": False, "output": tb, "elapsed_ms": elapsed_ms}

    try:
        conn.sendall(json.dumps(reply).encode("utf-8"))
    except BrokenPipeError:
        pass


def _args_dict_to_argv(args_dict):
    """Best-effort conversion of a {"query": "...", "budget": 5} dict into
    CLI-style argv, for callers that send the {"cmd", "args": {...}} shape
    described in the brief instead of a raw argv list."""
    argv = []
    positional = args_dict.pop("query", None) or args_dict.pop("message", None)
    if positional is not None:
        argv.append(str(positional))
    for k, v in args_dict.items():
        flag = f"--{k}"
        if isinstance(v, bool):
            if v:
                argv.append(flag)
        else:
            argv.append(flag)
            argv.append(str(v))
    return argv


if __name__ == "__main__":
    main()
