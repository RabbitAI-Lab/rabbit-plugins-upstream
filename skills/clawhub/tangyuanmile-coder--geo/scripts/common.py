"""Shared configuration, safe serialization and supported sampling contract."""
import hashlib, json, os, re, stat
from pathlib import Path

COMBINATIONS=[('DOUBA',0),('TXYB',0),('TXYBA',0),('TYQWA',0),('TYQWA',1)]
PLATFORMS={'DOUBA':'豆包','TXYB':'元宝','TXYBA':'元宝','TYQWA':'千问'}
EXPORT_CODES={'豆包手机版':'DOUBA','腾讯元宝网页版':'TXYB','腾讯元宝手机版':'TXYBA','通义千问手机版':'TYQWA','千问手机版':'TYQWA'}

def read_json(path): return json.loads(Path(path).read_text(encoding='utf-8-sig'))
def digest(value): return hashlib.sha256(json.dumps(value,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def visible(path):
    p=Path(path)
    if hasattr(os,'chflags') and hasattr(p.stat(),'st_flags'):
        os.chflags(p,p.stat().st_flags & ~stat.UF_HIDDEN)
def write_json(path,obj):
    p=Path(path);p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(obj,ensure_ascii=False,indent=2,allow_nan=False)+'\n',encoding='utf-8');visible(p)
def validate_config(c,require_targets=False):
    if c.get('input_type') not in ('brand_product','product_name'):raise ValueError('请选择商品名称或品牌＋商品名称输入方式')
    if not isinstance(c.get('name'),str) or not c['name'].strip():raise ValueError('缺少商品或类目名称')
    if c.get('name_type') not in ('category','specific_product'):raise ValueError('请确认名称属于类目还是具体商品')
    if c['input_type']=='brand_product' and not c.get('brand'):raise ValueError('品牌＋商品名模式缺少品牌')
    if c['input_type']=='product_name' and c.get('brand'):raise ValueError('无品牌模式不得预设监测品牌')
    if not re.fullmatch(r'\d{4}-\d{2}-\d{2}',c.get('date','')):raise ValueError('必须指定单日日期')
    from datetime import date
    date.fromisoformat(c['date'])
    qs=c.get('questions',[])
    if not qs or any(not all(isinstance(q.get(k),str) and q[k].strip() for k in ('id','prompt','intent')) for q in qs):raise ValueError('题库须包含题号、完整问题原文和唯一意图')
    if len({q['id'] for q in qs})!=len(qs) or len({q['prompt'] for q in qs})!=len(qs):raise ValueError('题号和问题原文不得重复')
    combos=[(x['name'],x['thinking_enabled']) for x in c.get('combinations',[])]
    if not combos or len(set(combos))!=len(combos) or any(x not in COMBINATIONS for x in combos):raise ValueError('仅支持已确认的五种平台终端模式组合，且不可重复')
    if not isinstance(c.get('repeats'),int) or isinstance(c['repeats'],bool) or c['repeats']<1:raise ValueError('每题每组合的独立重复采样次数必须是正整数')
    if require_targets and (c['input_type']=='brand_product' or c['name_type']=='specific_product'):
        if not isinstance(c.get('target_keys'),list) or not c['target_keys']:raise ValueError('请用已核验的商品归类确定目标商品集合；不得从品牌或问题补造商品')
    return c

def relative(base,path):
    p=Path(path);return p if p.is_absolute() else Path(base).parent/p
