#!/usr/bin/env python3
"""Primary + independent-reviewer reconstruction over dual OCR evidence.

Network is opt-in: providers come from --providers or, when omitted, from the
API keys already present in the host agent's environment (v1.5.0). Successful
batch JSON is cached for safe resume; provider rotation and split-batch
fallback avoid single-model and output-size failures.
"""
from __future__ import annotations
import argparse, concurrent.futures as cf, json, re
from pathlib import Path
from common import call_provider, extract_json, load_provider_config, normalize_persian
SYSTEM = """شما ویراستار ارشد فارسی و متخصص موضوع فایل آموزشی هستید. دو OCR مستقل از هر صفحه دارید. متن را کامل و وفادار بازسازی کنید، نه خلاصه. خطاهای OCR، املا، دستور، واژگان، تکرار، ترتیب سطر و نشانه‌گذاری را اصلاح کنید. متن نهایی فارسی معیار و مناسب راست‌به‌چپ باشد. متن انگلیسی را به فارسی روان ترجمه و نام علمی یا اصطلاح اصلی را داخل پرانتز نگه دارید. شماره صفحه، واترمارک و تزئین تکراری را حذف کنید. برای صفحه نموداری، برچسب‌ها و پیام قابل مشاهده را محتاطانه توضیح دهید. واقعیت نامطمئن اختراع نکنید. خروجی فقط JSON معتبر باشد."""

def parsed_pages(text, expected):
    data=extract_json(text)
    if not isinstance(data,list):raise ValueError('response is not a list')
    out={int(x['page']):{'title':normalize_persian(str(x.get('title',''))),
                         'text':normalize_persian(str(x.get('text','')))} for x in data}
    if set(out)!=set(expected):raise ValueError(f'page set mismatch: got {sorted(out)}, expected {expected}')
    if any(not x['text'] for x in out.values()):raise ValueError('empty reconstructed page')
    return out

def main():
    ap=argparse.ArgumentParser();ap.add_argument('evidence',type=Path);ap.add_argument('--providers',type=Path,default=None,help='optional providers.json; omit to auto-discover from environment')
    ap.add_argument('--out',type=Path,required=True);ap.add_argument('--batch',type=int,default=6)
    ap.add_argument('--proof-batch',type=int,default=12);ap.add_argument('--workers',type=int,default=3)
    a=ap.parse_args();a.out.mkdir(parents=True,exist_ok=True)
    evidence=json.loads(a.evidence.read_text('utf8'));providers=load_provider_config(a.providers)
    batches=[evidence[i:i+a.batch] for i in range(0,len(evidence),a.batch)]
    def primary(job):
        bi,items=job;cache=a.out/f'primary-{bi:04d}.json'
        if cache.exists():return json.loads(cache.read_text())
        pages=[x['page'] for x in items];blocks=[]
        for x in items:blocks.append(f"=== صفحه {x['page']} ===\nاستخراج منطقی:\n{x['logical_raw']}\n\nOCR تصویر:\n{x['ocr_raw']}")
        prompt='هر صفحه را مستقل بازسازی کن. خروجی دقیقاً [{"page":1,"title":"عنوان کوتاه","text":"متن کامل"}] باشد.\n\n'+'\n\n'.join(blocks)
        last=None
        for off in range(len(providers)):
            p=providers[(bi+off)%len(providers)]
            try:
                out=parsed_pages(call_provider(p,prompt,SYSTEM,12000),pages)
                obj={'provider':p['name'],'pages':out};cache.write_text(json.dumps(obj,ensure_ascii=False,indent=2));return obj
            except Exception as exc:last=exc
        # Honest local fallback. The later proof stage can repair it if another provider recovers.
        out={x['page']:{'title':f'صفحهٔ {x["page"]}','text':normalize_persian(x['ocr_raw'] or x['logical_raw'])} for x in items}
        obj={'provider':'local-ocr-fallback','error':type(last).__name__,'pages':out};cache.write_text(json.dumps(obj,ensure_ascii=False,indent=2));return obj
    with cf.ThreadPoolExecutor(max_workers=a.workers) as ex:prim=list(ex.map(primary,enumerate(batches)))
    merged={}
    for r in prim:merged.update({int(k):v for k,v in r['pages'].items()})
    numbers=sorted(merged);proof_sets=[numbers[i:i+a.proof_batch] for i in range(0,len(numbers),a.proof_batch)]
    def proof(job):
        bi,nums=job;cache=a.out/f'proof-{bi:04d}.json'
        if cache.exists():return json.loads(cache.read_text())
        draft=[{'page':n,**merged[n]} for n in nums]
        prompt='پیش‌نویس‌ها را نمونه‌خوانی نهایی کن؛ محتوا را حذف یا خلاصه نکن. خطای علمی آشکار، املا، دستور، نشانه‌گذاری، عنوان و بقایای OCR را اصلاح کن. همان آرایه page,title,text را برگردان:\n'+json.dumps(draft,ensure_ascii=False)
        for off in range(len(providers)):
            p=providers[(bi+1+off)%len(providers)]
            try:
                out=parsed_pages(call_provider(p,prompt,SYSTEM,15000),nums)
                obj={'provider':p['name'],'pages':out};cache.write_text(json.dumps(obj,ensure_ascii=False,indent=2));return obj
            except Exception:pass
        return {'provider':'primary-retained','pages':{n:merged[n] for n in nums}}
    with cf.ThreadPoolExecutor(max_workers=a.workers) as ex:proved=list(ex.map(proof,enumerate(proof_sets)))
    final={}
    for r in proved:final.update({int(k):v for k,v in r['pages'].items()})
    if len(final)!=len(evidence):raise SystemExit('final page count mismatch')
    (a.out/'final.json').write_text(json.dumps(final,ensure_ascii=False,indent=2),'utf8')
    report={'pages':len(final),'primary_batches':len(prim),'proof_batches':len(proved),
            'local_fallback_batches':sum(x['provider']=='local-ocr-fallback' for x in prim),
            'retained_primary_batches':sum(x['provider']=='primary-retained' for x in proved)}
    (a.out/'reasoning_report.json').write_text(json.dumps(report,indent=2),'utf8');print(json.dumps(report,indent=2))
if __name__=='__main__':main()
