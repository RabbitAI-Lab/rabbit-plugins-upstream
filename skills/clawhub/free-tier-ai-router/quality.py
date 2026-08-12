#!/usr/bin/env python3
"""Score candidate models on 5 objectively-checkable questions.
Quality must be MEASURED, not assumed from model names."""
import json, os, subprocess, sys, time
from concurrent.futures import ThreadPoolExecutor

def creds(p): return json.load(open(os.path.expanduser(f'~/.config/{p}/credentials.json')))

TESTS = [
    ("Is 91 a prime number? Answer with just yes or no.", lambda s: 'no' in s.lower()[:40]),
    ("A bat and ball cost $1.10. The bat costs $1.00 more than the ball. How many cents is the ball? Answer with just the number.",
     lambda s: '5' in s and '10' not in s.replace('1.10','').replace('1.00','')),
    ("How many letter r's are in 'strawberry'? Answer with just the number.", lambda s: '3' in s),
    ("Which is larger, 9.11 or 9.9? Answer with just the number.", lambda s: '9.9' in s and '9.11' not in s.split('9.9')[0]),
    ("Complete with one word only: The capital of Australia is", lambda s: 'canberra' in s.lower()),
]

CANDIDATES = [
 ('gemini','gemini-3.6-flash'),('gemini','gemini-3.5-flash'),('gemini','gemini-3.5-flash-lite'),
 ('gemini','gemini-flash-latest'),('gemini','gemini-3-flash-preview'),('gemini','gemini-3.1-flash-lite'),
 ('mistral','mistral-large-latest'),('mistral','mistral-medium-latest'),('mistral','mistral-small-latest'),
 ('mistral','ministral-8b-latest'),('mistral','ministral-3b-latest'),('mistral','magistral-medium-latest'),
 ('mistral','codestral-latest'),('mistral','open-mistral-nemo'),('mistral','mistral-tiny-latest'),
 ('openrouter','nvidia/nemotron-3-ultra-550b-a55b:free'),('openrouter','nvidia/nemotron-3-super-120b-a12b:free'),
 ('openrouter','inclusionai/ling-3.0-flash:free'),('openrouter','openai/gpt-oss-20b:free'),
 ('openrouter','nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free'),('openrouter','poolside/laguna-s-2.1:free'),
 ('kilo','kilo-auto/free'),('kilo','nvidia/nemotron-3-ultra-550b-a55b:free'),('kilo','stepfun/step-3.7-flash:free'),
 ('kilo','cohere/north-mini-code:free'),('kilo','openrouter/free'),
]

def ask(prov, model, q, timeout=70):
    if prov=='gemini':
        k=creds('gemini')['api_key']
        url=f'https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent'
        h=['Content-Type: application/json',f'X-goog-api-key: {k}']
        body=json.dumps({'contents':[{'parts':[{'text':q}]}],'generationConfig':{'maxOutputTokens':2500}})
    else:
        url,key,extra={
         'mistral':('https://api.mistral.ai/v1/chat/completions',creds('mistral')['api_key'],[]),
         'openrouter':('https://openrouter.ai/api/v1/chat/completions',creds('openrouter')['api_key'],
                       ['HTTP-Referer: https://arena.ai','X-Title: ArenaAgentMode']),
         'kilo':('https://api.kilo.ai/api/gateway/chat/completions',creds('kilo')['api_key'],
                 ['X-KILOCODE-FEATURE: arena-agent']),
        }[prov]
        h=['Content-Type: application/json',f'Authorization: Bearer {key}']+extra
        body=json.dumps({'model':model,'messages':[{'role':'user','content':q}],'max_tokens':2500})
    cmd=['curl','-sS',url,'-X','POST','--data-binary','@-','--max-time',str(timeout)]
    for x in h: cmd+=['-H',x]
    p=subprocess.run(cmd,input=body,capture_output=True,text=True)
    try: d=json.loads(p.stdout)
    except Exception: return ''
    try:
        return ''.join(x.get('text','') for x in d['candidates'][0]['content']['parts'])
    except Exception: pass
    try:
        m=d['choices'][0]['message']; c=m.get('content') or ''
        if isinstance(c,list): c=''.join(x.get('text','') for x in c if isinstance(x,dict))
        return c or (m.get('reasoning') or '')
    except Exception: return ''

def score(entry):
    prov,model=entry
    got=0; lat=[]
    for q,check in TESTS:
        t0=time.time()
        a=ask(prov,model,q)
        lat.append(time.time()-t0)
        if a and check(a): got+=1
        time.sleep(0.4)
    return {'provider':prov,'model':model,'score':got,'of':len(TESTS),
            'avg_sec':round(sum(lat)/len(lat),2)}

res=[]
with ThreadPoolExecutor(max_workers=3) as ex:
    for r in ex.map(score,CANDIDATES):
        res.append(r)
        print(f"  {r['score']}/{r['of']}  {r['avg_sec']:5.2f}s  {r['provider']:11} {r['model']}",file=sys.stderr)
res.sort(key=lambda r:(-r['score'],r['avg_sec']))
json.dump(res,open(os.path.expanduser('~/ai_probe/quality.json'),'w'),indent=1)
print('\n== RANKED ==',file=sys.stderr)
for r in res: print(f"  {r['score']}/5 {r['avg_sec']:6.2f}s  {r['provider']:11} {r['model']}",file=sys.stderr)
