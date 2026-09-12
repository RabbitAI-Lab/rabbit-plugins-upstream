import copy,json,sys,tempfile,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from common import *
from intake import extract,normalize
from analyze import build,matches
from render_report import render
from validate_report import validate
from task_plan import plan,approve,begin,record

def widget(kind,items):return 'render_ecom_card_widget_'+kind+'_start:'+json.dumps(items,ensure_ascii=False)+'render_ecom_card_widget_'+kind+'_end:'
def fixture():
    c={'input_type':'brand_product','name_type':'specific_product','name':'星河洁面乳','brand':'青禾','date':'2026-08-13','repeats':1,'is_demo':True,'questions':[{'id':'Q01','prompt':'温和洁面乳有哪些？','intent':'温和清洁'},{'id':'Q02','prompt':'预算百元的洁面乳推荐？','intent':'预算选择'}],'combinations':[{'name':n,'thinking_enabled':m} for n,m in COMBINATIONS],'target_keys':['qinghe-star'],'body_product':{'aliases':['星河洁面乳']}}
    tax={'brands':[{'name':'青禾','aliases':['青禾'],'basis':'样例品牌'},{'name':'云朵','aliases':['云朵'],'basis':'样例品牌'}],'products':[{'key':'qinghe-star','name':'青禾星河洁面乳','brand':'青禾','resolved':True},{'key':'cloud-mild','name':'云朵轻柔洁面乳','brand':'云朵','resolved':True}], 'cards':{}}
    rs=[]
    for i,(q,combo) in enumerate((q,combo) for q in c['questions'] for combo in c['combinations']):
        body=['青禾星河洁面乳可以参考。','青禾还有别的选择。','星河洁面乳可以参考。','可以按需求选购。','青禾星河洁面乳可以参考。'][i%5]
        kind='product' if combo['name']=='DOUBA' else 'jd' if combo['name'].startswith('TXYB') else 'taobao'
        f={'product':('pid','text','seller_name'),'jd':('sku','sku_name','shop_name'),'taobao':('item_id','title','shop_name')}[kind]
        items=[]
        for ident,k,title,b,price in [('A','qinghe-star','青禾星河洁面乳','青禾','39.90'),('B','cloud-mild','云朵轻柔洁面乳','云朵',None)]:
            if i in (1,4,6,9):continue
            card={f[0]:ident,f[1]:title,f[2]:b+'样例店','price':price};items.append(card)
            tax['cards'][kind+':'+ident]={'product_key':k,'evidence_title':title,'basis':'合成样例同ID同明确系列'}
        if i==0:items.append(items[0].copy())
        rs.append({'reqId':f'example-{i}','name':combo['name'],'thinking_enabled':combo['thinking_enabled'],'created_at':c['date'],'prompt':q['prompt'],'content':body+(widget(kind,items) if items else '')})
    return c,tax,rs

def data(c=None,tax=None,rs=None):
    cc,tt,rr=fixture();c=copy.deepcopy(c or cc);tax=copy.deepcopy(tax or tt);rs=copy.deepcopy(rs or rr)
    with tempfile.TemporaryDirectory() as d:
        p=Path(d);(p/'raw.jsonl').write_text('\n'.join(json.dumps(r,ensure_ascii=False) for r in rs));c['sources']=[{'path':'raw.jsonl'}]
        raw=normalize(c,p/'config.json');return raw,tax

class Regression(unittest.TestCase):
    def test_full_pipeline(self):
        raw,t=data();m=build(raw,t);self.assertEqual(m['overall']['answers'],10);self.assertEqual(m['overall']['events'],12);self.assertEqual(m['overall']['target']['events'],6);self.assertEqual(validate(m,render(m))['status'],'PASS')
    def test_card_only_does_not_backfill_body(self):
        body,cards,_=extract('仅按需求选择。'+widget('jd',[{'sku':'1','sku_name':'青禾星河洁面乳'}]));self.assertNotIn('青禾',body);self.assertEqual(len(cards),1)
    def test_only_product_body(self):
        raw,t=data();m=build(raw,t);x=m['ledger'][2];self.assertFalse(x['body_brands']);self.assertTrue(x['body_target']);self.assertTrue(x['cards'])
    def test_no_body_with_card_is_valid(self):
        raw,t=data();m=build(raw,t);self.assertEqual(sum(x['count'] for x in m['overall']['states8'] if not x['brand'] and not x['product'] and x['card']),2)
    def test_no_card_answers_in_denominator(self):
        raw,t=data();m=build(raw,t);self.assertEqual(m['overall']['target']['coverage'],.6)
    def test_first_card_denominator_is_any_card_answers(self):
        raw,t=data();m=build(raw,t);self.assertEqual(m['overall']['target']['first_rate'],1)
    def test_duplicate_cards(self):
        x={'sku':'1','sku_name':'A'};_,cs,_=extract(widget('jd',[x,x,{'sku':'2','sku_name':'A'}]));self.assertEqual([x['position'] for x in cs],[1,2])
    def test_multiple_cards_same_product_count_events(self):
        raw,t=data();card=copy.deepcopy(raw['answers'][0]['cards'][0]);card['identity']='jd:new';card['position']=3;raw['answers'][0]['cards'].append(card);t['cards'][card['identity']]={'product_key':'qinghe-star','evidence_title':card['title'],'basis':'样例明确系列'};m=build(raw,t);self.assertEqual(m['overall']['target']['events'],7);self.assertEqual(m['overall']['target']['card_answers'],6)
    def test_non_product_cards_removed(self):
        text,cs,ig=extract('普通文本'+widget('miniprogram',[{'title':'青禾'}]));self.assertNotIn('青禾',text);self.assertEqual(cs,[]);self.assertEqual(ig['miniprogram'],1)
    def test_malformed_marker_fails(self):
        with self.assertRaises(ValueError):extract('render_ecom_card_widget_jd_start:[notjson]')
    def test_quote_and_url_do_not_add_brand(self):
        s,_,_=extract('常见商品 https://example.org/青禾');self.assertNotIn('青禾',s)
    def test_unbranded_category(self):
        c,t,r=fixture();c.update(input_type='product_name',name_type='category',name='洁面乳',brand=None,target_keys=[]);raw,t=data(c,t,r);m=build(raw,t);h=render(m);self.assertEqual(len(m['overall']['products']),2);self.assertNotIn('id="states8"',h);self.assertEqual(validate(m,h)['status'],'PASS')
    def test_unbranded_specific_keeps_brands_separate(self):
        c,t,r=fixture();c.update(input_type='product_name',brand=None);raw,t=data(c,t,r);m=build(raw,t);self.assertEqual(m['overall']['target']['takeup'],None);self.assertEqual(validate(m,render(m))['status'],'PASS')
    def test_brand_category_targets_do_not_leak(self):
        c,t,r=fixture();c.update(name_type='category',name='洁面乳',target_keys=['qinghe-star','cloud-mild']);raw,t=data(c,t,r)
        with self.assertRaises(ValueError):build(raw,t)
    def test_missing_target_zero_rank(self):
        raw,t=data();t['products'].append({'key':'absent','name':'青禾另一款','brand':'青禾','resolved':True});raw['config']['target_keys']=['absent'];m=build(raw,t);self.assertEqual(m['target_products'][0]['events'],0);self.assertIsNone(m['target_products'][0]['rank']);self.assertIsNone(m['target_products'][0]['mean_position']);self.assertIn('未出卡',render(m))
    def test_unsupported_combination_not_counted(self):
        c,t,r=fixture();x=copy.deepcopy(r[0]);x.update(name='DB',reqId='unsupported');r.append(x);raw,t=data(c,t,r);self.assertEqual(len(raw['answers']),10)
    def test_partial_sampling_is_disclosed(self):
        c,t,r=fixture();r.pop();raw,t=data(c,t,r);self.assertFalse(raw['audit']['complete']);self.assertIn('部分采样数量与计划不一致',render(build(raw,t)))
    def test_mapping_requires_observed_evidence(self):
        raw,t=data();next(iter(t['cards'].values()))['evidence_title']='not observed'
        with self.assertRaises(ValueError):build(raw,t)
    def test_unknown_ids_not_merged(self):
        raw,t=data();t['cards']={};m=build(raw,t);self.assertEqual(len(m['overall']['products']),6)
    def test_missing_and_nonnumeric_price_not_zero(self):
        _,cs,_=extract(widget('jd',[{'sku':'1','sku_name':'A','price':'起价20'},{'sku':'2','sku_name':'B','price':0}]));self.assertIsNone(cs[0]['price']);self.assertEqual(cs[1]['price'],0)
    def test_cross_source_same_id_not_deduped(self):
        _,cs,_=extract(widget('jd',[{'sku':'1','sku_name':'A'}])+widget('taobao',[{'item_id':'1','title':'A'}]));self.assertEqual(len(cs),2)
    def test_html_escaping(self):
        raw,t=data();raw['config']['name']='<script>alert(1)</script>';h=render(build(raw,t));self.assertNotIn('<script>',h);self.assertIn('&lt;script&gt;',h)
    def test_overlapping_exports_use_original_request_id(self):
        c,t,r=fixture();x=copy.deepcopy(r[0]);x.pop('reqId');x['req_info']={'req_id':'original-request'};r[0]=x;r.append(copy.deepcopy(x));raw,t=data(c,t,r);self.assertEqual(len(raw['answers']),10);self.assertEqual(raw['audit']['excluded']['重复导入同一回答'],1)
    def test_all_zero_cards(self):
        c,t,r=fixture()
        for x in r:x['content']='青禾星河洁面乳可以参考。'
        raw,t=data(c,t,r);t['cards']={};m=build(raw,t);self.assertEqual(m['overall']['events'],0);self.assertIsNone(m['overall']['target']['sov']);self.assertIsNone(m['overall']['target']['first_rate']);self.assertEqual(validate(m,render(m))['status'],'PASS')
    def test_unknown_brand_remains_in_sov_denominator(self):
        raw,t=data();x=raw['answers'][0]['cards'][0];x['title']='无法识别的商品';t['cards'].pop(x['identity']);m=build(raw,t);self.assertEqual(m['overall']['events'],12);self.assertEqual(sum(p['events'] for p in m['overall']['products']),12)
    def test_mode_string_and_conflict(self):
        c,t,r=fixture()
        for x in r:x['thinking_enabled']=str(x['thinking_enabled'])
        raw,t=data(c,t,r);self.assertEqual(len(raw['answers']),10)
    def test_html_after_edit_does_not_pass_binding(self):
        raw,t=data();m=build(raw,t);h=render(m).replace('含商品卡回答6条','含商品卡回答999条')
        with self.assertRaises(ValueError):validate(m,h)
    def test_plan_exact_five_combinations(self):
        c,_,_=fixture();p=plan(c);self.assertEqual(len(p['tasks']),10);self.assertEqual(p['tasks'][0]['api_body']['prompt'],c['questions'][0]['prompt']);self.assertIn('thinkingEnabled',p['tasks'][0]['mcp_arguments'])
    def test_no_paid_request_without_approval(self):
        p=plan(fixture()[0]);self.assertEqual(p['total_points'],'9.2')
        with self.assertRaises(ValueError):begin(p,'T00001')
    def test_unknown_submission_never_retried(self):
        c,_,_=fixture();q={'source':'合成测试价格','checked_at':'2026-08-13','prices':{n+':'+str(m):'1' for n,m in COMBINATIONS}};p=plan(c,q);approve(p,p['plan_hash'],'确认执行');begin(p,'T00001');record(p,'T00001',None)
        with self.assertRaises(ValueError):begin(p,'T00001')
        with self.assertRaises(ValueError):begin(p,'T00002')
    def test_changed_parameters_invalidate_approval(self):
        c,_,_=fixture();q={'source':'合成测试价格','checked_at':'2026-08-13','prices':{n+':'+str(m):'1' for n,m in COMBINATIONS}};p=plan(c,q);approve(p,p['plan_hash'],'确认执行');p['tasks'][0]['api_body']['prompt']='另一问题'
        with self.assertRaises(ValueError):begin(p,'T00001')
if __name__=='__main__':unittest.main()
