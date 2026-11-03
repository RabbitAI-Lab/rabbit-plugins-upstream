from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
import uuid
from pathlib import Path

from . import VERSION
from .store import Store, MemoryError, atomic, digest, encoded, load, now, pack, record, restore
from .sync import backend_for, ensure_worker, flush, join, prepare, provision, record_failure, worker_run, worker_tick
from .transport import Notion

HOME=Path.home()/".team-memory"


def emit(value):
    print(json.dumps(value,ensure_ascii=False,indent=2))


def apply_record(store,data,operation_id=None,expected=None):
    current=store.records()
    rid=data.get("id") or (str(uuid.uuid5(uuid.UUID(store.meta["library_id"]),operation_id)) if operation_id else str(uuid.uuid4()))
    old=current.get(rid)
    payload_hash=digest(encoded(data))
    if old:
        if operation_id and old["attributes"].get("operation_id")==operation_id:
            if old["attributes"].get("operation_hash")!=payload_hash: raise MemoryError("同一operation_id内容变化，拒绝静默覆盖")
            return old
        if expected!=old["revision"]: raise MemoryError("修订必须提供当前expected_revision，避免覆盖另一聊天的修改")
        if old["status"]=="confirmed-deleted" and data.get("status")!="confirmed-deleted" and not data.get("attributes",{}).get("explicit_restore"):
            raise MemoryError("已确认删除的记录不能自动复活；需明确恢复流程")
        value={**old,**data,"id":rid,"created_at":old["created_at"],"updated_at":now(),
               "revision":str(uuid.uuid4()),"parents":[old["revision"]]}
    else:
        if expected: raise MemoryError("目标记录不存在，不能按旧版本修订")
        value=record(data["kind"],data["title"],data.get("body",""),id=rid)
        value.update({k:v for k,v in data.items() if k not in {"id","revision","created_at","updated_at","parents"}})
    value.setdefault("attributes",{})
    if operation_id: value["attributes"]={**value["attributes"],"operation_id":operation_id,"operation_hash":payload_hash}
    store.put_many([value])
    return value


def capture(store,data):
    """The agent supplies semantic extraction in its existing turn; no model is invoked."""
    input_id=data.get("input_id")
    if not isinstance(input_id,str) or not input_id: raise MemoryError("capture需要稳定input_id，重试使用相同值")
    text=data.get("user_text")
    if not isinstance(text,str) or not text.strip(): raise MemoryError("capture需要真实用户原话")
    sid=str(uuid.uuid5(uuid.UUID(store.meta["library_id"]),"input:"+input_id))
    with store.lock():
        h=store.add_blob(text.encode("utf-8")); current=store.records()
        if sid in current and current[sid]["attributes"].get("object_hash")!=h: raise MemoryError("同一input_id原话变化，请生成新输入或显式修订")
        if sid not in current:
            store.put_many([record("source","用户沟通 "+input_id,id=sid,status="archived",
                attributes=dict(object_hash=h,byte_length=len(text.encode("utf-8")),input_id=input_id,speaker="user"))])
        ids=[]
        for i,item in enumerate(data.get("items",[])):
            key=item.get("key")
            if not isinstance(key,str) or not key: raise MemoryError("每条拆解需提供稳定key")
            value={k:v for k,v in item.items() if k not in {"key","expected_revision","source_span"}}
            span=item.get("source_span",[1,len(text.splitlines())])
            if len(span)!=2 or not all(isinstance(n,int) for n in span) or not 1<=span[0]<=span[1]<=len(text.splitlines()): raise MemoryError("原话行号无效")
            value["source_refs"]=[dict(source_id=sid,start_line=span[0],end_line=span[1])]
            if value.get("claim_kind") in {"用户判断","AI推断"}: value["kind"]="judgment"
            if value.get("claim_kind")=="对方陈述" and value.get("verification_status") in {"已确认","已闭环"}: raise MemoryError("转述不能自动升级为已确认事实")
            ids.append(apply_record(store,value,input_id+":"+key,item.get("expected_revision"))["id"])
        for i,conclusion in enumerate(data.get("key_conclusions",[])):
            ids.append(apply_record(store,dict(kind="judgment",title="沟通关键结论",body=conclusion,
                claim_kind="AI推断",verification_status="待确认",source_refs=[dict(source_id=sid)],
                attributes=dict(speaker="assistant",input_id=input_id)),input_id+":conclusion:"+str(i))["id"])
        report=store.doctor()
        if not report["ok"]: raise MemoryError("本端已保存，但拆解引用需修复: "+str(report["problems"][:3]))
        store.rebuild()
        return dict(source_id=sid,record_ids=ids,**store.status())


def resolve_conflict(store,cid,take=None,revision=None):
    with store.lock():
        conflict=store.records().get(cid)
        if not conflict or conflict["kind"]!="conflict" or conflict["status"]=="resolved": raise MemoryError("没有待解决的冲突")
        candidates=[json.loads((store.root/"objects"/conflict["attributes"][key]).read_bytes()) for key in ("local_object","remote_object")]
        current=store.records().get(conflict["attributes"]["record_id"])
        if not current or current["revision"] not in {r["revision"] for r in candidates}: raise MemoryError("目标记录已产生后续修订，需重新核对，不能用旧冲突覆盖")
        if revision:
            chosen=next((r for r in candidates if r["revision"]==revision),None)
            if chosen is None: raise MemoryError("所选修订不属于此冲突")
        else: chosen=candidates[0 if take=="local" else 1]
        target={**chosen,"revision":str(uuid.uuid4()),"parents":[r["revision"] for r in candidates],"updated_at":now()}
        closed={**conflict,"revision":str(uuid.uuid4()),"parents":[conflict["revision"]],"status":"resolved","updated_at":now()}
        store.put_many([target,closed]); store.rebuild()
        return store.status()


def parser():
    p=argparse.ArgumentParser(description="Team Memory 3.0：独立记忆、迁移与合并同步")
    p.add_argument("--version",action="version",version=VERSION)
    p.add_argument("--library-root",type=Path)
    p.add_argument("--json",action="store_true",help="默认所有结果均为JSON")
    sub=p.add_subparsers(dest="group",required=True)
    lib=sub.add_parser("library").add_subparsers(dest="action",required=True)
    init=lib.add_parser("init"); init.add_argument("--library-id")
    legacy=lib.add_parser("import-legacy"); legacy.add_argument("--source",type=Path,required=True); legacy.add_argument("--sha256"); legacy.add_argument("--sample-policy",type=Path)
    j=lib.add_parser("join"); j.add_argument("--root-page",required=True); j.add_argument("--expected-library-id"); j.add_argument("--activate",action="store_true")
    for name in ("export","restore"):
        q=lib.add_parser(name); q.add_argument("--output" if name=="export" else "--input",type=Path,required=True)
    lib.add_parser("doctor")
    upgrade=lib.add_parser("upgrade"); upgrade.add_argument("--to",default="3.0")
    prov=lib.add_parser("provision"); prov.add_argument("--parent",required=True)
    rec=sub.add_parser("record").add_subparsers(dest="action",required=True)
    put=rec.add_parser("put"); put.add_argument("--input",type=Path,required=True); put.add_argument("--operation-id"); put.add_argument("--expected-revision"); put.add_argument("--no-worker",action="store_true")
    cap=rec.add_parser("capture"); cap.add_argument("--input",type=Path,required=True); cap.add_argument("--no-worker",action="store_true")
    query=rec.add_parser("query"); query.add_argument("--text",default=""); query.add_argument("--entity"); query.add_argument("--kind"); query.add_argument("--limit",type=int,default=12); query.add_argument("--include-archive",action="store_true")
    show=rec.add_parser("show"); show.add_argument("--id",required=True)
    source=rec.add_parser("source"); source.add_argument("--id",required=True)
    resolve=rec.add_parser("resolve"); resolve.add_argument("--conflict-id",required=True)
    choice=resolve.add_mutually_exclusive_group(required=True); choice.add_argument("--take",choices=("local","remote")); choice.add_argument("--revision")
    delete=rec.add_parser("delete"); delete.add_argument("--id",required=True); delete.add_argument("--expected-revision",required=True); delete.add_argument("--confirm",action="store_true",required=True)
    undelete=rec.add_parser("restore"); undelete.add_argument("--id",required=True); undelete.add_argument("--expected-revision",required=True); undelete.add_argument("--confirm",action="store_true",required=True)
    session=sub.add_parser("session").add_subparsers(dest="action",required=True)
    prep=session.add_parser("prepare"); prep.add_argument("--fresh",action="store_true")
    checkpoint=session.add_parser("checkpoint"); checkpoint.add_argument("--no-worker",action="store_true")
    f=session.add_parser("flush"); f.add_argument("--retry",action="store_true")
    session.add_parser("status")
    worker=sub.add_parser("worker").add_subparsers(dest="action",required=True)
    run=worker.add_parser("run"); run.add_argument("--once",action="store_true")
    report=sub.add_parser("report"); report.add_argument("--entity"); report.add_argument("--output",type=Path)
    report.add_argument("--format",choices=("markdown","json","svg"),default="markdown")
    report.add_argument("--scope",choices=("overview","tasks"),default="overview")
    report.add_argument("--period",choices=("all","week","month"),default="all")
    return p


def main(argv=None):
    args=parser().parse_args(argv)
    try:
        root=args.library_root
        if root is None:
            active=load(HOME/"active.json",{})
            root=Path(active["root"]) if active.get("root") else None
        if args.group=="library" and args.action=="import-legacy":
            from .legacy import import_legacy
            policy=load(args.sample_policy,{}) if args.sample_policy else {}
            if root is None:
                ident=policy.get("source_identity") or digest(args.source.read_bytes())
                root=HOME/"libraries"/str(uuid.uuid5(uuid.uuid5(uuid.NAMESPACE_URL,"team-memory-legacy:"+ident),"library"))
            store,report=import_legacy(args.source,root,policy,args.sha256)
            emit(dict(library_root=str(root),source_files=report["source_file_count"],new_records=report["new_records"],doctor=store.doctor()))
            return 0
        if args.group=="library" and args.action=="join":
            match=re.search(r"([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}|[0-9a-fA-F]{32})(?:[/?#]|$)",args.root_page)
            if not match: raise MemoryError("请提供正式云库页面UUID或完整链接")
            connection=dict(root_page=str(uuid.UUID(match[1])),token_env="TEAM_MEMORY_NOTION_TOKEN")
            b=Notion(connection); control=b.control()
            if control.get("schema")!="3.0":
                from .upgrade import path_for
                path_for(control.get("schema"),"3.0")
            else: Store.check_version(control)
            if args.expected_library_id and control["library_id"]!=args.expected_library_id: raise MemoryError("指定的库身份不匹配")
            connection={k:v for k,v in control.items() if k in {"root_page","library_id","head_pages","lock_page","bundles_page","views_page","guide_page","token_env"}}
            b.connection=connection
            root=root or HOME/"libraries"/control["library_id"]
            store=join(b,root,connection)
            if store.dirty_ids(): ensure_worker(store)
            if args.activate: atomic(HOME/"active.json",encoded(dict(root=str(root),library_id=store.meta["library_id"])))
            emit(dict(library_root=str(root),**store.status())); return 0
        if args.group=="library" and args.action=="restore":
            if root is None: raise MemoryError("restore需要显式--library-root空目录")
            store=restore(args.input.read_bytes(),root); emit(store.doctor()); return 0
        if args.group=="library" and args.action=="upgrade":
            if root is None: raise MemoryError("请先指定或接入记忆库")
            from .upgrade import upgrade_library
            emit(upgrade_library(root,args.to)); return 0
        if args.group=="library" and args.action=="init":
            root=root or HOME/"libraries"/str(uuid.uuid4())
            store=Store(root,create=True,library_id=args.library_id); emit(dict(library_root=str(root),**store.status())); return 0
        if root is None: raise MemoryError("未选择记忆库，请使用--library-root或library join --activate；不会自动创建空库")
        meta=load(Path(root)/"library.json",{})
        if meta.get("schema") not in {None,"3.0"}:
            from .upgrade import MIGRATIONS,upgrade_library
            if meta["schema"] in MIGRATIONS: upgrade_library(root)
        store=Store(root)
        if args.group=="library":
            if args.action=="doctor": result=store.doctor()
            elif args.action=="export":
                with store.lock():
                    check=store.doctor()
                    if not check["ok"]: raise MemoryError("记忆引用校验失败，停止导出")
                    raw,m=pack(store); atomic(args.output,raw)
                result=dict(output=str(args.output.resolve()),sha256=digest(raw),files=len(m["files"]),includes_pending=bool(store.dirty_ids()))
            elif args.action=="provision": result=provision(store,Notion({}),args.parent)
        elif args.group=="record":
            if args.action=="query": result=store.query(args.text,args.entity,args.kind,args.limit,args.include_archive)
            elif args.action=="show":
                result=store.records().get(args.id)
                if result is None: raise MemoryError("记录不存在")
                if result["kind"]=="conflict":
                    result={**result,"variants":{side:load(store.root/"objects"/result["attributes"][key]) for side,key in (("local","local_object"),("remote","remote_object"))}}
            elif args.action=="source":
                r=store.records().get(args.id)
                if not r or r["kind"]!="source": raise MemoryError("来源不存在")
                raw=(store.root/"objects"/r["attributes"]["object_hash"]).read_bytes()
                result=dict(id=r["id"],sha256=digest(raw),text=raw.decode("utf-8"))
            elif args.action=="resolve": result=resolve_conflict(store,args.conflict_id,args.take,args.revision); ensure_worker(store)
            elif args.action in {"delete","restore"}:
                with store.lock():
                    old=store.records().get(args.id)
                    if not old: raise MemoryError("记录不存在")
                    if args.action=="restore" and old["status"]!="confirmed-deleted": raise MemoryError("记录未被删除")
                    fields=dict(id=args.id,status="confirmed-deleted" if args.action=="delete" else "active")
                    if args.action=="restore": fields["attributes"]={**old["attributes"],"explicit_restore":True}
                    r=apply_record(store,fields,expected=args.expected_revision)
                result=dict(id=r["id"],**store.status()); ensure_worker(store)
            else:
                data=load(args.input)
                with store.lock():
                    if args.action=="capture": result=capture(store,data)
                    else:
                        r=apply_record(store,data,args.operation_id,args.expected_revision)
                        store.rebuild(); result=dict(id=r["id"],revision=r["revision"],**store.status())
                if not args.no_worker: result["worker_started"]=ensure_worker(store)
        elif args.group=="session":
            if args.action=="status": result=store.status()
            elif args.action=="checkpoint":
                with store.lock(): result=store.checkpoint()
                if not args.no_worker: result["worker_started"]=ensure_worker(store)
            elif args.action=="flush": result=flush(store,retry=args.retry)
            else:
                # Resume overdue batches before starting another conversation.
                status=store.status()
                if status["pending"] and status["due_at"]<=time.time() and not store.state().get("paused"): worker_tick(store)
                try: result=prepare(store)
                except MemoryError as exc:
                    result={**store.status(),"possibly_stale":True,"error":str(exc)}
        elif args.group=="worker": result=worker_run(store,args.once)
        elif args.group=="report":
            from .reports import report_data,markdown,svg
            try: prepare(store)
            except MemoryError as exc: raise MemoryError("正式材料前无法确认最新版本: "+str(exc))
            data=report_data(store,args.entity,args.scope,args.period)
            text=encoded(data).decode() if args.format=="json" else svg(data) if args.format=="svg" else markdown(data)
            if args.output: atomic(args.output,text.encode())
            result=dict(output=str(args.output) if args.output else None,format=args.format,counts=data['counts'],unresolved_conflicts=data['unresolved_conflicts'],
                        includes_local_pending=data['includes_local_pending'],cloud_revision=data['cloud_revision'])
            if not args.output: result["data" if args.format=="json" else "text"]=data if args.format=="json" else text
        emit(result)
        return 2 if isinstance(result,dict) and (result.get("ok") is False or result.get("state") in {"paused","retry_pending"}) else 0
    except (MemoryError,OSError,ValueError,KeyError,TypeError) as exc:
        emit(dict(ok=False,error=str(exc))); return 1
