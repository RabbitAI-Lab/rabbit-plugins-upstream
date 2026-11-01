"""Notion is an adapter, never the identity or format of a memory record."""
from __future__ import annotations

import contextlib
import io
import json
import os
import random
import re
import socket
import time
import urllib.error
import urllib.parse
import urllib.request
import uuid
import zipfile
from pathlib import Path

from . import VERSION, SCHEMA, PROTOCOL
from .store import MemoryError, Lock, atomic, digest, encoded, load

CHUNK=4*1024*1024
PART_ENCODING="zip-stored-v1"
PART_ENTRY="payload"


def zip_part(payload):
    output=io.BytesIO()
    with zipfile.ZipFile(output,"w",compression=zipfile.ZIP_STORED,allowZip64=False) as archive:
        info=zipfile.ZipInfo(PART_ENTRY,date_time=(2026,1,1,0,0,0))
        info.external_attr=0o100600<<16
        archive.writestr(info,payload)
    return output.getvalue()


PART_PAYLOAD=CHUNK-len(zip_part(b""))


def unzip_part(raw):
    try:
        with zipfile.ZipFile(io.BytesIO(raw)) as archive:
            entries=archive.infolist()
            if len(entries)!=1 or entries[0].filename!=PART_ENTRY or entries[0].compress_type!=zipfile.ZIP_STORED or entries[0].file_size>PART_PAYLOAD:
                raise MemoryError("云端ZIP分片结构无效")
            return archive.read(entries[0])
    except (zipfile.BadZipFile,ValueError,RuntimeError) as exc:
        raise MemoryError("云端ZIP分片损坏") from exc


class RemoteError(MemoryError):
    def __init__(self,message,status=None,retry_after=None):
        super().__init__(message); self.status=status; self.retry_after=retry_after


def parse_control(markdown):
    for match in re.finditer(r"```(?:json)?\s*\n(.*?)\n```",markdown,re.S):
        try:
            obj=json.loads(match[1])
            if isinstance(obj,dict) and "kind" in obj: return obj
        except ValueError: pass
    try:
        obj=json.loads(markdown)
        if isinstance(obj,dict) and "kind" in obj: return obj
    except ValueError: pass
    raise MemoryError("云端控制页不完整，未继续同步")


def control_body(value): return "```json\n"+encoded(value).decode().rstrip()+"\n```\n"


def select_head(candidates):
    valid=[c for c in candidates if c.get("kind")=="team-memory-head-v3" and c.get("snapshot") and c.get("complete") is True]
    if not valid: raise MemoryError("没有完整可用的云端头，禁止创建空库")
    seq=max(c["sequence"] for c in valid); latest=[c for c in valid if c["sequence"]==seq]
    if len({digest(encoded(c)) for c in latest})!=1: raise MemoryError("云端同序号版本头冲突")
    return latest[0]


class Notion:
    def __init__(self, connection, token=None):
        self.connection=connection
        self.token=token or os.environ.get(connection.get("token_env","TEAM_MEMORY_NOTION_TOKEN"),"")
        if not self.token: raise RemoteError("缺少Notion授权，请在本机设置凭据；不要把token写进记忆包",401)
        self.request_count=0; self.last_request=0.; self.guard=None; self.inside_guard=False; self.lease_record=None

    def wait(self,seconds):
        deadline=time.monotonic()+seconds
        while time.monotonic()<deadline:
            time.sleep(min(5,deadline-time.monotonic())); self.checkpoint()

    def checkpoint(self):
        if self.guard and not self.inside_guard:
            self.inside_guard=True
            try: self.guard()
            finally: self.inside_guard=False

    def request(self,method,path,data=None,raw=None,content_type=None,safe=False):
        if path.startswith("https://") and not path.startswith("https://api.notion.com/"):
            raise MemoryError("拒绝向其他服务发送Notion凭据")
        url=path if path.startswith("https://") else "https://api.notion.com"+path
        body=raw if raw is not None else encoded(data) if data is not None else None
        for attempt in range(6):
            self.checkpoint(); self.wait(max(0,.6-(time.monotonic()-self.last_request)))
            headers={"Authorization":"Bearer "+self.token,"Notion-Version":"2026-03-11"}
            if body is not None: headers["Content-Type"]=content_type or "application/json"
            try:
                self.request_count+=1
                with urllib.request.urlopen(urllib.request.Request(url,data=body,headers=headers,method=method),timeout=45) as response:
                    result=json.loads(response.read() or b"{}")
                self.last_request=time.monotonic(); self.checkpoint(); return result
            except urllib.error.HTTPError as exc:
                self.last_request=time.monotonic()
                try: info=json.loads(exc.read())
                except ValueError: info={}
                finally: exc.close()
                delay=exc.headers.get("Retry-After",""); delay=float(delay) if delay.isdigit() else min(2**attempt,30)
                blocked=(info.get("additional_data") or {}).get("rate_limit_reason")=="public_api_request_blocked"
                if not blocked and (exc.code in {429,529} or (safe and exc.code in {500,502,503,504})) and attempt<5:
                    self.wait(delay+random.uniform(0,.25)); continue
                if blocked: raise RemoteError("Notion已限制此连接的API权限，请处理授权后显式重试",403) from None
                raise RemoteError("Notion请求失败: "+str(exc.code)+" "+str(info.get("message","")[:160]),exc.code,delay) from None
            except (urllib.error.URLError,TimeoutError,socket.timeout):
                self.last_request=time.monotonic()
                if safe and attempt<5: self.wait(min(2**attempt,30)); continue
                raise RemoteError("Notion网络暂不可用；本端内容仍已保存",None) from None

    def markdown(self,page):
        result=self.request("GET",f"/v1/pages/{page}/markdown?markdown_version=v2",safe=True)
        if result.get("truncated") or result.get("unknown_block_ids"): raise MemoryError("云端页面被截断或有未知块")
        return result.get("markdown","")

    def control(self):
        obj=parse_control(self.markdown(self.connection["root_page"]))
        if obj.get("kind")!="team-memory-cloud-v3" or obj.get("status")!="active": raise MemoryError("此页面不是已启用的3.0云库")
        return obj

    def head(self):
        candidates=[]
        for page in self.connection["head_pages"]:
            try: candidates.append(parse_control(self.markdown(page)))
            except MemoryError as exc:
                if isinstance(exc,RemoteError) and exc.status not in {404}: raise
        result=select_head(candidates)
        if result["library_id"]!=self.connection["library_id"]: raise MemoryError("云库身份不一致")
        return result

    def cas(self,page,old,new):
        try:
            self.request("PATCH",f"/v1/pages/{page}/markdown",dict(markdown_version="v2",type="update_content",update_content=dict(content_updates=[dict(old_str=encoded(old).decode().rstrip(),new_str=encoded(new).decode().rstrip())])))
        except RemoteError as exc:
            if exc.status==400 and parse_control(self.markdown(page))!=old:
                raise RemoteError("条件更新失效，其他设备已修改控制页，稍后重新合并",409,60) from None
            raise

    @contextlib.contextmanager
    def lease(self,owner):
        page=self.connection["lock_page"]; current=parse_control(self.markdown(page))
        if current.get("nonce") and current.get("expires",0)>time.time(): raise RemoteError("云库正在提交或迁移，稍后自动重试",409,60)
        lease=dict(kind="team-memory-lease-v3",owner=owner,nonce=str(uuid.uuid4()),expires=time.time()+120)
        self.cas(page,current,lease)
        if parse_control(self.markdown(page)).get("nonce")!=lease["nonce"]: raise RemoteError("没有取得唯一云端租约",409,60)
        last=time.monotonic()
        def renew():
            nonlocal lease,last
            if time.monotonic()-last<30: return
            actual=parse_control(self.markdown(page))
            if actual.get("nonce")!=lease["nonce"]: raise RemoteError("云端租约已丢失，未提交版本头",409,60)
            updated={**lease,"expires":time.time()+120}; self.cas(page,actual,updated)
            if parse_control(self.markdown(page)).get("nonce")!=lease["nonce"]: raise RemoteError("租约续期确认失败",409,60)
            lease=updated; last=time.monotonic()
        self.guard=renew
        try: yield
        finally:
            self.guard=None
            try:
                actual=parse_control(self.markdown(page))
                if actual.get("nonce")==lease["nonce"]: self.cas(page,actual,dict(kind="team-memory-lease-v3",owner=None,nonce=None,expires=0))
            except MemoryError: pass  # Expiring lease is recoverable; never undo a committed head.

    def create_page(self,parent,title,value=None,markdown=None,files=None):
        payload=dict(parent=dict(page_id=parent),properties=dict(title=dict(title=[dict(type="text",text=dict(content=title))])))
        if files is not None or value is not None:
            children=[]
            if value is not None:
                content=encoded(value).decode(); children.append(dict(object="block",type="code",code=dict(language="json",rich_text=[dict(type="text",text=dict(content=content[i:i+1900])) for i in range(0,len(content),1900)])))
            for name,upload_id in files or []:
                children.append(dict(object="block",type="file",file=dict(type="file_upload",file_upload=dict(id=upload_id),name=name)))
            payload["children"]=children
        else: payload["markdown"]=markdown or ""
        return self.request("POST","/v1/pages",payload)["id"]

    def children(self,page):
        cursor=None; result=[]
        while True:
            query="?page_size=100"+("&start_cursor="+urllib.parse.quote(cursor) if cursor else "")
            data=self.request("GET",f"/v1/blocks/{page}/children"+query,safe=True); result.extend(data.get("results",[]))
            if not data.get("has_more"): return result
            cursor=data.get("next_cursor")
            if not cursor: raise MemoryError("附件分页不完整")

    def put_bundle(self,raw,commit_id,kind):
        if not zipfile.is_zipfile(io.BytesIO(raw)): raise MemoryError("提交包必须为有效ZIP，拒绝只改扩展名")
        uploads=[]; hashes=[]
        fragmented=len(raw)>CHUNK
        step=PART_PAYLOAD if fragmented else CHUNK
        for index,start in enumerate(range(0,len(raw),step)):
            payload=raw[start:start+step]; chunk=zip_part(payload) if fragmented else payload
            if len(chunk)>CHUNK: raise MemoryError("ZIP分片超过4MiB附件上限")
            name=f"{commit_id}.part-{index:04d}.zip"; hashes.append(digest(chunk))
            upload=self.request("POST","/v1/file_uploads",dict(mode="single_part",filename=name,content_type="application/zip"))
            boundary="tmemory"+uuid.uuid4().hex
            body=(f'--{boundary}\r\nContent-Disposition: form-data; name="file"; filename="{name}"\r\nContent-Type: application/zip\r\n\r\n').encode()+chunk+f"\r\n--{boundary}--\r\n".encode()
            self.request("POST",f"/v1/file_uploads/{upload['id']}/send",raw=body,content_type="multipart/form-data; boundary="+boundary)
            uploads.append((name,upload["id"]))
        desc=dict(commit_id=commit_id,sha256=digest(raw),bytes=len(raw),parts=hashes,package_kind=kind)
        if fragmented: desc.update(part_encoding=PART_ENCODING,min_client="3.0.1")
        page=self.create_page(self.connection["bundles_page"],commit_id,value={"kind":"team-memory-bundle-v3",**desc},files=uploads)
        return {**desc,"page_id":page}

    def get_bundle(self,descriptor):
        encoding=descriptor.get("part_encoding","raw")
        if encoding not in {"raw",PART_ENCODING}: raise MemoryError("未知云端分片编码，请升级程序")
        chunks=[]
        files=[b["file"] for b in self.children(descriptor["page_id"]) if b.get("type")=="file"]
        if len(files)!=len(descriptor["parts"]): raise MemoryError("云端记忆分片不完整")
        for index,f in enumerate(files):
            url=(f.get("file") or {}).get("url")
            if not url or not url.startswith("https://"): raise MemoryError("附件不是有效托管文件")
            self.checkpoint()
            try:
                with urllib.request.urlopen(url,timeout=45) as response: raw=response.read(CHUNK+1)
            except (urllib.error.URLError,TimeoutError): raise RemoteError("附件下载失败，稍后重新取得临时地址") from None
            if len(raw)>CHUNK or digest(raw)!=descriptor["parts"][index]: raise MemoryError("云端分片校验失败")
            chunks.append(unzip_part(raw) if encoding==PART_ENCODING else raw)
        raw=b"".join(chunks)
        if len(raw)!=descriptor["bytes"] or digest(raw)!=descriptor["sha256"]: raise MemoryError("云端提交包校验失败")
        return raw

    def commit(self,head,expected):
        self.checkpoint()
        actual=self.head()
        if actual["sequence"]!=expected["sequence"] or digest(encoded(actual))!=digest(encoded(expected)):
            raise RemoteError("远端版本已改变，未覆盖，等待重新合并",409,60)
        target=self.connection["head_pages"][head["sequence"]%2]
        old=parse_control(self.markdown(target)); self.cas(target,old,head)
        if digest(encoded(self.head()))!=digest(encoded(head)): raise RemoteError("版本头提交待确认，请重试核对",409,60)

    def render(self,store,changed_entities):
        # Only derived pages for affected people and the small overview change.
        page=self.connection.get("views_page")
        if not page: return
        pages={b.get("child_page",{}).get("title"):b["id"] for b in self.children(page) if b.get("type")=="child_page"}
        records=store.records()
        for key in sorted(set(changed_entities)|{"overview"}):
            if key=="overview":
                title="总览 [overview]"
                active=[r for r in records.values() if r["status"] not in {"sample","archived","confirmed-deleted"}]
                content="本页由正式JSON记录生成；详细资料见人物页，通过skill查询及追溯原文。\n\n"+"\n".join(
                    "- "+k+": "+str(sum(r["kind"]==k for r in active)) for k in ("entity","event","task","judgment","conflict"))
                content+="\n\n"+"\n".join("- "+r["title"]+" | "+r["id"] for r in active if r["kind"]=="entity")
                content+="\n\n## 团队公共资料\n\n"+"\n\n".join("### "+r["title"]+"\n\n"+r["body"] for r in active if not r["entity_ids"] and r["kind"] not in {"entity","conflict"})
            else:
                entity=records.get(key)
                if not entity or entity["kind"]!="entity": continue
                title=entity["title"]+" ["+key+"]"; content=store.view(key)
            if len(content)>70000: content=content[:68000]+"\n\n本页仅展示前68000字符；完整记录、历史与原文均在正式记忆包中，请通过skill按需查询。"
            if title in pages:
                self.request("PATCH",f"/v1/pages/{pages[title]}/markdown",dict(markdown_version="v2",type="replace_content",replace_content=dict(new_str=content)),safe=True)
            else: self.create_page(page,title,markdown=content)


class DirectoryBackend:
    """Deterministic adapter for tests and offline round-trip verification, not a NAS service."""
    def __init__(self,root): self.root=Path(root); self.calls=0
    def head(self):
        self.calls+=1
        return select_head([load(self.root/f"head-{i}.json",{}) for i in (0,1)])
    @contextlib.contextmanager
    def lease(self,owner):
        with Lock(self.root/"lease.lock",timeout=.2): yield
    def put_bundle(self,raw,commit_id,kind):
        atomic(self.root/"bundles"/(commit_id+".zip"),raw)
        return dict(commit_id=commit_id,sha256=digest(raw),bytes=len(raw),parts=[digest(raw)],package_kind=kind)
    def get_bundle(self,desc):
        self.calls+=1; raw=(self.root/"bundles"/(desc["commit_id"]+".zip")).read_bytes()
        if digest(raw)!=desc["sha256"] or len(raw)!=desc["bytes"]: raise MemoryError("测试后端包校验失败")
        return raw
    def commit(self,head,expected):
        if self.head()!=expected: raise RemoteError("远端版本冲突",409)
        atomic(self.root/f"head-{head['sequence']%2}.json",encoded(head))
    def render(self,store,changed_entities): atomic(self.root/"view.md",store.view().encode())
