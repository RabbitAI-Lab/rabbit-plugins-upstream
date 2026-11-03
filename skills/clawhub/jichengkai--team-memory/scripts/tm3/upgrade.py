"""Explicit schema migrations, staged away from the live library.

Future releases register a deterministic (target_schema, convert_directory)
step. Unknown versions are never guessed. Legacy Markdown belongs to legacy.py.
"""
from __future__ import annotations

import contextlib
import io
import json
import os
import shutil
import tempfile
import uuid
import zipfile
from pathlib import Path

from . import SCHEMA, PROTOCOL, VERSION
from .store import Store, MemoryError, Lock, atomic, encoded, digest, load, now, pack, record, safe_relative
from .transport import Notion, parse_control

MIGRATIONS = {}


def migration_files(raw):
    """Only migration code can read the envelope of a known older schema."""
    try:
        with zipfile.ZipFile(io.BytesIO(raw)) as z:
            names=z.namelist()
            if len(names)!=len(set(n.casefold() for n in names)): raise MemoryError("迁移包路径重复")
            if sum(i.file_size for i in z.infolist())>1024*1024*1024: raise MemoryError("迁移包过大")
            m=json.loads(z.read("manifest.json"))
            if set(names)!={"manifest.json",*m["files"]}: raise MemoryError("迁移包清单不完整")
            result={}
            for n,info in m["files"].items():
                safe_relative(n)
                if n!="library.json" and not n.startswith(("records/","objects/","history/","migrations/")): raise MemoryError("迁移包包含非记忆文件")
                raw=z.read(n)
                if digest(raw)!=info["sha256"] or len(raw)!=info["bytes"]: raise MemoryError("迁移包哈希错误")
                result[n]=raw
            return result
    except (KeyError,ValueError,zipfile.BadZipFile) as exc: raise MemoryError("迁移包损坏") from exc


def path_for(source,target):
    steps=[]; seen=set()
    while source!=target:
        if source in seen or source not in MIGRATIONS: raise MemoryError("没有经过验证的迁移链；请安装支持该格式的skill或执行legacy导入")
        seen.add(source); destination,fn=MIGRATIONS[source]; steps.append((source,destination,fn)); source=destination
    return steps


def convert(stage,steps,old_meta):
    original_ids={p.stem for p in (stage/"records").glob("*.json")}
    original_objects={p.name for p in (stage/"objects").glob("*") if p.is_file()}
    for source,target,fn in steps:
        fn(stage)
        meta=load(stage/"library.json"); meta.update(schema=target,protocol=PROTOCOL,min_client=VERSION)
        atomic(stage/"library.json",encoded(meta))
    result=Store(stage)
    if result.meta["library_id"]!=old_meta["library_id"] or not original_ids.issubset(result.records()):
        raise MemoryError("迁移改变库身份或遗漏记录")
    if not original_objects.issubset({p.name for p in (stage/"objects").glob("*")}):
        raise MemoryError("迁移遗漏原文对象")
    if not result.doctor()["ok"]: raise MemoryError("迁移后引用校验失败")
    return result


def upgrade_library(root,target=SCHEMA,backend=None):
    root=Path(root).expanduser().resolve(); meta=load(root/"library.json")
    if not meta or meta.get("kind")!="team-memory-library": raise MemoryError("不是可升级的独立记忆库")
    if target!=SCHEMA: raise MemoryError("此程序不能猜测未来格式，请安装对应版本skill")
    if meta["schema"]==target:
        Store.check_version(meta)
        return dict(ok=True,changed=False,schema=target,library_id=meta["library_id"])
    steps=path_for(meta["schema"],target)
    Store.check_version({**meta,"schema":SCHEMA,"protocol":PROTOCOL})
    connection=load(root/".runtime/connection.json")
    if not connection and isinstance(backend,Notion): connection=backend.connection
    backend=backend or (Notion(connection) if connection else None)
    with Lock(root.parent/("."+root.name+".write.lock")):
        # Preserve the complete original including the local queue; this is local
        # recovery state, not a portable export or a cloud credential bundle.
        history=root.parent/("."+root.name+".upgrades"); history.mkdir(exist_ok=True)
        backup=history/(str(uuid.uuid4())+".pre-upgrade")
        shutil.copytree(root,backup)
        stage=Path(tempfile.mkdtemp(prefix=".upgrade-",dir=root.parent))
        try:
            shutil.copytree(root,stage,dirs_exist_ok=True)
            local=convert(stage,steps,meta)
            rawbuf=io.BytesIO()
            with zipfile.ZipFile(rawbuf,"w",zipfile.ZIP_DEFLATED) as z:
                for p in backup.rglob("*"):
                    if p.is_file() and ".runtime" not in p.relative_to(backup).parts: z.write(p,p.relative_to(backup).as_posix())
            raw=rawbuf.getvalue(); h=local.add_blob(raw)
            local.put_many([record("source","格式升级前完整记忆快照",status="archived",
                attributes=dict(object_hash=h,byte_length=len(raw),from_schema=meta["schema"]))])
            with backend.lease(load(root/".runtime/state.json",{}).get("machine_id","upgrade")) if backend else contextlib.nullcontext():
                if backend:
                    from .sync import merge_remote
                    head=backend.head(); remote_stage=Path(tempfile.mkdtemp(prefix=".upgrade-remote-",dir=root.parent))
                    try:
                        for desc in [head["snapshot"]]+head["deltas"]:
                            for n,b in migration_files(backend.get_bundle(desc)).items(): atomic(remote_stage/n,b)
                        remote_meta=load(remote_stage/"library.json")
                        if remote_meta["library_id"]!=meta["library_id"] or head["library_id"]!=meta["library_id"]: raise MemoryError("迁移云库身份不符，禁止切换")
                        remote=convert(remote_stage,path_for(remote_meta["schema"],target),remote_meta)
                        if backend.head()!=head: raise MemoryError("升级期间云端版本改变，未切换")
                        if head["schema"]!=target:
                            # Keep the complete old cloud chain as immutable raw
                            # sources, even if the next head starts a new snapshot.
                            for desc in [head["snapshot"]]+head["deltas"]:
                                old_raw=backend.get_bundle(desc); old_hash=remote.add_blob(old_raw)
                                remote.put_many([record("source","升级前云端提交包",status="archived",attributes=dict(object_hash=old_hash,byte_length=len(old_raw),from_schema=head["schema"]))])
                            bundle,_=pack(remote)
                            desc=backend.put_bundle(bundle,str(uuid.uuid4()),"snapshot")
                            if backend.get_bundle(desc)!=bundle: raise MemoryError("新格式快照回读失败")
                            newer={**head,"schema":target,"protocol":PROTOCOL,"min_client":VERSION,"sequence":head["sequence"]+1,
                                   "snapshot":desc,"deltas":[],"updated_at":now()}
                            backend.commit(newer,head); head=newer
                        if isinstance(backend,Notion):
                            old=parse_control(backend.markdown(connection["root_page"]))
                            if old.get("schema")!=target or old.get("min_client")!=VERSION:
                                backend.cas(connection["root_page"],old,{**old,"schema":target,"protocol":PROTOCOL,"min_client":VERSION})
                        merge_remote(local,remote,head)
                    finally: shutil.rmtree(remote_stage,ignore_errors=True)
            atomic(stage/"migrations"/(str(uuid.uuid4())+".json"),encoded(dict(kind="schema-upgrade",from_schema=meta["schema"],to_schema=target,at=now(),local_snapshot_hash=h)))
            if not local.doctor()["ok"]: raise MemoryError("切换前校验失败")
            local.rebuild()
            pending=local.status()["pending"]
            old=root.parent/(".retired-"+uuid.uuid4().hex)
            os.replace(root,old)
            try: os.replace(stage,root)
            except BaseException:
                os.replace(old,root); raise
            # The already validated backup is retained; the moved old directory
            # is also retained until explicit user cleanup.
            return dict(ok=True,changed=True,schema=target,library_id=meta["library_id"],backup=str(backup),
                        retired=str(old),pending=pending)
        except BaseException as exc:
            # Preserve the failed conversion and its original backup for recovery.
            atomic(history/(stage.name+".failure.json"),encoded(dict(stage=str(stage),backup=str(backup),error=str(exc),at=now())))
            raise
