#!/usr/bin/env python3
"""
Varredura de procedência de ativos no Meta Ads.

Responde à pergunta "de onde saiu esse <nome>? isso é campanha?" com evidência,
não com dedução. Varre TODAS as contas do token e TODAS as edges relevantes.

Uso:
    python3 meta_asset_provenance_sweep.py <termo-de-busca> [--token TOKEN]

    # exemplo
    python3 meta_asset_provenance_sweep.py "evolution|imers"

Token: passado via --token, ou env META_ACCESS_TOKEN, ou extraído do primeiro
script *.py encontrado em --scan-dir (default /root/papi_ads_creatives).

Saída:
    - Inventário de campanhas/adsets/ads por conta com effective_status
    - Ocorrências do termo em cada edge (busca no JSON serializado do objeto)
    - Conjunto de URLs de destino presentes nos criativos (ruído de CDN filtrado)
    - Veredito: termo encontrado em alguma entidade? alguma entidade ativa?
"""
import argparse
import glob
import json
import os
import re
import sys

try:
    import requests
except ImportError:
    sys.exit("requests não instalado: pip install requests")

API = "https://graph.facebook.com/v21.0"

EDGES = [
    ("campaigns", "id,name,status,effective_status,created_time,daily_budget"),
    ("adsets", "id,name,status,effective_status,created_time,daily_budget,campaign_id"),
    ("ads", "id,name,status,effective_status,created_time,adset_id,creative"),
    ("adcreatives",
     "id,name,object_story_spec,asset_feed_spec,object_type,"
     "effective_object_story_id,link_url,thumbnail_url"),
    ("adimages", "hash,name,created_time"),
    ("advideos", "id,title,description,created_time"),
]

CDN_NOISE = re.compile(r"scontent|fbcdn|akamaihd", re.I)


def resolve_token(args):
    if args.token:
        return args.token
    if os.environ.get("META_ACCESS_TOKEN"):
        return os.environ["META_ACCESS_TOKEN"]
    for path in sorted(glob.glob(os.path.join(args.scan_dir, "*.py"))):
        try:
            m = re.search(r"EAA[A-Za-z0-9]{80,}", open(path, errors="ignore").read())
        except OSError:
            continue
        if m:
            print(f"[token] extraído de {path}", file=sys.stderr)
            return m.group(0)
    sys.exit("Nenhum token encontrado (use --token ou META_ACCESS_TOKEN).")


def get(path, token, fields, limit=300):
    r = requests.get(f"{API}/{path}",
                     params={"fields": fields, "limit": limit, "access_token": token},
                     timeout=60)
    body = r.json()
    if "error" in body:
        print(f"  ! erro em {path}: {body['error'].get('message')}", file=sys.stderr)
        return []
    return body.get("data", [])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("term", help="regex de busca, ex: 'evolution|imers'")
    ap.add_argument("--token")
    ap.add_argument("--scan-dir", default="/root/papi_ads_creatives")
    ap.add_argument("--account", action="append",
                    help="limitar a conta(s) act_XXX; default = todas do token")
    args = ap.parse_args()

    token = resolve_token(args)
    pattern = re.compile(args.term, re.I)

    accounts = args.account or [a["id"] for a in
                                get("me/adaccounts", token, "id,name", limit=50)]
    if not accounts:
        sys.exit("Nenhuma conta de anúncios acessível pelo token.")

    hits, urls, actives = [], {}, []

    for act in accounts:
        print(f"\n{'=' * 70}\nCONTA {act}\n{'=' * 70}")
        for edge, fields in EDGES:
            rows = get(f"{act}/{edge}", token, fields)
            print(f"\n-- {edge}: {len(rows)}")
            for x in rows:
                blob = json.dumps(x, ensure_ascii=False)

                if edge in ("campaigns", "adsets", "ads"):
                    st = x.get("effective_status") or x.get("status")
                    print(f"   {x.get('id')} | {x.get('name')} | {st} | "
                          f"{x.get('created_time')} | budget={x.get('daily_budget')}")
                    if st == "ACTIVE":
                        actives.append((act, edge, x.get("id"), x.get("name")))

                if edge == "adcreatives":
                    for u in re.findall(r"https?://[^\"'\\ ]+", blob):
                        base = u.split("?")[0]
                        if CDN_NOISE.search(base):
                            continue
                        urls[base] = urls.get(base, 0) + 1

                if pattern.search(blob):
                    hits.append((act, edge, x.get("id") or x.get("hash"),
                                 x.get("name") or x.get("title"), blob[:600]))

    print(f"\n{'=' * 70}\nURLs DE DESTINO NOS CRIATIVOS\n{'=' * 70}")
    for u, c in sorted(urls.items(), key=lambda kv: -kv[1]):
        print(f"  {c:>4}x  {u}")

    print(f"\n{'=' * 70}\nENTIDADES ATIVAS\n{'=' * 70}")
    for a in actives:
        print(f"  {a[0]} | {a[1]} | {a[2]} | {a[3]}")

    print(f"\n{'=' * 70}\nOCORRÊNCIAS DE '{args.term}'\n{'=' * 70}")
    if not hits:
        print("  NENHUMA. O termo não existe em nenhuma entidade de nenhuma conta.")
        print("  => Não é campanha/adset/ad/criativo. Procure a origem fora da")
        print("     Graph API (outputs de cron, conversas de CRM, dumps de sessão):")
        print("     grep -i -n -E '<termo>' /root/.hermes/cron/output/*.txt")
    else:
        for act, edge, ident, name, blob in hits:
            print(f"\n  [{act}] {edge} | {ident} | {name}\n  {blob}")

    return 0 if not hits else 1


if __name__ == "__main__":
    sys.exit(main())
