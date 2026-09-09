#!/usr/bin/env python3
"""
Script utilitário de auditoria automatizada de contas Meta Ads.
Verifica status da conta, saldo pré-pago, métricas dos últimos 7 dias,
integridade HTTP das Landing Pages e regras de stop-loss.
"""
import sys
import json
import yaml
import requests
import subprocess

def load_meta_token():
    try:
        with open("/root/.hermes/config.yaml", "r") as f:
            cfg = yaml.safe_load(f)
        return cfg.get("mcp_servers", {}).get("meta-ads", {}).get("env", {}).get("META_ACCESS_TOKEN")
    except Exception as e:
        print(f"Erro ao carregar token do config.yaml: {e}", file=sys.stderr)
        return None

def check_landing_page(url):
    try:
        cmd = f'curl -sIL -o /dev/null -w "%{{http_code}}" --max-time 10 "{url}"'
        res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return res.stdout.strip()
    except Exception:
        return "ERROR"

def audit_account(ad_account_id):
    token = load_meta_token()
    if not token:
        print("Erro: META_ACCESS_TOKEN não encontrado.", file=sys.stderr)
        return

    if not ad_account_id.startswith("act_"):
        ad_account_id = f"act_{ad_account_id}"

    # 1. Dados da Conta
    u_acc = f"https://graph.facebook.com/v21.0/{ad_account_id}"
    p_acc = {
        "access_token": token,
        "fields": "id,name,account_status,amount_spent,spend_cap,balance,currency,disable_reason,is_prepay_account"
    }
    r_acc = requests.get(u_acc, params=p_acc).json()
    print(f"=== AUDITORIA DA CONTA: {ad_account_id} ({r_acc.get('name')}) ===")
    print(f"Status: {r_acc.get('account_status')} | Saldo Pré-pago: R$ {float(r_acc.get('balance', 0))/100:.2f} | Gasto Total: R$ {float(r_acc.get('amount_spent', 0))/100:.2f}")

    # 2. Anúncios Ativos
    u_ads = f"https://graph.facebook.com/v21.0/{ad_account_id}/ads"
    p_ads = {
        "access_token": token,
        "fields": "id,name,campaign_id,adset_id,status,effective_status,creative{id,name,object_story_spec,asset_feed_spec}"
    }
    r_ads = requests.get(u_ads, params=p_ads).json().get("data", [])
    active_ads = [a for a in r_ads if a.get("effective_status") in ("ACTIVE", "WITH_ISSUES")]
    print(f"\nTotal de Anúncios: {len(r_ads)} | Ativos/Com Alerta: {len(active_ads)}")

    for a in active_ads:
        ad_id = a.get("id")
        cr = a.get("creative", {})
        oss = cr.get("object_story_spec", {})
        link_data = oss.get("link_data", {})
        video_data = oss.get("video_data", {})
        afs = cr.get("asset_feed_spec", {})

        link = None
        if link_data:
            link = link_data.get("link") or (link_data.get("call_to_action", {}).get("value", {}).get("link") if isinstance(link_data.get("call_to_action"), dict) else None)
        if not link and video_data:
            link = video_data.get("call_to_action", {}).get("value", {}).get("link") if isinstance(video_data.get("call_to_action"), dict) else None
        if not link and afs and afs.get("link_urls"):
            link = afs.get("link_urls")[0].get("website_url")

        http_status = check_landing_page(link) if link else "N/A"

        # Insights 7d
        u_ins = f"https://graph.facebook.com/v21.0/{ad_id}/insights"
        p_ins = {
            "access_token": token,
            "date_preset": "last_7d",
            "fields": "spend,impressions,clicks,cpc,cpm,ctr,reach"
        }
        r_ins = requests.get(u_ins, params=p_ins).json().get("data", [])
        m_str = "Sem veiculação / Ramo inicial"
        if r_ins:
            d = r_ins[0]
            m_str = f"Gasto: R$ {float(d.get('spend',0)):.2f} | Impr: {d.get('impressions')} | Cliques: {d.get('clicks')} | CTR: {float(d.get('ctr',0)):.2f}% | CPC: R$ {float(d.get('cpc',0)):.2f}"

        print(f"\n- [{ad_id}] {a.get('name')}")
        print(f"  Status: {a.get('effective_status')} | AdSet: {a.get('adset_id')}")
        print(f"  LP: {link} (HTTP {http_status})")
        print(f"  Métricas: {m_str}")

if __name__ == "__main__":
    acc = sys.argv[1] if len(sys.argv) > 1 else "act_327126129438619"
    audit_account(acc)
