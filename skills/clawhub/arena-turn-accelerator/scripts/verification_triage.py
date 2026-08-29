#!/usr/bin/env python3
"""verification_triage.py — you ARE human; find WHY you keep getting challenged.
Bot detection is a probabilistic SCORE. This ranks false-positive triggers and gives
legitimate fixes. NOT a CAPTCHA solver or bypass."""
import argparse
RULES = [
 (30,"cookies_blocked","Verification cookie is blocked",
  "The token proving you already passed can't persist, so every session re-challenges you. #1 cause of REPEAT CAPTCHAs.",
  "Allow cookies/site data for this site (exempt from 'block third-party cookies' and clear-on-exit)."),
 (25,"blocker_strict","Aggressive content/script blocker",
  "If the challenge script can't load, the check hard-fails straight to a CAPTCHA.",
  "Allowlist the site in uBlock/Shields/strict tracking protection."),
 (22,"vpn","VPN / datacenter / shared IP",
  "IP reputation is shared. Datacenter/NAT exits are used by real bots, so you inherit their score.",
  "Disable the VPN for this site, or use a residential-reputation exit."),
 (15,"many_tabs","Many parallel tabs/sessions","Simultaneous identical sessions look like scripted fan-out.","Close duplicates; keep one active tab."),
 (14,"headless","Automated/headless browser signals","Webdriver flags are a direct automation signal.","Use a normal browser window."),
 (12,"rapid","Very rapid repeated requests","Superhuman cadence trips rate heuristics.","Let a turn finish before re-sending."),
 (10,"private","Private/incognito or profile switching","No accumulated trust history.","Use one persistent profile."),
 (10,"stale_session","Stale cookies after a reconnect","A half-restored session can't be attested.","Hard-refresh once after reconnecting."),
 (8,"anon","Not signed in","Anonymous sessions carry less trust.","Sign in."),
 (6,"clock","Clock/timezone mismatch","Token validity windows fail when the clock is off.","Enable automatic date/time."),
]
def main():
    p = argparse.ArgumentParser()
    for f,c in (("vpn",["yes","no"]),("headless",["yes","no"]),("rapid",["yes","no"]),("private",["yes","no"])):
        p.add_argument(f"--{f}", choices=c, default=None)
    p.add_argument("--blocker", choices=["strict","normal","none"], default=None)
    p.add_argument("--cookies", choices=["blocked","allowed"], default=None)
    p.add_argument("--tabs", type=int, default=None)
    p.add_argument("--signed-in", choices=["yes","no"], default=None)
    a = p.parse_args()
    cond = {"vpn":a.vpn=="yes","blocker_strict":a.blocker=="strict","cookies_blocked":a.cookies=="blocked",
            "many_tabs":(a.tabs or 0)>=4,"headless":a.headless=="yes","rapid":a.rapid=="yes",
            "private":a.private=="yes","anon":a.signed_in=="no","stale_session":False,"clock":False}
    answered = any(v is not None for v in [a.vpn,a.blocker,a.cookies,a.tabs,a.headless,a.rapid,a.private,a.signed_in])
    print("YOU ARE HUMAN. Bot-detection is a probabilistic score, not a judgement about you.")
    print("Innocent signals stack until you cross a threshold. Here's what likely tipped it.\n")
    if not answered:
        print("Full trigger checklist (pass flags to score YOUR setup):\n")
        for w,_k,l,why,fix in sorted(RULES,key=lambda r:-r[0]):
            print(f"[{w:>2} pts] {l}\n         why: {why}\n         fix: {fix}\n")
        return
    hits=[(w,l,why,fix) for w,k,l,why,fix in RULES if cond.get(k)]
    total=sum(h[0] for h in hits)
    risk="LOW" if total<25 else "MEDIUM" if total<55 else "HIGH"
    bar="#"*min(20,total//5)+"."*(20-min(20,total//5))
    print(f"FALSE-POSITIVE RISK: {risk} ({total} pts) [{bar}]\n")
    if not hits:
        print("No common triggers detected. Likely ISP IP reputation. Signing in usually resolves it."); return
    print("Ordered fixes (highest yield first):\n")
    for i,(w,l,why,fix) in enumerate(sorted(hits,key=lambda h:-h[0]),1):
        print(f"{i}. {l}  (+{w})\n   why: {why}\n   FIX: {fix}\n")
    print("Not included by design: solving, bypassing, or spoofing verification. Removing "
          "false-positive triggers is the honest fix — and the durable one.")
if __name__ == "__main__": main()
