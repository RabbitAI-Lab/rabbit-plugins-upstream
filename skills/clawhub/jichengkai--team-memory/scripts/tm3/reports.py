"""Deterministic evidence views, without model calls or performance inference."""
from datetime import datetime, timezone, timedelta
from html import escape


def report_data(store,entity=None,scope="overview",period="all"):
    records=store.records()
    conflicts={r["attributes"].get("record_id") for r in records.values() if r["kind"]=="conflict" and r["status"]!="resolved"}
    rows=[r for r in records.values() if r["status"] not in {"sample","archived","confirmed-deleted"} and r["kind"] not in {"source","conflict","configuration"}
          and (not entity or r["id"]==entity or entity in r["entity_ids"])]
    if scope=="tasks": rows=[r for r in rows if r["kind"]=="task"]
    if period!="all":
        after=(datetime.now(timezone.utc)-timedelta(days=7 if period=="week" else 30)).isoformat()
        # Capture dates and event dates are deliberately not conflated.
        rows=[r for r in rows if r["updated_at"]>=after]
    rows.sort(key=lambda r:r["updated_at"],reverse=True)
    return dict(library_id=store.meta["library_id"],cloud_revision=store.state().get("cloud_revision",0),
        includes_local_pending=bool(store.dirty_ids()),scope=scope,period=period,period_basis="记录最近修订时间；不代表事件发生时间",
        counts={k:sum(r["kind"]==k for r in rows) for k in ("entity","event","feedback","judgment","task","summary","historical")},
        unresolved_conflicts=len(conflicts),records=[{**r,"has_conflict":r["id"] in conflicts} for r in rows],
        caveat="资料覆盖与记录数量不代表绩效结论。未核实反馈、管理者判断和AI推断按各自证据性质使用。")


def markdown(data):
    text="# 团队记忆证据视图\n\n库: "+data["library_id"]+" | 已提交版本: "+str(data["cloud_revision"])+" | 含本端待提交: "+str(data["includes_local_pending"])+"\n\n"+data["caveat"]+"\n\n"+data["period_basis"]
    for r in data["records"]:
        text+="\n\n## "+r["title"]+"\n\n"+("**存在未解决冲突，不能形成确定结论。**\n\n" if r["has_conflict"] else "")+r["body"]
        text+="\n\n状态: "+r["status"]+" | 性质: "+r["claim_kind"]+" | 核实: "+r["verification_status"]+" | 记录ID: "+r["id"]
        if r.get("time"): text+="\n日期（"+r["time"]["precision"]+"）: "+r["time"]["original"]
        text+="\n来源: "+", ".join(ref["source_id"]+(":"+str(ref["start_line"])+"-"+str(ref["end_line"]) if "start_line" in ref else "") for ref in r["source_refs"])
    return text+"\n"


def svg(data):
    # A4 overview intentionally summarizes, with an explicit full-evidence pointer.
    rows=data["records"][:24]
    fragments=['<svg xmlns="http://www.w3.org/2000/svg" width="210mm" height="297mm" viewBox="0 0 794 1123">',
        '<rect width="794" height="1123" fill="#f6f7f9"/>',
        '<g font-family="sans-serif" fill="#182537"><text x="38" y="55" font-size="25">团队记忆 · 证据总览</text>',
        '<text x="38" y="83" font-size="12">已提交版本 '+str(data['cloud_revision'])+' | 待确认冲突 '+str(data['unresolved_conflicts'])+'</text>',
        '<text x="38" y="108" font-size="12">'+escape(' / '.join(k+': '+str(v) for k,v in data['counts'].items()))+'</text>']
    for i,r in enumerate(rows):
        y=142+i*36
        label=('⚠ ' if r['has_conflict'] else '')+r['title'][:39]
        fragments.append(f'<text x="38" y="{y}" font-size="14">{escape(label)}</text>')
        fragments.append(f'<text x="38" y="{y+16}" font-size="10" fill="#52657a">{escape(r["kind"]+" | "+r["status"]+" | "+r["claim_kind"]+" | "+r["verification_status"])}</text>')
    fragments.extend(['<text x="38" y="1046" font-size="12">仅展示最近24条摘要；完整内容与来源请查询JSON或Markdown报告。</text>',
        '<text x="38" y="1068" font-size="12">记录数量不代表绩效。推断、反馈、判断及冲突需分别核实。</text>','</g></svg>'])
    return '\n'.join(fragments)
