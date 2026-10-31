from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
import uuid
from pathlib import Path

from . import VERSION, SCHEMA, PROTOCOL
from .store import Store, MemoryError, Lock, atomic, digest, encoded, load, now, pack, record, unpack
from .transport import Notion, RemoteError


def backend_for(store):
    connection=load(store.root/".runtime/connection.json")
    if not connection: raise RemoteError("尚未连接正式云库，请先join或provision",401)
    return Notion(connection)


def new_head(store, snapshot):
    return dict(kind="team-memory-head-v3",library_id=store.meta["library_id"],schema=SCHEMA,protocol=PROTOCOL,
                min_client=VERSION,sequence=1,complete=True,snapshot=snapshot,deltas=[],updated_at=now())


def check_compatibility(store,head):
    try: Store.check_version(head)
    except MemoryError:
        atomic(store.root/".runtime/compatibility-block.json",encoded({k:head.get(k) for k in ("schema","protocol","min_client")}))
        raise
    block=store.root/".runtime/compatibility-block.json"
    if block.exists(): block.unlink()


def acknowledge(store,head):
    state=store.state(); state.update(baseline={k:r["revision"] for k,r in store.records().items()},cloud_revision=head["sequence"],
        pending=False,retry_at=None,failures=0,paused=False,error=None,last_success=now())
    state["known_paths"]=[p.relative_to(store.root).as_posix() for area in ("records","history","objects","migrations") for p in (store.root/area).rglob("*") if p.is_file()]
    store.save_state(state); atomic(store.root/".runtime/head.json",encoded(head))


def materialize(backend,head,target):
    Store.check_version(head)
    m,files=unpack(backend.get_bundle(head["snapshot"]),head["library_id"])
    if m["package_kind"]!="snapshot": raise MemoryError("云端基线不是完整快照")
    for desc in head["deltas"]:
        dm,df=unpack(backend.get_bundle(desc),head["library_id"])
        if dm["package_kind"]!="delta": raise MemoryError("云端增量链类型不一致")
        files.update(df)
    for name,raw in files.items(): atomic(Path(target)/name,raw)
    remote=Store(target)
    report=remote.doctor()
    if not report["ok"]: raise MemoryError("云端快照引用不完整: "+str(report["problems"][:5]))
    return remote


def remote_cache(store,backend,head):
    cache=store.root/".runtime/remote"
    cached=load(store.root/".runtime/cache-head.json")
    if cached==head and (cache/"library.json").exists(): return Store(cache)
    stage=Path(tempfile.mkdtemp(prefix=".remote-",dir=store.root/".runtime"))
    try:
        if cached and cached.get("snapshot")==head["snapshot"] and (cache/"library.json").exists() and head["deltas"][:len(cached.get("deltas",[]))]==cached.get("deltas",[]):
            shutil.copytree(cache,stage,dirs_exist_ok=True)
            for desc in head["deltas"][len(cached["deltas"]):]:
                _,files=unpack(backend.get_bundle(desc),store.meta["library_id"])
                for n,b in files.items(): atomic(stage/n,b)
            remote=Store(stage)
            if not remote.doctor()["ok"]: raise MemoryError("云端增量引用校验失败")
        else: remote=materialize(backend,head,stage)
        if backend.head()!=head: raise RemoteError("下载期间远端变化，保留本端并稍后重试",409,60)
        if cache.exists(): shutil.rmtree(cache)
        os.replace(stage,cache); atomic(store.root/".runtime/cache-head.json",encoded(head))
        return Store(cache)
    finally:
        if stage.exists(): shutil.rmtree(stage)


def merge_remote(store,remote,head):
    local=store.records(); incoming=remote.records(); state=store.state(); baseline=state.get("baseline",{}); installs=[]
    for area in ("objects","history","migrations"):
        for p in (remote.root/area).rglob("*"):
            if p.is_file():
                target=store.root/p.relative_to(remote.root)
                if target.exists() and area in {"objects","history"} and target.read_bytes()!=p.read_bytes(): raise MemoryError("不可变原文或历史被修改")
                if not target.exists(): atomic(target,p.read_bytes())
    for rid,rr in incoming.items():
        lr=local.get(rid); base=baseline.get(rid)
        if lr and lr["revision"]==rr["revision"]:
            if lr!=rr: raise MemoryError("同一修订内容不同，停止读取")
            baseline[rid]=rr["revision"]; continue
        if lr is None or lr["revision"]==base:
            installs.append(rr); baseline[rid]=rr["revision"]; continue
        if rr["revision"]==base: continue
        cid=str(uuid.uuid5(uuid.NAMESPACE_URL,"conflict:"+rid+":"+":".join(sorted([lr["revision"],rr["revision"]]))))
        if cid not in local and cid not in incoming:
            lh=store.add_blob(encoded(lr)); rh=store.add_blob(encoded(rr))
            installs.append(record("conflict","待确认修订："+rr["title"],"双方版本均已保留。未解决前不得据此形成确定结论。",id=cid,
                entity_ids=list(dict.fromkeys(lr["entity_ids"]+rr["entity_ids"])),status="pending",
                attributes=dict(record_id=rid,local_object=lh,remote_object=rh,base_revision=base)))
        installs.append(rr); baseline[rid]=rr["revision"]
    if installs: store.put_many(installs,dirty=False)
    state.update(baseline=baseline,cloud_revision=head["sequence"],last_checked=now())
    store.save_state(state); atomic(store.root/".runtime/head.json",encoded(head))
    if installs: store.rebuild()
    return len(installs)


def prepare(store,backend=None):
    backend=backend or backend_for(store)
    with store.lock():
        head=backend.head(); check_compatibility(store,head)
        if head["library_id"]!=store.meta["library_id"]: raise MemoryError("不同云库禁止自动合并")
        if load(store.root/".runtime/head.json")==head: return {**store.status(),"downloaded":0}
        count=merge_remote(store,remote_cache(store,backend,head),head)
        return {**store.status(),"downloaded":count}


def record_failure(store,error,clock=None):
    state=store.state(); failures=state.get("failures",0)+1
    permanent=not isinstance(error,RemoteError) or error.status in {400,401,403,404}
    delays=[60,300,900,3600]; delay=delays[min(failures-1,3)]
    if isinstance(error,RemoteError) and error.retry_after: delay=max(delay,error.retry_after)
    state.update(pending=bool(store.dirty_ids()),failures=failures,paused=permanent,
                 retry_at=None if permanent else (clock if clock is not None else time.time())+delay,error=str(error))
    store.save_state(state)


def flush(store,backend=None,retry=False):
    with store.lock():
        state=store.state(); state["batch_deadline"]=time.time(); store.save_state(state)
    try:
        backend=backend or backend_for(store)
        with store.lock():
            if store.state().get("paused") and not retry: return store.status()
            with backend.lease(store.state()["machine_id"]):
                head=backend.head(); check_compatibility(store,head)
                if head["library_id"]!=store.meta["library_id"]: raise MemoryError("云库身份不一致")
                if load(store.root/".runtime/head.json")!=head:
                    merge_remote(store,remote_cache(store,backend,head),head)
                dirty=store.dirty_ids()
                if not dirty:
                    acknowledge(store,head); return store.status()
                report=store.doctor()
                if not report["ok"]: raise MemoryError("本端引用校验失败: "+str(report["problems"][:4]))
                raw,m=pack(store,"delta",dirty,store.state().get("known_paths",[]))
                snapshot=len(head["deltas"])+1>=50 or sum(d["bytes"] for d in head["deltas"])+len(raw)>8*1024*1024
                if snapshot: raw,m=pack(store)
                cid=str(uuid.uuid5(uuid.UUID(store.meta["library_id"]),str(head["sequence"])+":"+digest(raw)))
                desc=backend.put_bundle(raw,cid,"snapshot" if snapshot else "delta")
                if backend.get_bundle(desc)!=raw: raise MemoryError("提交包回读不一致")
                newer={**head,"sequence":head["sequence"]+1,"updated_at":now(),
                       "snapshot":desc if snapshot else head["snapshot"],"deltas":[] if snapshot else head["deltas"]+[desc]}
                required=desc.get("min_client",head["min_client"])
                if tuple(map(int,required.split(".")))>tuple(map(int,head["min_client"].split("."))): newer["min_client"]=required
                backend.commit(newer,head)
                acknowledge(store,newer)
                records=store.records()
                changed={e for rid in dirty for e in records[rid]["entity_ids"]}|{rid for rid in dirty if records[rid]["kind"]=="entity"}
                atomic(store.root/".runtime/view-pending.json",encoded(sorted(changed)))
                try:
                    backend.render(store,changed)
                    state=store.state(); state.update(view_error=None,view_retry_at=None); store.save_state(state)
                except (MemoryError,OSError) as error:
                    state=store.state(); state.update(view_error=str(error),view_retry_at=time.time()+300); store.save_state(state)
                return {**store.status(),"committed":len(dirty),"view_error":store.state().get("view_error")}
    except (MemoryError,OSError) as error:
        with store.lock(): record_failure(store,error)
        return store.status()


def join(backend,target,connection=None):
    target=Path(target).expanduser().resolve()
    if target.exists() and any(target.iterdir()): raise MemoryError("join目标非空；请在已有库运行prepare，不能覆盖本端修改")
    head=backend.head()
    migrate=head.get("schema")!=SCHEMA
    if migrate:
        from .upgrade import path_for
        path_for(head.get("schema"),SCHEMA)  # Unknown formats never create a directory.
    else: Store.check_version(head)
    target.parent.mkdir(parents=True,exist_ok=True)
    stage=Path(tempfile.mkdtemp(prefix=".join-",dir=target.parent))
    try:
        if migrate:
            from .upgrade import migration_files,upgrade_library
            for desc in [head["snapshot"]]+head["deltas"]:
                for n,b in migration_files(backend.get_bundle(desc)).items(): atomic(stage/n,b)
            if load(stage/"library.json",{}).get("library_id")!=head["library_id"]: raise MemoryError("旧格式云库身份不符")
            atomic(stage/".runtime/state.json",encoded(dict(machine_id=str(uuid.uuid4()),baseline={},cloud_revision=head["sequence"],pending=True,last_activity=time.time(),retry_at=None,failures=0,paused=False)))
            if connection: atomic(stage/".runtime/connection.json",encoded(connection))
            try: upgrade_library(stage,backend=backend)
            except BaseException:
                # Conversion failures retain their staged scene and original snapshots.
                failed=stage.parent/(stage.name+".failed")
                if stage.exists(): os.replace(stage,failed)
                raise
            store=Store(stage); head=backend.head()
        else: store=materialize(backend,head,stage)
        if backend.head()!=head: raise RemoteError("接入期间云库变化，请重试",409)
        if not migrate: acknowledge(store,head)
        if connection: atomic(stage/".runtime/connection.json",encoded(connection))
        store.rebuild()
        if target.exists(): target.rmdir()
        os.replace(stage,target)
    finally:
        if stage.exists(): shutil.rmtree(stage)
    return Store(target)


def provision(store,backend,parent):
    with store.lock():
        check=store.doctor()
        if not check["ok"]: raise MemoryError("导入校验未通过，不能发布")
        root=backend.create_page(parent,"团队记忆云库",value=dict(kind="team-memory-cloud-v3",status="staging",library_id=store.meta["library_id"]))
        connection=dict(provider="notion",root_page=root,library_id=store.meta["library_id"],token_env="TEAM_MEMORY_NOTION_TOKEN")
        empty=dict(kind="team-memory-head-v3",sequence=0,complete=False)
        connection["head_pages"]=[backend.create_page(root,"系统版本头 "+str(i),value=empty) for i in range(2)]
        connection["lock_page"]=backend.create_page(root,"系统同步锁",value=dict(kind="team-memory-lease-v3",nonce=None,owner=None,expires=0))
        connection["bundles_page"]=backend.create_page(root,"来源与版本包",markdown="此目录保存不可变记忆包，请通过skill读写。")
        connection["views_page"]=backend.create_page(root,"团队记忆可读视图",markdown=store.view())
        guide=(Path(__file__).parents[2]/"references/new-device-join.md").read_text()
        guide=guide.replace("LIBRARY_ID",store.meta["library_id"]).replace("ROOT_PAGE_ID",root)
        connection["guide_page"]=backend.create_page(root,"新设备接入指南",markdown=guide)
        backend.connection=connection
        raw,m=pack(store); desc=backend.put_bundle(raw,str(uuid.uuid4()),"snapshot")
        if backend.get_bundle(desc)!=raw: raise MemoryError("初始快照云端回读失败，新库保留未启用状态")
        head=new_head(store,desc)
        for page in connection["head_pages"]: backend.cas(page,empty,head)
        control=dict(kind="team-memory-cloud-v3",status="active",schema=SCHEMA,protocol=PROTOCOL,min_client=VERSION,**connection)
        backend.cas(root,dict(kind="team-memory-cloud-v3",status="staging",library_id=store.meta["library_id"]),control)
        atomic(store.root/".runtime/connection.json",encoded(connection)); acknowledge(store,head)
        return control


def worker_tick(store,backend=None,clock=None):
    clock=time.time() if clock is None else clock
    state=store.state(); dirty=store.dirty_ids()
    if state.get("paused"): return store.status()
    if not dirty:
        if state.get("view_error") and clock>=state.get("view_retry_at",0):
            try:
                backend=backend or backend_for(store)
                with backend.lease(state["machine_id"]):
                    prepare(store,backend)
                    backend.render(store,load(store.root/".runtime/view-pending.json",[]))
                state=store.state(); state.update(view_error=None,view_retry_at=None); store.save_state(state)
            except (MemoryError,OSError) as exc:
                state=store.state(); state.update(view_error=str(exc),view_retry_at=clock+3600); store.save_state(state)
        return store.status()
    deadline=max(state.get("retry_at") or 0,state.get("batch_deadline",(state.get("last_activity") or 0)+store.meta["settings"]["idle_seconds"]))
    if clock<deadline: return store.status()
    return flush(store,backend)


def ensure_worker(store):
    if not store.dirty_ids() or not (store.root/".runtime/connection.json").exists(): return False
    log=store.root/".runtime/worker.log"
    command=[sys.executable,str(Path(__file__).parents[1]/"team-memory.py"),"--library-root",str(store.root),"worker","run"]
    with log.open("ab") as output:
        options=dict(stdin=subprocess.DEVNULL,stdout=output,stderr=output,close_fds=True)
        if os.name=="nt": options["creationflags"]=subprocess.CREATE_NEW_PROCESS_GROUP|subprocess.DETACHED_PROCESS
        else: options["start_new_session"]=True
        subprocess.Popen(command,**options)
    return True


def worker_run(store,once=False):
    try:
        with Lock(store.root.parent/("."+store.root.name+".worker.lock"),timeout=.1):
            while True:
                result=worker_tick(store)
                if once or (not store.dirty_ids() and not store.state().get("view_error")) or store.state().get("paused"): return result
                time.sleep(store.meta["settings"]["tick_seconds"])
    except MemoryError: return {**store.status(),"worker":"already-running"}
