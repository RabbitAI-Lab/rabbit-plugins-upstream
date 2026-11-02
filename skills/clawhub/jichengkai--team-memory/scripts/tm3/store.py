from __future__ import annotations

import contextlib
import hashlib
import io
import json
import os
import re
import shutil
import sqlite3
import stat
import tempfile
import time
import uuid
import zipfile
from datetime import date, datetime, timezone
from pathlib import Path, PurePosixPath

from . import VERSION, SCHEMA, PROTOCOL


class MemoryError(RuntimeError):
    pass


def now():
    return datetime.now(timezone.utc).isoformat(timespec="microseconds")


def encoded(value):
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8")


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def atomic(path, raw):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, name = tempfile.mkstemp(prefix=".write-", dir=path.parent)
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(raw)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(name, path)
    finally:
        if os.path.exists(name):
            os.unlink(name)


def load(path, default=None):
    path = Path(path)
    return json.loads(path.read_bytes()) if path.exists() else default


def safe_relative(name):
    p = PurePosixPath(name)
    if not name or "\\" in name or p.is_absolute() or any(x in {"", ".", ".."} for x in name.split("/")) or ":" in name or "\x00" in name:
        raise MemoryError("包内存在不安全路径")
    return p


class Lock:
    """An external lock survives atomic library-directory replacement."""
    def __init__(self, path, timeout=60):
        self.path, self.timeout, self.handle = Path(path), timeout, None

    def __enter__(self):
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.handle = self.path.open("a+b")
        if not self.path.stat().st_size:
            self.handle.write(b"0"); self.handle.flush()
        deadline = time.monotonic() + self.timeout
        while True:
            try:
                if os.name == "nt":
                    import msvcrt
                    self.handle.seek(0); msvcrt.locking(self.handle.fileno(), msvcrt.LK_NBLCK, 1)
                else:
                    import fcntl
                    fcntl.flock(self.handle, fcntl.LOCK_EX | fcntl.LOCK_NB)
                return self
            except (OSError, BlockingIOError):
                if time.monotonic() >= deadline:
                    self.handle.close(); raise MemoryError("本端记忆库正被其他操作使用")
                time.sleep(.05)

    def __exit__(self, *args):
        if os.name == "nt":
            import msvcrt
            self.handle.seek(0); msvcrt.locking(self.handle.fileno(), msvcrt.LK_UNLCK, 1)
        else:
            import fcntl
            fcntl.flock(self.handle, fcntl.LOCK_UN)
        self.handle.close()


KINDS = {"entity", "event", "feedback", "judgment", "task", "summary", "historical", "configuration", "source", "conflict"}
STATES = {"active", "archived", "sample", "pending", "done", "confirmed-deleted", "resolved"}


def validate_record(r):
    if not isinstance(r, dict) or r.get("kind") not in KINDS:
        raise MemoryError("未知记录类型")
    for key in ("id", "revision"):
        try:
            if str(uuid.UUID(r[key]))!=r[key]: raise ValueError()
        except (KeyError, ValueError, TypeError, AttributeError):
            raise MemoryError("记录ID和修订ID必须为UUID")
    if r.get("schema") != SCHEMA or r.get("status") not in STATES:
        raise MemoryError("记录格式或状态不受支持")
    for key in ("title", "body", "created_at", "updated_at"):
        if not isinstance(r.get(key), str):
            raise MemoryError("缺少记录字段: " + key)
    for key in ("entity_ids", "parents", "source_refs"):
        if not isinstance(r.get(key), list):
            raise MemoryError("缺少记录数组: " + key)
    for parent in r["parents"]:
        try: uuid.UUID(parent)
        except (ValueError, TypeError, AttributeError): raise MemoryError("无效父修订")
    if r["revision"] in r["parents"] or len(r["parents"])!=len(set(r["parents"])): raise MemoryError("修订关系重复或自引用")
    if not isinstance(r.get("attributes"),dict) or not isinstance(r.get("claim_kind"),str) or not isinstance(r.get("verification_status"),str): raise MemoryError("属性或证据性质无效")
    for eid in r["entity_ids"]:
        try: uuid.UUID(eid)
        except (ValueError,TypeError,AttributeError): raise MemoryError("关联对象ID无效")
    timing=r.get("time")
    if timing is not None:
        if not isinstance(timing,dict) or timing.get("precision") not in {"unknown","year","quarter","month","day","range"} or not isinstance(timing.get("original"),str): raise MemoryError("日期精度或原始表述无效")
        precision=timing["precision"]
        if precision in {"year","quarter","month"} and timing.get("value"): raise MemoryError("估算日期不能保存为精确日期")
        if precision in {"day","range"}:
            try: date.fromisoformat(timing["value"])
            except (ValueError,KeyError,TypeError): raise MemoryError("精确日期无效")
    for ref in r["source_refs"]:
        if not isinstance(ref, dict) or not isinstance(ref.get("source_id"), str):
            raise MemoryError("无效来源引用")
        if "start_line" in ref and (not isinstance(ref["start_line"], int) or ref["start_line"] < 1 or ref.get("end_line", 0) < ref["start_line"]):
            raise MemoryError("无效原文行号")
    if r.get("claim_kind") == "AI推断" and r.get("verification_status") in {"已确认", "已闭环"}:
        raise MemoryError("AI推断不能自动作为已确认事实")
    return r


def record(kind, title, body="", *, id=None, **fields):
    stamp = now()
    r = dict(schema=SCHEMA, id=id or str(uuid.uuid4()), revision=str(uuid.uuid4()), parents=[], kind=kind,
             title=title, body=body, entity_ids=[], source_refs=[], attributes={}, time=None,
             status="active", claim_kind="未标注", verification_status="未标注", created_at=stamp, updated_at=stamp)
    r.update(fields)
    return validate_record(r)


class Store:
    def __init__(self, root, create=False, library_id=None):
        self.root = Path(root).expanduser().resolve()
        self.lock_path = self.root.parent / ("." + self.root.name + ".write.lock")
        self.depth = 0
        if create and not (self.root / "library.json").exists():
            if self.root.exists() and any(self.root.iterdir()):
                raise MemoryError("目标目录非空，不能覆盖或冒充已有记忆库")
            self.root.mkdir(parents=True, exist_ok=True)
            atomic(self.root / "library.json", encoded(dict(kind="team-memory-library", schema=SCHEMA, protocol=PROTOCOL,
                library_id=library_id or str(uuid.uuid4()), min_client=VERSION, created_at=now(),
                settings=dict(idle_seconds=900, tick_seconds=60, capture="automatic", cloud_edits="agents-only"))))
            atomic(self.root/"migrations/format-3.0.json",encoded(dict(kind="format-description",schema=SCHEMA,protocol=PROTOCOL,
                encoding="UTF-8 JSON",identity="UUID record id; UUID immutable revision; parents are revisions of the same record",
                files=dict(records="records/<record-id>.json current revision",history="history/<record-id>/<revision-id>.json all revisions",
                           objects="objects/<sha256> original bytes",migrations="source mappings, format description and upgrade audit"),
                evidence="claim_kind and verification_status are preserved; AI推断 is never automatically verified",
                dates="time.precision: unknown/year/quarter/month/day/range; original expression retained; never fill missing precision",
                deleted="confirmed-deleted tombstones retain history; explicit restoration required",
                conflicts="conflict records reference both immutable variants in objects; unresolved conflicts remain visible",
                portable="package manifest verifies every file; no program, credentials, machine identity or runtime cache")))
        self.meta = load(self.root / "library.json")
        if not self.meta or self.meta.get("kind") != "team-memory-library":
            raise MemoryError("没有有效的3.0记忆库；请明确执行导入或join，不能自动创建空库")
        self.check_version(self.meta)
        with self.lock():
            self.recover()
            if not (self.root / ".runtime/state.json").exists():
                self.save_state(dict(machine_id=str(uuid.uuid4()), baseline={}, cloud_revision=0, pending=False,
                                     last_activity=None, retry_at=None, failures=0, paused=False))

    @staticmethod
    def check_version(meta):
        if meta.get("schema") != SCHEMA or meta.get("protocol") != PROTOCOL:
            raise MemoryError("记忆格式或同步协议不受支持；请升级skill，禁止旧版写入")
        try:
            newer = tuple(map(int, meta.get("min_client", VERSION).split("."))) > tuple(map(int, VERSION.split(".")))
        except (ValueError, AttributeError):
            raise MemoryError("最低客户端版本无效")
        if newer: raise MemoryError("此云库要求更新的skill，当前客户端暂停读写")

    @contextlib.contextmanager
    def lock(self):
        if self.depth:
            self.depth += 1
            try: yield
            finally: self.depth -= 1
        else:
            with Lock(self.lock_path):
                self.depth = 1
                try: yield
                finally: self.depth = 0

    def state(self): return load(self.root / ".runtime/state.json", {})
    def save_state(self, value): atomic(self.root / ".runtime/state.json", encoded(value))
    def records(self):
        return {p.stem: validate_record(load(p)) for p in sorted((self.root / "records").glob("*.json"))}

    def recover(self):
        journal = self.root / ".runtime/transaction.json"
        tx = load(journal)
        if not tx: return
        for r in tx["records"]:
            validate_record(r)
            history=self.root / "history" / r["id"] / (r["revision"] + ".json")
            if history.exists() and history.read_bytes()!=encoded(r): raise MemoryError("不可变修订内容冲突")
            atomic(history, encoded(r))
            atomic(self.root / "records" / (r["id"] + ".json"), encoded(r))
        journal.unlink()

    def put_many(self, records, dirty=True):
        with self.lock():
            compatibility=load(self.root/".runtime/compatibility-block.json")
            if compatibility:
                self.check_version(compatibility)
                (self.root/".runtime/compatibility-block.json").unlink()
            existing = self.records()
            for r in records:
                validate_record(r)
                old = existing.get(r["id"])
                if old and old["kind"]=="source" and r["attributes"].get("object_hash")!=old["attributes"].get("object_hash"):
                    raise MemoryError("原文来源不可变，更正内容需创建新来源并保留旧引用")
                if old and old["revision"] == r["revision"] and old != r:
                    raise MemoryError("同一修订号内容不一致")
            if len({r["id"] for r in records})!=len(records): raise MemoryError("同一事务存在重复记录ID")
            candidate={**existing,**{r["id"]:r for r in records}}
            check=self.doctor(candidate)
            if not check["ok"]: raise MemoryError("拒绝保存无效引用: "+str(check["problems"][:3]))
            atomic(self.root / ".runtime/transaction.json", encoded({"records":records}))
            self.recover()
            if dirty: self.checkpoint()

    def add_blob(self, raw):
        h = digest(raw); p = self.root / "objects" / h
        if p.exists() and p.read_bytes() != raw: raise MemoryError("原文对象哈希冲突")
        if not p.exists(): atomic(p, raw)
        return h

    def dirty_ids(self):
        base = self.state().get("baseline", {})
        return [k for k, r in self.records().items() if base.get(k) != r["revision"]]

    def checkpoint(self, clock=None):
        state = self.state()
        state.update(last_activity=time.time() if clock is None else clock, pending=bool(self.dirty_ids()))
        state["batch_deadline"]=state["last_activity"]+self.meta["settings"]["idle_seconds"]
        self.save_state(state)
        return self.status()

    def status(self):
        s = self.state(); dirty = self.dirty_ids()
        conflicts = [r["id"] for r in self.records().values() if r["kind"] == "conflict" and r["status"] != "resolved"]
        return dict(version=VERSION,schema=SCHEMA,protocol=PROTOCOL,library_id=self.meta["library_id"], local_saved=True, pending=len(dirty), conflicts=len(conflicts),
                    state="paused" if s.get("paused") else "retry_pending" if s.get("retry_at") else "queued" if dirty else "synced" if s.get("cloud_revision") else "local_only",
                    cloud_revision=s.get("cloud_revision", 0), last_success=s.get("last_success"),
                    due_at=s.get("batch_deadline",(s.get("last_activity") or time.time())+self.meta["settings"]["idle_seconds"]) if dirty else None,
                    retry_at=s.get("retry_at"), error=s.get("error"),view_error=s.get("view_error"))

    def doctor(self, records=None):
        check_current_history=records is None
        records = self.records() if records is None else records
        problems=[]
        for r in records.values():
            if check_current_history:
                hp=self.root/"history"/r["id"]/(r["revision"]+".json")
                if not hp.is_file() or hp.read_bytes()!=encoded(r): problems.append(r["id"]+": current revision missing or altered")
            for eid in r["entity_ids"]:
                if eid not in records or records[eid]["kind"] != "entity": problems.append(r["id"]+": invalid entity")
            for ref in r["source_refs"]:
                src = records.get(ref["source_id"])
                if not src or src["kind"] != "source": problems.append(r["id"]+": missing source"); continue
                h=src["attributes"].get("object_hash", "")
                if re.fullmatch(r"[a-f0-9]{64}",h) is None: problems.append(src["id"]+": bad object hash"); continue
                p=self.root/"objects"/h
                if not p.is_file() or digest(p.read_bytes()) != h: problems.append(src["id"]+": corrupt source"); continue
                if "end_line" in ref:
                    try:
                        if ref["end_line"] > len(p.read_bytes().decode("utf-8").splitlines()): problems.append(r["id"]+": invalid span")
                    except UnicodeError: problems.append(r["id"]+": binary source cannot have line spans")
            if r["kind"] == "source":
                h=r["attributes"].get("object_hash", "")
                if not re.fullmatch(r"[a-f0-9]{64}",h) or not (self.root/"objects"/h).is_file() or digest((self.root/"objects"/h).read_bytes()) != h:
                    problems.append(r["id"]+": corrupt source")
            for parent in r["parents"]:
                if not (self.root/"history"/r["id"]/(parent+".json")).is_file(): problems.append(r["id"]+": missing parent revision")
            if r["kind"]=="conflict":
                for key in ("local_object","remote_object"):
                    h=r["attributes"].get(key,"")
                    if not re.fullmatch(r"[a-f0-9]{64}",h) or not (self.root/"objects"/h).is_file() or digest((self.root/"objects"/h).read_bytes())!=h:
                        problems.append(r["id"]+": corrupt conflict variant")
        for path in (self.root/"objects").glob("*"):
            if not path.is_file() or path.is_symlink() or path.name!=digest(path.read_bytes()): problems.append("corrupt immutable object")
        graphs={}
        for path in (self.root/"history").glob("*/*.json"):
            try:
                historic=validate_record(load(path))
                if path.parent.name!=historic["id"] or path.stem!=historic["revision"]: raise MemoryError("history identity mismatch")
                graphs.setdefault(historic["id"],{})[historic["revision"]]=historic["parents"]
            except (MemoryError,ValueError,KeyError): problems.append("invalid historical revision: "+path.name)
        for r in records.values(): graphs.setdefault(r["id"],{})[r["revision"]]=r["parents"]
        for rid,graph in graphs.items():
            color={}
            for revision in graph:
                if color.get(revision)==2: continue
                stack=[(revision,False)]
                while stack:
                    rev,leave=stack.pop()
                    if leave: color[rev]=2; continue
                    if color.get(rev)==1: problems.append(rid+": revision cycle"); continue
                    if color.get(rev)==2: continue
                    if rev not in graph: problems.append(rid+": missing historical parent"); continue
                    color[rev]=1; stack.append((rev,True))
                    stack.extend((parent,False) for parent in graph[rev])
        return dict(ok=not problems, library_id=self.meta["library_id"], records=len(records),
                    kinds={k:sum(r["kind"]==k for r in records.values()) for k in sorted(KINDS)}, problems=problems)

    def rebuild(self):
        records=self.records(); directory=self.root/".runtime"; directory.mkdir(exist_ok=True)
        db=sqlite3.connect(directory/"index.sqlite")
        db.execute("CREATE TABLE IF NOT EXISTS records(id TEXT PRIMARY KEY,kind TEXT,title TEXT,body TEXT,status TEXT)")
        with db:
            db.execute("DELETE FROM records")
            db.executemany("INSERT INTO records VALUES(?,?,?,?,?)", [(r["id"],r["kind"],r["title"],r["body"],r["status"]) for r in records.values()])
        db.close()

    def query(self, text="", entity=None, kind=None, limit=12, include_archive=False):
        records=self.records(); conflicted={r["attributes"].get("record_id") for r in records.values() if r["kind"]=="conflict" and r["status"]!="resolved"}
        result=[]
        for r in records.values():
            if not include_archive and r["status"] in {"sample", "archived", "confirmed-deleted"}: continue
            if r["kind"] == "source" and not include_archive: continue
            if entity and entity not in r["entity_ids"] and r["id"]!=entity: continue
            if kind and r["kind"] != kind: continue
            if text and text.casefold() not in (r["title"]+"\n"+r["body"]).casefold(): continue
            result.append({**r, "body":r["body"][:1600], "body_truncated":len(r["body"])>1600, "has_conflict":r["id"] in conflicted})
        result.sort(key=lambda r:r["updated_at"], reverse=True)
        result.sort(key=lambda r:r["kind"] not in {"summary","entity","task"})
        return result[:max(1,min(limit,100))]

    def view(self, entity=None):
        all_records=self.records()
        rows=[r for r in all_records.values() if r["status"] not in {"sample","archived","confirmed-deleted"} and r["kind"] not in {"source","conflict"}
              and (entity is None or r["id"]==entity or entity in r["entity_ids"])]
        rows.sort(key=lambda r:r["updated_at"],reverse=True)
        conflicts={r["attributes"].get("record_id") for r in all_records.values() if r["kind"]=="conflict" and r["status"]!="resolved"}
        return "\n\n".join("## "+r["title"]+"\n\n"+("待确认冲突：以下为最近已发布版本，另有修订待确认。\n\n" if r["id"] in conflicts else "")+r["body"]+
            "\n\n记录ID: "+r["id"]+" | 状态: "+r["status"]+" | 性质: "+r["claim_kind"]+" | 核实: "+r["verification_status"]+
            "\n来源: "+json.dumps(r["source_refs"],ensure_ascii=False)+( "\n日期: "+json.dumps(r["time"],ensure_ascii=False) if r.get("time") else "") for r in rows)


def pack(store, kind="snapshot", ids=None, known_paths=()):
    """The same verified ZIP format is used offline and by every cloud adapter."""
    files={}; known=set(known_paths)
    selected=set(ids or [])
    for area in ("records", "history", "objects", "migrations"):
        for p in sorted((store.root/area).rglob("*")):
            if not p.is_file(): continue
            if p.is_symlink(): raise MemoryError("记忆库不能包含符号链接")
            name=p.relative_to(store.root).as_posix()
            if kind=="delta":
                if area=="records" and p.stem not in selected: continue
                if area!="records" and name in known: continue
            files[name]=p.read_bytes()
    files["library.json"]=encoded(store.meta)
    manifest=dict(kind="team-memory-package", schema=SCHEMA, protocol=PROTOCOL, package_kind=kind,
                  library_id=store.meta["library_id"], files={n:dict(sha256=digest(b),bytes=len(b)) for n,b in files.items()})
    output=io.BytesIO()
    with zipfile.ZipFile(output,"w",zipfile.ZIP_DEFLATED) as z:
        for name,raw in [("manifest.json",encoded(manifest)),*files.items()]:
            info=zipfile.ZipInfo(name,date_time=(2026,1,1,0,0,0)); info.compress_type=zipfile.ZIP_DEFLATED
            info.external_attr=0o100600<<16
            z.writestr(info,raw)
    return output.getvalue(), manifest


def unpack(raw, expected_id=None):
    try:
        with zipfile.ZipFile(io.BytesIO(raw)) as z:
            names=z.namelist()
            if len(names)!=len(set(n.casefold() for n in names)) or len(names)>100000: raise MemoryError("包内存在重复文件或文件数超限")
            for info in z.infolist():
                safe_relative(info.filename)
                mode=info.external_attr>>16
                if stat.S_ISLNK(mode) or info.file_size>256*1024*1024: raise MemoryError("拒绝链接或过大条目")
            if sum(i.file_size for i in z.infolist())>1024*1024*1024: raise MemoryError("包解压大小超限")
            m=json.loads(z.read("manifest.json")); Store.check_version(m)
            if m.get("kind")!="team-memory-package" or m.get("package_kind") not in {"snapshot","delta"}: raise MemoryError("未知记忆包")
            if expected_id and expected_id!=m["library_id"]: raise MemoryError("记忆库身份不一致")
            if set(names)!={"manifest.json",*m["files"]}: raise MemoryError("包清单覆盖不完整")
            files={}
            for n,meta in m["files"].items():
                if n!="library.json" and not n.startswith(("records/","history/","objects/","migrations/")): raise MemoryError("包内包含非记忆文件")
                b=z.read(n)
                if len(b)!=meta["bytes"] or digest(b)!=meta["sha256"]: raise MemoryError("记忆包校验失败: "+n)
                if n.startswith(("records/","history/")):
                    r=validate_record(json.loads(b)); parts=PurePosixPath(n).parts
                    if n.startswith("records/") and (len(parts)!=2 or parts[-1]!=r["id"]+".json"): raise MemoryError("记录路径与身份不一致")
                    if n.startswith("history/") and (len(parts)!=3 or parts[1]!=r["id"] or parts[-1]!=r["revision"]+".json"): raise MemoryError("历史路径与身份不一致")
                if n.startswith("objects/") and (len(PurePosixPath(n).parts)!=2 or Path(n).name!=digest(b)): raise MemoryError("原文对象名与哈希不一致")
                files[n]=b
            meta=json.loads(files["library.json"]); Store.check_version(meta)
            if meta["library_id"]!=m["library_id"]: raise MemoryError("记忆库身份与清单不一致")
            return m,files
    except (zipfile.BadZipFile, KeyError, ValueError, UnicodeError) as exc:
        raise MemoryError("记忆包损坏或格式错误") from exc


def restore(raw, target, expected_id=None):
    m,files=unpack(raw,expected_id)
    if m["package_kind"]!="snapshot": raise MemoryError("独立恢复需要完整快照")
    target=Path(target).expanduser().resolve()
    if target.exists() and any(target.iterdir()): raise MemoryError("恢复目标非空，拒绝覆盖")
    target.parent.mkdir(parents=True, exist_ok=True)
    stage=Path(tempfile.mkdtemp(prefix=".restore-",dir=target.parent))
    try:
        for n,b in files.items(): atomic(stage/n,b)
        s=Store(stage); report=s.doctor()
        if not report["ok"]: raise MemoryError("恢复校验失败: "+str(report["problems"][:5]))
        if target.exists(): target.rmdir()
        os.replace(stage,target)
    finally:
        if stage.exists(): shutil.rmtree(stage)
    result=Store(target); result.rebuild()
    return result
