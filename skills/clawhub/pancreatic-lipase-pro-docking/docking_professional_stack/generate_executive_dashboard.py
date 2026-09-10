#!/usr/bin/env python3
"""
generate_executive_dashboard.py

Generate a polished, self-contained executive HTML dashboard for molecular docking / GI-fluid
virtual screening results. Designed for high-stakes presentation settings: government,
enterprise, grant review, pharma decision committees.

No external CSS/JS/CDN needed. Works offline.

Usage:
  python generate_executive_dashboard.py \
    --results speed_runs/myrun/final_ranked_results.csv \
    --metadata speed_runs/myrun/metadata.json \
    --out executive_dashboard.html \
    --title "Pancreatic Lipase Inhibition Screening"

If --results is omitted, a demo dashboard is generated.
"""
from __future__ import annotations
import argparse, csv, html, json, math, statistics, datetime
from pathlib import Path
from collections import Counter


def read_csv(path):
    with open(path, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))


def fnum(x, default=None):
    try:
        if x in (None, '', 'None', 'nan'): return default
        return float(x)
    except Exception:
        return default


def inum(x, default=0):
    try: return int(float(x))
    except Exception: return default


def esc(x):
    return html.escape(str(x if x is not None else ''))


def demo_rows():
    return [
        {'name':'orlistat_control','smiles':'CCCC...','vina_score_kcal_mol':'-8.9','prediction':'moderate predicted binder','confidence':'medium','GI_fluid_penalty':'3','key_flags':'high cLogP: micelle/lipid sequestration risk','MW':'495.7','cLogP':'6.1','TPSA':'72.9','Lipinski_violations':'1','Veber_pass':'True','PAINS_alerts':'','docking_status':'ok'},
        {'name':'candidate_A','smiles':'O=C1...','vina_score_kcal_mol':'-9.4','prediction':'strong predicted binder','confidence':'medium','GI_fluid_penalty':'1','key_flags':'moderate micelle-partition risk','MW':'412.4','cLogP':'4.7','TPSA':'88.2','Lipinski_violations':'0','Veber_pass':'True','PAINS_alerts':'','docking_status':'ok'},
        {'name':'candidate_B','smiles':'CCN...','vina_score_kcal_mol':'-7.8','prediction':'moderate predicted binder','confidence':'medium','GI_fluid_penalty':'0','key_flags':'','MW':'358.3','cLogP':'3.2','TPSA':'76.1','Lipinski_violations':'0','Veber_pass':'True','PAINS_alerts':'','docking_status':'ok'},
        {'name':'polyphenol_C','smiles':'Oc1...','vina_score_kcal_mol':'-8.2','prediction':'good docking but GI-fluid suitability concern','confidence':'low-medium','GI_fluid_penalty':'4','key_flags':'polyphenol-like; PAINS/assay interference risk','MW':'302.2','cLogP':'1.7','TPSA':'131.4','Lipinski_violations':'0','Veber_pass':'True','PAINS_alerts':'catechol_A','docking_status':'ok'},
        {'name':'weak_D','smiles':'CCC...','vina_score_kcal_mol':'-5.1','prediction':'weak predicted binder','confidence':'medium','GI_fluid_penalty':'0','key_flags':'','MW':'221.2','cLogP':'2.0','TPSA':'38.5','Lipinski_violations':'0','Veber_pass':'True','PAINS_alerts':'','docking_status':'ok'},
    ]


def load_metadata(path):
    if path and Path(path).exists():
        try: return json.loads(Path(path).read_text(encoding='utf-8'))
        except Exception: pass
    return {}


def status_class(pred, conf='', flags=''):
    p=(pred or '').lower(); c=(conf or '').lower(); fl=(flags or '').lower()
    if 'strong' in p and 'concern' not in p and 'low' not in c:
        return 'good'
    if 'moderate' in p and 'concern' not in p:
        return 'watch'
    if 'concern' in p or 'unreliable' in p or 'pains' in fl or 'low' in c:
        return 'risk'
    if 'weak' in p:
        return 'muted'
    return 'neutral'


def compute_summary(rows):
    scores=[fnum(r.get('vina_score_kcal_mol')) for r in rows]
    scores=[s for s in scores if s is not None]
    docked=sum(1 for r in rows if (r.get('docking_status') or '').lower() in ('ok','dry') or fnum(r.get('vina_score_kcal_mol')) is not None)
    strong=sum(1 for r in rows if 'strong' in (r.get('prediction') or '').lower() and 'concern' not in (r.get('prediction') or '').lower())
    moderate=sum(1 for r in rows if 'moderate' in (r.get('prediction') or '').lower() and 'concern' not in (r.get('prediction') or '').lower())
    concerns=sum(1 for r in rows if 'concern' in (r.get('prediction') or '').lower() or 'unreliable' in (r.get('prediction') or '').lower() or r.get('PAINS_alerts'))
    gi_penalties=[inum(r.get('GI_fluid_penalty'),0) for r in rows]
    return {
        'total': len(rows),
        'docked': docked,
        'strong': strong,
        'moderate': moderate,
        'concerns': concerns,
        'best_score': min(scores) if scores else None,
        'median_score': statistics.median(scores) if scores else None,
        'mean_gi_penalty': statistics.mean(gi_penalties) if gi_penalties else 0,
    }


def histogram_svg(values, width=560, height=180):
    vals=[v for v in values if v is not None]
    if not vals:
        return '<div class="empty">No docking-score data available.</div>'
    lo=math.floor(min(vals)); hi=math.ceil(max(vals))
    if lo==hi: lo-=1; hi+=1
    bins=10
    step=(hi-lo)/bins
    counts=[0]*bins
    for v in vals:
        idx=min(bins-1,max(0,int((v-lo)/step)))
        counts[idx]+=1
    maxc=max(counts) or 1
    pad=28; chart_w=width-2*pad; chart_h=height-2*pad
    bars=[]
    for i,c in enumerate(counts):
        x=pad+i*chart_w/bins+3
        bw=chart_w/bins-6
        bh=chart_h*c/maxc
        y=pad+chart_h-bh
        label=f'{lo+i*step:.1f}'
        bars.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{bw:.1f}" height="{bh:.1f}" rx="4" class="bar"/><text x="{x+bw/2:.1f}" y="{height-8}" text-anchor="middle" class="axis">{esc(label)}</text>')
    return f'''<svg viewBox="0 0 {width} {height}" class="chart" role="img" aria-label="Docking score distribution">
      <line x1="{pad}" y1="{pad+chart_h}" x2="{pad+chart_w}" y2="{pad+chart_h}" class="grid"/>
      <text x="{pad}" y="16" class="chart-title">Docking Score Distribution, kcal/mol</text>
      {''.join(bars)}
    </svg>'''


def donut_svg(rows, width=240, height=240):
    cats=Counter()
    for r in rows:
        cls=status_class(r.get('prediction'), r.get('confidence'), r.get('key_flags'))
        label={'good':'Priority','watch':'Promising','risk':'Risk/Concern','muted':'Weak','neutral':'Undetermined'}[cls]
        cats[label]+=1
    total=sum(cats.values()) or 1
    colors={'Priority':'#16a34a','Promising':'#d97706','Risk/Concern':'#dc2626','Weak':'#64748b','Undetermined':'#2563eb'}
    cx=width/2; cy=height/2; r=78; sw=34
    parts=[]; angle=-90
    for label,count in cats.items():
        frac=count/total; end=angle+frac*360
        large=1 if frac>0.5 else 0
        x1=cx+r*math.cos(math.radians(angle)); y1=cy+r*math.sin(math.radians(angle))
        x2=cx+r*math.cos(math.radians(end)); y2=cy+r*math.sin(math.radians(end))
        parts.append(f'<path d="M {x1:.2f} {y1:.2f} A {r} {r} 0 {large} 1 {x2:.2f} {y2:.2f}" fill="none" stroke="{colors[label]}" stroke-width="{sw}" stroke-linecap="round"><title>{esc(label)}: {count}</title></path>')
        angle=end
    legend=''.join(f'<span><i style="background:{colors[k]}"></i>{esc(k)}: {v}</span>' for k,v in cats.items())
    return f'''<div class="donut-wrap"><svg viewBox="0 0 {width} {height}" class="donut">{''.join(parts)}<text x="{cx}" y="{cy-2}" text-anchor="middle" class="donut-num">{total}</text><text x="{cx}" y="{cy+20}" text-anchor="middle" class="donut-label">Compounds</text></svg><div class="legend">{legend}</div></div>'''


def top_table(rows, n=25):
    def key(r):
        s=fnum(r.get('vina_score_kcal_mol'),999)
        gi=inum(r.get('GI_fluid_penalty'),0)
        return (s==999, s, gi)
    ordered=sorted(rows, key=key)[:n]
    trs=[]
    for i,r in enumerate(ordered,1):
        cls=status_class(r.get('prediction'), r.get('confidence'), r.get('key_flags'))
        trs.append(f'''<tr>
          <td class="rank">{i}</td>
          <td><b>{esc(r.get('name'))}</b><div class="subtle mono">{esc((r.get('smiles') or '')[:80])}</div></td>
          <td class="num">{esc(r.get('vina_score_kcal_mol',''))}</td>
          <td><span class="pill {cls}">{esc(r.get('prediction','undetermined'))}</span><div class="subtle">Confidence: {esc(r.get('confidence',''))}</div></td>
          <td class="num">{esc(r.get('GI_fluid_penalty','0'))}</td>
          <td>{esc(r.get('key_flags','') or r.get('PAINS_alerts',''))}</td>
        </tr>''')
    return '<table class="results"><thead><tr><th>#</th><th>Compound</th><th>Score</th><th>Decision Class</th><th>GI Penalty</th><th>Risk / Notes</th></tr></thead><tbody>'+''.join(trs)+'</tbody></table>'


def property_cards(rows):
    fields=[('MW','Molecular Weight'),('cLogP','cLogP'),('TPSA','TPSA'),('Lipinski_violations','Lipinski Viol.'),('GI_fluid_penalty','GI Penalty')]
    cards=[]
    for key,label in fields:
        vals=[fnum(r.get(key)) for r in rows]
        vals=[v for v in vals if v is not None]
        if vals:
            cards.append(f'<div class="mini"><span>{esc(label)}</span><b>{statistics.median(vals):.2f}</b><small>median; range {min(vals):.1f}–{max(vals):.1f}</small></div>')
    return ''.join(cards)


def make_html(rows, metadata, title, subtitle):
    summary=compute_summary(rows)
    scores=[fnum(r.get('vina_score_kcal_mol')) for r in rows]
    now=datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    target=metadata.get('target_pdb') or metadata.get('target') or 'Not specified'
    grid=metadata.get('grid') or metadata.get('grid_center') or 'Not specified'
    mode=metadata.get('mode','screening')
    no_scores = all(fnum(r.get('vina_score_kcal_mol')) is None for r in rows)
    dry_mode = str(mode).lower() == 'dry' or metadata.get('dry_mode') or no_scores
    dry_banner = ''
    if dry_mode:
        dry_banner = '<section class="panel danger-banner"><h2>DRY MODE / NO PHYSICAL DOCKING PERFORMED</h2><p>This report contains input processing, descriptors, GI-fluid flags, and workflow structure only. It must not be interpreted as molecular docking evidence because no valid Vina docking scores were produced.</p></section>'
    css=r'''
:root{--navy:#0b1220;--blue:#143a5a;--gold:#c9a227;--bg:#f4f7fb;--card:#ffffff;--muted:#64748b;--line:#d9e2ef;--green:#16a34a;--amber:#d97706;--red:#dc2626;--slate:#475569}*{box-sizing:border-box}body{margin:0;background:linear-gradient(180deg,#eef4fb,#f7f9fc);font-family:Inter,Segoe UI,Roboto,Arial,sans-serif;color:#111827}.cover{background:radial-gradient(circle at 10% 0%,#1e4f78 0,#0b1220 45%,#050816 100%);color:white;padding:34px 42px 28px;border-bottom:5px solid var(--gold);position:relative;overflow:hidden}.cover:after{content:"";position:absolute;right:-120px;top:-160px;width:420px;height:420px;border:1px solid rgba(255,255,255,.09);border-radius:50%;box-shadow:0 0 0 70px rgba(255,255,255,.025),0 0 0 140px rgba(255,255,255,.015)}.seal{display:inline-flex;gap:10px;align-items:center;padding:8px 12px;border:1px solid rgba(255,255,255,.25);border-radius:999px;background:rgba(255,255,255,.08);font-size:12px;letter-spacing:.08em;text-transform:uppercase}.seal i{width:10px;height:10px;background:var(--gold);border-radius:50%;display:inline-block}.cover h1{font-size:34px;line-height:1.1;margin:18px 0 8px;max-width:900px}.cover p{max-width:900px;color:#cbd5e1;font-size:15px}.meta-strip{display:flex;gap:18px;flex-wrap:wrap;margin-top:24px}.meta-strip div{background:rgba(255,255,255,.08);padding:12px 14px;border-radius:12px;border:1px solid rgba(255,255,255,.12);min-width:180px}.meta-strip span{display:block;color:#9fb3c8;font-size:11px;text-transform:uppercase}.meta-strip b{font-size:14px}.container{padding:26px 42px 60px;max-width:1500px;margin:auto}.cards{display:grid;grid-template-columns:repeat(6,1fr);gap:14px;margin-top:-48px;position:relative;z-index:3}.card{background:var(--card);border:1px solid var(--line);border-radius:18px;padding:18px;box-shadow:0 16px 38px rgba(15,23,42,.09)}.metric span{font-size:11px;text-transform:uppercase;color:var(--muted);letter-spacing:.06em}.metric b{display:block;font-size:28px;margin-top:8px;color:#0f172a}.metric small{color:var(--muted)}.grid2{display:grid;grid-template-columns:1.2fr .8fr;gap:18px;margin-top:18px}.grid3{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}.panel{background:#fff;border:1px solid var(--line);border-radius:18px;padding:20px;box-shadow:0 8px 24px rgba(15,23,42,.05)}.panel h2{font-size:18px;margin:0 0 14px;color:#0f172a}.panel h3{font-size:14px;margin:0 0 10px;text-transform:uppercase;letter-spacing:.06em;color:#334155}.executive{font-size:15px;line-height:1.65}.executive b{color:#0b3b60}.pill{display:inline-block;padding:5px 9px;border-radius:999px;font-size:12px;font-weight:700}.good{background:#dcfce7;color:#166534}.watch{background:#fef3c7;color:#92400e}.risk{background:#fee2e2;color:#991b1b}.muted{background:#e2e8f0;color:#334155}.neutral{background:#dbeafe;color:#1e40af}.results{width:100%;border-collapse:separate;border-spacing:0;font-size:13px}.results th{text-align:left;background:#f1f5f9;color:#334155;padding:11px;border-top:1px solid var(--line);border-bottom:1px solid var(--line)}.results td{padding:11px;border-bottom:1px solid #eef2f7;vertical-align:top}.results tr:hover td{background:#fafcff}.rank{font-weight:800;color:#0b3b60}.num{text-align:right;font-variant-numeric:tabular-nums}.subtle{color:var(--muted);font-size:12px;margin-top:4px}.mono{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,monospace}.chart{width:100%;height:auto}.bar{fill:#1d4ed8;opacity:.82}.grid{stroke:#cbd5e1;stroke-width:1}.axis{font-size:10px;fill:#64748b}.chart-title{font-size:13px;font-weight:700;fill:#334155}.donut-wrap{display:flex;gap:16px;align-items:center;justify-content:center}.donut{max-width:210px}.donut-num{font-size:26px;font-weight:800;fill:#0f172a}.donut-label{font-size:11px;fill:#64748b}.legend{display:grid;gap:7px;font-size:12px}.legend span{display:flex;gap:7px;align-items:center}.legend i{display:inline-block;width:10px;height:10px;border-radius:3px}.mini{background:#f8fafc;border:1px solid #e2e8f0;border-radius:14px;padding:13px}.mini span{display:block;color:#64748b;font-size:11px;text-transform:uppercase}.mini b{display:block;font-size:22px;margin:5px 0}.mini small{color:#64748b}.note{background:#fffbeb;border:1px solid #f4d06f;border-radius:14px;padding:14px;color:#713f12}.danger-banner{background:#fff1f2!important;border:2px solid #dc2626!important;color:#7f1d1d}.danger-banner h2{color:#991b1b!important}.footer{margin-top:28px;color:#64748b;font-size:12px;border-top:1px solid var(--line);padding-top:18px}.toolbar{position:sticky;top:0;z-index:10;background:rgba(255,255,255,.92);backdrop-filter:blur(8px);border-bottom:1px solid var(--line);padding:9px 42px;display:flex;justify-content:space-between;align-items:center}.toolbar button{border:1px solid #cbd5e1;background:#fff;border-radius:10px;padding:8px 12px;cursor:pointer}.toolbar input{border:1px solid #cbd5e1;border-radius:10px;padding:9px 12px;min-width:260px}@media(max-width:1100px){.cards{grid-template-columns:repeat(3,1fr)}.grid2{grid-template-columns:1fr}.grid3{grid-template-columns:1fr}}@media print{.toolbar{display:none}.cover{break-after:avoid}.panel,.card{box-shadow:none}.container{padding:20px}.cards{margin-top:20px}.results tr{break-inside:avoid}}
'''
    metadata_pre=esc(json.dumps(metadata, indent=2)[:4000])
    html_doc=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{esc(title)}</title><style>{css}</style></head><body>
<div class="toolbar"><div><b>Executive Scientific Dashboard</b></div><div><input id="q" placeholder="Search compound, flag, prediction..." oninput="filterRows()"><button onclick="window.print()">Print / Save PDF</button></div></div>
<header class="cover"><div class="seal"><i></i> Confidential Scientific Decision Support</div><h1>{esc(title)}</h1><p>{esc(subtitle)}</p><div class="meta-strip"><div><span>Target</span><b>{esc(target)}</b></div><div><span>Mode</span><b>{esc(mode)}</b></div><div><span>Generated</span><b>{esc(now)}</b></div><div><span>Grid / Site</span><b>{esc(str(grid)[:80])}</b></div></div></header>
<main class="container">
<section class="cards">
  <div class="card metric"><span>Total Compounds</span><b>{summary['total']}</b><small>records analyzed</small></div>
  <div class="card metric"><span>Docked / Processed</span><b>{summary['docked']}</b><small>with score or status</small></div>
  <div class="card metric"><span>Priority Hits</span><b>{summary['strong']}</b><small>strong class</small></div>
  <div class="card metric"><span>Promising Hits</span><b>{summary['moderate']}</b><small>moderate class</small></div>
  <div class="card metric"><span>Best Score</span><b>{'' if summary['best_score'] is None else f"{summary['best_score']:.2f}"}</b><small>kcal/mol</small></div>
  <div class="card metric"><span>GI Risk Flags</span><b>{summary['concerns']}</b><small>concerns/alerts</small></div>
</section>
{dry_banner}
<section class="grid2">
  <div class="panel"><h2>Executive Interpretation</h2><div class="executive">
    <p>This dashboard summarizes a computational screening workflow for <b>{esc(target)}</b>. Compounds are ranked by docking score, predicted class, and gastrointestinal-fluid suitability flags. The output is intended for <b>decision support</b>, not standalone biological proof.</p>
    <p><b>Primary decision rule:</b> prioritize compounds with favorable docking scores, plausible active-site binding, low GI-fluid penalty, low PAINS/assay-interference risk, and medium/high confidence. Compounds with strong docking but high GI penalty should be treated as formulation or assay-risk candidates.</p>
  </div><div class="note"><b>Scientific caution:</b> Molecular docking predicts binding hypotheses. Pancreatic lipase inhibition must be confirmed experimentally in GI-relevant enzymatic media, ideally with bile salts/colipase and an orlistat reference control.</div></div>
  <div class="panel"><h2>Portfolio Decision Classes</h2>{donut_svg(rows)}</div>
</section>
<section class="grid2">
  <div class="panel"><h2>Score Distribution</h2>{histogram_svg(scores)}</div>
  <div class="panel"><h2>Property Snapshot</h2><div class="grid3">{property_cards(rows)}</div></div>
</section>
<section class="panel" style="margin-top:18px"><h2>Ranked Candidate Table</h2>{top_table(rows, 50)}</section>
<section class="panel" style="margin-top:18px"><h2>Method & Audit Metadata</h2><pre class="mono subtle" style="white-space:pre-wrap">{metadata_pre}</pre></section>
<div class="footer">Generated by the professional docking workflow. Report is self-contained and offline-capable. Use for triage, governance review, and prioritization; not as a substitute for wet-lab validation.</div>
</main>
<script>
function filterRows(){{
  const q=document.getElementById('q').value.toLowerCase();
  document.querySelectorAll('table.results tbody tr').forEach(tr=>{{
    tr.style.display=tr.innerText.toLowerCase().includes(q)?'':'none';
  }});
}}
</script></body></html>'''
    return html_doc


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--results', help='final_ranked_results.csv')
    ap.add_argument('--metadata', help='metadata.json')
    ap.add_argument('--demo', action='store_true', help='generate a demo dashboard with synthetic example rows')
    ap.add_argument('--out', default='executive_dashboard.html')
    ap.add_argument('--title', default='Molecular Docking Executive Dashboard')
    ap.add_argument('--subtitle', default='Professional virtual-screening output with docking, GI-fluid suitability, risk flags, and decision-ready candidate ranking.')
    args=ap.parse_args()
    if args.demo:
        rows = demo_rows()
    elif args.results and Path(args.results).exists():
        rows = read_csv(args.results)
    else:
        raise SystemExit('ERROR: --results final_ranked_results.csv is required unless --demo is used. Refusing to generate placeholder/demo results by accident.')
    metadata=load_metadata(args.metadata)
    if not metadata:
        metadata={'target_pdb':'1LPB','mode':'unknown','grid':'unknown','note':'No metadata.json supplied.'}
    out=Path(args.out)
    out.write_text(make_html(rows, metadata, args.title, args.subtitle), encoding='utf-8')
    print(out)

if __name__=='__main__':
    main()
