"""One-way readers for historical layouts. Never imported by normal queries."""
from __future__ import annotations

import io
import json
import re
import tarfile
import uuid
import zipfile
from datetime import date
from pathlib import Path

from .store import MemoryError, Store, atomic, digest, encoded, record, safe_relative, now


def _read_legacy(path):
    path=Path(path); files={}
    if path.is_dir():
        for p in sorted(path.rglob("*")):
            if p.is_symlink(): raise MemoryError("旧主库含符号链接，需人工核对")
            if p.is_file() and not any(x.startswith(".") for x in p.relative_to(path).parts):
                files[p.relative_to(path).as_posix()]=p.read_bytes()
    elif zipfile.is_zipfile(path):
        with zipfile.ZipFile(path) as z:
            for item in z.infolist():
                if item.is_dir(): continue
                safe_relative(item.filename)
                if (item.external_attr>>16)&0o170000 == 0o120000 or item.file_size>256*1024*1024: raise MemoryError("拒绝归档链接或过大文件")
                if item.filename in files: raise MemoryError("旧包包含重复路径")
                files[item.filename]=z.read(item)
    else:
        try:
            with tarfile.open(path,"r:*") as t:
                for item in t:
                    if item.isdir(): continue
                    safe_relative(item.name)
                    if not item.isfile() or item.size>256*1024*1024: raise MemoryError("旧包包含链接或特殊文件")
                    if item.name in files: raise MemoryError("旧包包含重复路径")
                    files[item.name]=t.extractfile(item).read()
        except tarfile.TarError as exc: raise MemoryError("无法读取旧归档") from exc
    if not files or sum(map(len,files.values()))>1024*1024*1024: raise MemoryError("旧归档为空或超限")
    if len({n.casefold() for n in files})!=len(files): raise MemoryError("旧包路径存在大小写冲突")
    # Handle export wrappers, without interpreting program files as memories.
    data_prefix=next((n[:-len("skill-config.yaml")]+"data/" for n in files if n.endswith("skill-config.yaml") and any(k.startswith(n[:-len("skill-config.yaml")]+"data/") for k in files)),None)
    if data_prefix:
        files={n[len(data_prefix):] if n.startswith(data_prefix) else n.rsplit("/",1)[-1]:b for n,b in files.items() if n.startswith(data_prefix) or n.endswith("skill-config.yaml")}
    elif all(n.startswith("data/") for n in files): files={n[5:]:b for n,b in files.items()}
    return files


def read_legacy(path):
    try: return _read_legacy(path)
    except (EOFError,OSError,tarfile.TarError,zipfile.BadZipFile) as exc:
        raise MemoryError("旧归档损坏或读取失败，未完成导入") from exc


def event_time(text):
    m=re.search(r"(?<!\d)(20\d{2})[-年](\d{1,2})(?:[-月](\d{1,2}))?",text)
    if not m:
        year=re.search(r"(?<!\d)(20\d{2})(?:年|年度|\s|$)",text)
        quarter=re.search(r"(?<!\d)(20\d{2})[-年\s]*[Qq]([1-4])",text)
        if quarter: return dict(original=text,precision="quarter",year=int(quarter[1]),quarter=int(quarter[2]))
        return dict(original=text,precision="year",year=int(year[1])) if year else None
    y,mo=int(m[1]),int(m[2]); d=int(m[3]) if m[3] else None
    if not 1<=mo<=12: return None
    result={"original":text,"precision":"day" if d else "month","year":y,"month":mo}
    if re.search(r"年度估算|年末估算|年末估计|年终估算",text): result.update(precision="year",month=None)
    elif "季度估算" in text:
        q=re.search(r"Q([1-4])",text,re.I)
        result.update(precision="quarter",quarter=int(q[1]) if q else (mo-1)//3+1,month=None)
    elif re.search(r"月度估算|年中估算",text): result["precision"]="month" if "月度" in text else "year"
    elif d:
        try: result["value"]=date(y,mo,d).isoformat()
        except ValueError: return {"original":text,"precision":"unknown"}
        end=re.search(r"20\d{2}-\d{1,2}-\d{1,2}/(\d{1,2})",text)
        if end:
            try: result.update(precision="range",end=date(y,mo,int(end[1])).isoformat())
            except ValueError: pass
    return result


def meaningful(text):
    lines=[re.sub(r"[*_>#\-\s]","",x).strip() for x in text.splitlines()]
    return any(x and "{" not in x and x not in {"暂无","待填写","待定","未填写","无","[]"} and not x.endswith((":","：")) for x in lines)


def import_legacy(source, target, policy=None, expected_sha=None):
    source=Path(source); archive_hash=digest(source.read_bytes()) if source.is_file() else None
    if expected_sha and archive_hash!=expected_sha: raise MemoryError("旧归档SHA-256不匹配，未导入")
    files=read_legacy(source)
    policy=policy or {}; samples=set(policy.get("sample_files",[])); cutoffs=policy.get("sample_from_line",{})
    identity=policy.get("source_identity") or archive_hash or digest(encoded({p:digest(b) for p,b in files.items()}))
    ns=uuid.uuid5(uuid.NAMESPACE_URL,"team-memory-legacy:"+identity)
    uid=lambda value:str(uuid.uuid5(ns,value))
    s=Store(target,create=True,library_id=uid("library"))
    if s.meta["library_id"]!=uid("library"): raise MemoryError("目标库不是同一迁移来源，禁止自动混库")
    existing=s.records(); records=[]; report=dict(kind="legacy-import",source_identity=identity,archive_sha256=archive_hash,
        imported_at=now(),files=[], notes=["估算日期保持原精度；旧资料未标注的核实状态不补造", "示例策略仅作用于本次指定源路径和区段"])

    for name,raw in sorted(files.items()):
        safe_relative(name); h=s.add_blob(raw); srcid=uid("source:"+name); entity=None
        is_sample=name in samples
        if srcid in existing and existing[srcid]["attributes"].get("object_hash")!=h:
            raise MemoryError("同一迁移来源文件已变化；请提供新的source_identity，禁止静默跳过: "+name)
        try: text=raw.decode("utf-8")
        except UnicodeError: text=""
        lines=text.splitlines(); cutoff=int(cutoffs.get(name,len(lines)+1))
        entities=re.match(r"members/(member-\d+)-(.+)\.md$",name)
        nested=re.match(r"members/(member-[^/]+)/(profile|timeline|distill)\.md$",name)
        chinese=re.match(r"members/(.+)-(档案|时间轴|蒸馏)\.md$",name)
        if not is_sample and (entities or nested or chinese):
            legacy_id=entities[1] if entities else nested[1] if nested else None
            title=entities[2] if entities else chinese[1] if chinese else re.sub(r"^#\s*|\s*[-—].*$","",lines[0]) if lines else legacy_id
            identity_key=(legacy_id+":"+title) if entities else nested[1] if nested else "named:"+title
            identity_key=policy.get("entity_mapping",{}).get(name,identity_key)
            entity=uid("entity:"+identity_key)
            if entity not in {r["id"] for r in records} and entity not in existing:
                intro_end=next((i for i,l in enumerate(lines) if l.startswith("## ")),len(lines))
                records.append(record("entity",title,"\n".join(lines[:intro_end]).strip(),id=entity,
                    entity_ids=[], source_refs=[dict(source_id=srcid,start_line=1,end_line=max(1,intro_end))],
                    attributes=dict(entity_type="person",legacy_id=legacy_id,legacy_path=name,
                        fields={m[1]:m[2].strip() for l in lines[:intro_end] if (m:=re.match(r"\s*>?\s*\*\*(.+?)\*\*\s*[:：]\s*(.*)",l))})))
        records.append(record("source",name,id=srcid,status="sample" if is_sample else "archived",
            attributes=dict(object_hash=h,byte_length=len(raw),original_path=name,encoding="utf-8" if text else "binary",classification="sample" if is_sample else "legacy-original")))
        mapped=[srcid]+([entity] if entity else [])
        headings=[(i,len(m[1]),m[2]) for i,l in enumerate(lines) if (m:=re.match(r"^(#{1,6})\s+(.+)",l))]
        boundaries=sorted(set([0,len(lines)]+[x[0] for x in headings]+([cutoff-1] if 0<cutoff<=len(lines) else [])))
        stack=[]
        for index in range(len(boundaries)-1):
            start,end=boundaries[index],boundaries[index+1]
            segment="\n".join(lines[start:end]).strip()
            if not segment: continue
            hm=re.match(r"^(#{1,6})\s+(.+)",lines[start])
            if hm:
                level,title=len(hm[1]),hm[2]
                stack=[x for x in stack if x[0]<level]; stack.append((level,title))
            else: title=Path(name).stem
            sample=is_sample or start+1>=cutoff
            context=" / ".join(x[1] for x in stack)
            # A parent like “历史（2023-2025）” must not steal a child's date.
            timing=next((t for _,heading in reversed(stack) if (t:=event_time(heading)) is not None),None)
            body="\n".join(lines[start+1:end]).strip() if hm else segment
            if not body: continue
            metadata={m[1]:m[2].strip() for l in body.splitlines() if (m:=re.match(r"\s*\*\*(.+?)\*\*\s*[:：]\s*(.*)",l))}
            legacy_type=metadata.get("记录类型","")
            if timing and any(x in metadata.get("日期精度","") for x in ("复核","待确认","不确定")):
                timing={**timing,"uncertain":True,"note":metadata["日期精度"]}
            status="sample" if sample else "active" if meaningful(body) else "archived"
            kind="event" if timing and meaningful(body) else "historical"
            if legacy_type in {"管理判断","草稿想法"} or any(x in context for x in ("性格","管理笔记","管理策略","激励方式","沟通建议")): kind="judgment"
            rid=uid("section:"+name+":"+str(start))
            r=record(kind,title,body,id=rid,entity_ids=[entity] if entity else [],status=status,time=timing,
                source_refs=[dict(source_id=srcid,start_line=start+1,end_line=end)],
                claim_kind=("历史记录："+legacy_type) if legacy_type else "历史管理判断" if kind=="judgment" else "历史记录",
                verification_status=metadata.get("核实状态","未标注"),
                attributes=dict(legacy_path=name,legacy_heading=context,legacy_metadata=metadata,needs_review=not timing or kind=="historical"))
            records.append(r); mapped.append(rid)
            if sample: continue
            for offset,line in enumerate(lines[start:end],start+1):
                task=re.match(r"\s*[-*]\s+\[([ xX])\]\s*(.+)",line)
                if not task or not meaningful(task[2]) or "{" in task[2]: continue
                # Checklist bookkeeping and undecided alternatives remain in
                # the containing historical record, not the actionable ledger.
                if re.fullmatch(r"已记录(?:到档案)?",task[2].strip()) or task[2].lstrip().startswith("或"): continue
                tid=uid("task:"+name+":"+str(offset))
                records.append(record("task",task[2],task[2],id=tid,entity_ids=[entity] if entity else [],
                    source_refs=[dict(source_id=srcid,start_line=offset,end_line=offset)],status="done" if task[1].lower()=="x" else "active",
                    claim_kind="历史待办",attributes=dict(source_record=rid,commitment="未标注",legacy_path=name)))
                mapped.append(tid)
        if not lines:
            rid=uid("binary:"+name); records.append(record("historical",name,"历史二进制资料，见来源对象",id=rid,status="archived",source_refs=[dict(source_id=srcid)])); mapped.append(rid)
        report["files"].append(dict(path=name,bytes=len(raw),sha256=h,source_id=srcid,record_ids=list(dict.fromkeys(mapped)),classification="sample" if is_sample else "mixed" if cutoff<=len(lines) else "converted"))
    # Idempotency: never issue a new revision for already imported, identical sections.
    fresh=[]
    for r in records:
        if r["id"] in existing: continue
        fresh.append(r)
    with s.lock():
        s.put_many(fresh)
        report.update(source_file_count=len(files),new_records=len(fresh),coverage_complete=all(x["record_ids"] for x in report["files"]))
        atomic(s.root/"migrations"/(str(ns)+".json"),encoded(report))
        if source.is_file():
            h=s.add_blob(source.read_bytes())
            if uid("original-archive") not in s.records():
                s.put_many([record("source","迁移前完整归档",id=uid("original-archive"),status="archived",attributes=dict(object_hash=h,original_path=source.name,byte_length=source.stat().st_size))])
        s.rebuild()
    check=s.doctor()
    if not check["ok"]: raise MemoryError("导入完整性检查失败: "+str(check["problems"][:5]))
    return s,report
