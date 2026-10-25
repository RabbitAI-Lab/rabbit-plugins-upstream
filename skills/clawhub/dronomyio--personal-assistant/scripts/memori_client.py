"""Memori memory layer for the user's Temporal agents — 100% local, no cloud.

Uses Memori's open-source SDK (Apache 2.0) in BYODB mode against a local
SQLite file. What runs where:

  - Conversation + fact storage: local SQLite (~/workspace/temporal/data/memori.db)
  - Embeddings: local ONNX model (all-MiniLM-L6-v2, ~/.cache/memori-models/)
  - Semantic recall: local vector search over the fact table
  - Fact extraction: the AGENT writes its own observations as facts
    (Memori's hosted "Advanced Augmentation" does LLM-based extraction in
    their cloud — we deliberately don't use it; deterministic agents record
    exact observations instead of model-guessed facts)

No MEMORI_API_KEY, no signup, no data leaves the sandbox.

Each agent gets its own memory namespace via its entity id
("<user>/<agent>"), so the content-health agent's learnings never mix with
a future brief-writer's.

Usage (any Temporal agent):
    from memori_client import recall_memories, capture_run

    context = recall_memories("content-health", "recent incidents, flaky sources")
    ...
    capture_run("content-health",
                user_content="Run 2026-10-16 06:40: checked 5 sources.",
                assistant_content="Learnings: NSE calendar API flaky at 06:00, "
                                  "recovered on retry. No alerts fired.")
"""

from __future__ import annotations

import logging
import os
from datetime import datetime, timezone
from pathlib import Path

log = logging.getLogger(__name__)

ENTITY_ID = os.environ.get("MEMORI_ENTITY_ID", "personal-assistant-user")
DB_PATH = Path(os.environ.get("MEMORI_DB_PATH",
                              str(Path.home() / "workspace" / "temporal" / "data" / "memori.db")))

# Embedding model (quantized ONNX) — downloaded once, served from local disk.
MODEL_REPO = "Qdrant/all-MiniLM-L6-v2-onnx"
MODEL_SHA = "d13954661f83248295ba75c1ed411eef3b7b936e"
MODEL_FILES = ["config.json", "tokenizer.json", "tokenizer_config.json",
               "special_tokens_map.json", "vocab.txt", "model.onnx"]
MODEL_DIR = Path.home() / ".cache" / "memori-models" / "all-MiniLM-L6-v2-onnx"

_mem_instance = None


def _agent_entity_id(process_id: str) -> str:
    """Per-agent memory namespace."""
    return f"{ENTITY_ID}/{process_id}"


def _ensure_model_cache() -> None:
    """Seed fastembed's CWD-relative model cache from the local model dir.

    The Rust embedder resolves its model through a `.fastembed_cache`
    directory relative to the process working directory (the sandbox proxy
    breaks its TLS, so it can never download). We symlink the already
    downloaded files in. Idempotent and cheap.
    """
    if not all((MODEL_DIR / f).exists() for f in MODEL_FILES):
        log.warning("memori embedding model files missing in %s", MODEL_DIR)
        return
    root = Path.cwd() / ".fastembed_cache" / f"models--{MODEL_REPO.replace('/', '--')}"
    ref = root / "refs" / "main"
    if ref.exists():
        return
    snap = root / "snapshots" / MODEL_SHA
    snap.mkdir(parents=True, exist_ok=True)
    ref.parent.mkdir(parents=True, exist_ok=True)
    ref.write_text(MODEL_SHA)
    for f in MODEL_FILES:
        link = snap / f
        if not link.exists():
            link.symlink_to(MODEL_DIR / f)


def _mem():
    """Process-local Memori instance in BYODB (local SQLite) mode."""
    global _mem_instance
    if _mem_instance is None:
        _ensure_model_cache()
        from memori import Memori
        from sqlalchemy import create_engine
        from sqlalchemy.orm import sessionmaker

        db_path = Path(DB_PATH)
        db_path.parent.mkdir(parents=True, exist_ok=True)
        engine = create_engine(
            f"sqlite:///{db_path}", connect_args={"check_same_thread": False}
        )
        SessionLocal = sessionmaker(bind=engine)
        _mem_instance = Memori(conn=SessionLocal)  # byodb=True, cloud=False
        _mem_instance.config.storage.build()
    return _mem_instance


def _driver():
    return _mem().config.storage.driver


def recall_memories(process_id: str, query: str, limit: int = 5) -> list[str]:
    """Semantic recall over this agent's facts (local ONNX vector search)."""
    try:
        m = _mem()
        m.attribution(entity_id=_agent_entity_id(process_id),
                      process_id=process_id)
        facts = m.recall(query, limit=limit) or []
    except Exception as exc:  # noqa: BLE001 — memory must never break a run
        log.warning("memori recall failed for %s: %s", process_id, exc)
        return []
    out = []
    for f in facts:
        if isinstance(f, dict):
            text = f.get("content") or f.get("text")
        else:
            text = getattr(f, "text", None) or getattr(f, "content", None)
        out.append(text or str(f))
        if len(out) >= limit:
            break
    return out


def recall_summary(process_id: str) -> str:
    """Newest captured learnings as a short paragraph. '' when none."""
    facts = recall_memories(process_id, "learnings and outcomes", limit=5)
    return " ".join(facts)


def capture_run(
    process_id: str,
    user_content: str,
    assistant_content: str,
    session_id: str | None = None,  # accepted for API compatibility; unused locally
) -> bool:
    """Record one agent run as a fact with a local embedding.

    Stores a timestamped observation in the agent's namespace. Near-duplicate
    observations merge (num_times++) instead of duplicating.
    """
    try:
        from memori._rust_core import embed_texts as _embed_texts

        stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
        fact = f"[{stamp}] {user_content} Outcome: {assistant_content}"

        drv = _driver()
        entity_row_id = drv.entity.create(_agent_entity_id(process_id))
        embeddings = _embed_texts([fact])
        drv.entity_fact.create(entity_row_id, [fact], embeddings)
        return True
    except Exception as exc:  # noqa: BLE001 — memory must never break a run
        log.warning("memori capture failed for %s: %s", process_id, exc)
        return False
