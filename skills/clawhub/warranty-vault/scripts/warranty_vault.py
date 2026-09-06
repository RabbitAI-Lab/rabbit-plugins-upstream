#!/usr/bin/env python3
"""
warranty_vault.py — track purchases, warranties, and consumer-rights coverage.

Vault: JSON (default ~/.warranty-vault.json). Pure stdlib.
"""
import argparse
import datetime as dt
import json
import os
import sys

DEFAULT_FILE = os.path.join(os.path.expanduser("~"), ".warranty-vault.json")

JURISDICTIONS = ["US", "UK", "EU"]
STATUTORY = {  # months of statutory rights from purchase
    "UK": 72,   # Consumer Rights Act + Limitation Act (England/Wales/NI; 60 Scotland)
    "EU": 24,   # Directive (EU) 2019/771 minimum
    "US": 0,    # no general federal repair right
}
UK_BURDEN_MONTHS = 6  # reversed burden of proof window

CARD_PERKS = {
    # program -> (extra months after mfr warranty, max base-warranty months eligible)
    "visa-infinite": (24, 36),
    "visa-signature": (12, 36),
    "world-elite-mc": (12, 24),
    "amex": (12, 24),
}
CARD_HINT = "visa-infinite | visa-signature | world-elite-mc | amex | none"

REMEDY_HINT = "repair | replace | refund"


def today():
    return dt.date.today()


def d(s):
    return dt.date.fromisoformat(s) if s else None


def months_add(date, months):
    m = date.month - 1 + months
    y = date.year + m // 12
    m = m % 12 + 1
    day = min(date.day, [31, 29 if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0) else 28,
                         31, 30, 31, 30, 31, 31, 30, 31, 30, 31][m - 1])
    return dt.date(y, m, day)


def load(path):
    if not os.path.exists(path):
        return {"jurisdiction": "US", "entries": []}
    with open(path) as f:
        return json.load(f)


def save(reg, path):
    with open(path, "w") as f:
        json.dump(reg, f, indent=2)
    print(f"saved -> {path}")


def find(reg, eid):
    for e in reg["entries"]:
        if e["id"] == eid:
            return e
    return None


def need(reg, eid):
    e = find(reg, eid)
    if not e:
        sys.exit(f"error: no entry '{eid}' — try 'list'")
    return e


def card_program(card):
    if not card:
        return None
    c = card.lower()
    for k in CARD_PERKS:
        if k in c or k.split("-")[0] in c and "infinite" in c:
            return k
    if "infinite" in c:
        return "visa-infinite"
    if "amex" in c or "american express" in c:
        return "amex"
    if "world elite" in c:
        return "world-elite-mc"
    if "visa" in c:
        return "visa-signature"
    if "mastercard" in c or "mc" == c.strip():
        return "world-elite-mc"
    return None


# --------------------------- coverage engine -------------------------------
def layers_for(e, jurisdiction):
    """Return list of layer dicts with end dates and status."""
    out = []
    t = today()
    p = d(e["purchased"])
    wm = e.get("warranty_mo") or 0
    if wm:
        end = months_add(p, wm)
        out.append(dict(name="manufacturer warranty", end=end,
                        live=end >= t, counterparty="manufacturer",
                        evidence="proof of purchase, serial"))
    sm = STATUTORY.get(jurisdiction, 0)
    if sm:
        end = months_add(p, sm)
        age_mo = (t - p).days / 30.44
        if jurisdiction == "UK":
            note = (f"burden REVERSED (fault presumed inherent) — age {age_mo:.0f} mo"
                    if age_mo <= UK_BURDEN_MONTHS else
                    f"you must show fault inherent — age {age_mo:.0f} mo")
        else:
            note = f"presumption of non-conformity in first 12 mo; age {age_mo:.0f} mo"
        out.append(dict(name=f"statutory rights ({jurisdiction})", end=end,
                        live=end >= t, counterparty="RETAILER",
                        evidence="proof of purchase + fault inherent" + (
                            " (presumed)" if jurisdiction == "UK" and age_mo <= UK_BURDEN_MONTHS else ""),
                        note=note))
    em = e.get("extended_mo") or 0
    if em:
        end = months_add(p, em)
        out.append(dict(name=f"extended plan ({e.get('extended_by') or '3rd party'})",
                        end=end, live=end >= t,
                        counterparty=f"plan admin ({e.get('extended_by') or 'plan provider'})",
                        evidence=f"plan number/receipt{'; deductible ' + str(e['extended_deductible']) if e.get('extended_deductible') else ''}"))
    prog = card_program(e.get("card"))
    if prog and wm:
        extra, max_base = CARD_PERKS[prog]
        if wm <= max_base:
            end = months_add(months_add(p, wm), extra)
            out.append(dict(name=f"card perk ({prog} +{extra}mo after mfr)", end=end,
                            live=end >= t, counterparty=f"card issuer — pay with {e['card']}",
                            evidence="card statement line + claim form"))
        else:
            out.append(dict(name=f"card perk ({prog})", end=None, live=False,
                            counterparty="—",
                            evidence=f"ineligible: base warranty {wm}mo > {max_base}mo cap"))
    return sorted(out, key=lambda x: (x["end"] or dt.date.min), reverse=True)


def days_left(end):
    return (end - today()).days if end else None


# --------------------------- subcommands -----------------------------------
def cmd_add(a):
    reg = load(a.file)
    if find(reg, a.id):
        sys.exit(f"error: id '{a.id}' exists — use 'update'")
    if a.jurisdiction:
        reg["jurisdiction"] = a.jurisdiction
    e = dict(id=a.id, name=a.name or a.id, category=a.category or "other",
             price=a.price, purchased=a.purchased,
             warranty_mo=a.warranty_mo, receipt=a.receipt, card=a.card,
             serial=a.serial, registered=a.registered, notes=a.notes,
             extended_mo=a.extended_mo, extended_by=a.extended_by,
             extended_deductible=a.extended_deductible)
    missing = [k for k in ("price", "purchased") if not e[k]]
    if missing:
        sys.exit(f"error: --price and --purchased are required")
    reg["entries"].append(e)
    reg["entries"].sort(key=lambda x: x["purchased"], reverse=True)
    save(reg, a.file)


def cmd_update(a):
    reg = load(a.file)
    e = need(reg, a.id)
    changed = False
    for k in ("name", "category", "receipt", "card", "serial", "notes",
              "extended_by", "registered"):
        v = getattr(a, k, None)
        if v:
            e[k] = v
            changed = True
    for k in ("price", "warranty_mo", "extended_mo", "extended_deductible"):
        v = getattr(a, k, None)
        if v is not None:
            e[k] = v
            changed = True
    if a.purchased:
        e["purchased"] = a.purchased
        changed = True
    if a.mark_registered:
        e["registered"] = today().isoformat()
        changed = True
    if not changed:
        sys.exit("nothing to update")
    save(reg, a.file)


def cmd_remove(a):
    reg = load(a.file)
    e = need(reg, a.id)
    reg["entries"].remove(e)
    save(reg, a.file)


def cmd_list(a):
    reg = load(a.file)
    if not reg["entries"]:
        print("(empty vault — 'add' your first purchase)")
        return
    print(f"jurisdiction: {reg.get('jurisdiction') or 'US'}   "
          f"({len(reg['entries'])} items, total ${sum(e.get('price') or 0 for e in reg['entries']):,.0f})")
    print(f"\n{'ID':<14}{'PURCHASED':<11}{'$':>7}  {'MFR-MO':>7}{'EXT':>4}  NAME")
    print("-" * 76)
    for e in reg["entries"]:
        print(f"{e['id']:<14}{e['purchased']:<11}{e.get('price') or 0:>7,.0f}  "
              f"{str(e.get('warranty_mo') or '-'):>7}{str(e.get('extended_mo') or '-'):>4}  "
              f"{e.get('name')[:34]}")


def cmd_covered(a):
    reg = load(a.file)
    e = need(reg, a.id)
    jur = a.jurisdiction or reg.get("jurisdiction") or "US"
    print(f"COVERAGE — {e['name']} ({e['id']})")
    print(f"purchased {e['purchased']} for ${e.get('price') or 0:,.0f}; jurisdiction {jur}\n")
    any_live = False
    for ly in layers_for(e, jur):
        end = ly["end"]
        left = days_left(end)
        state = ("LIVE" if ly["live"] else
                 ("DEAD" if end else "N/A"))
        any_live |= ly["live"]
        print(f"  [{state:>3}] {ly['name']}")
        if end:
            print(f"         ends {end} "
                  f"({left} days {'remaining' if left >= 0 else 'ago'})")
        if ly.get("note"):
            print(f"         {ly['note']}")
        print(f"         claim vs: {ly['counterparty']}; bring: {ly['evidence']}")
    print()
    if any_live:
        print("NEXT: run 'claim' to draft the letter; attach evidence above.")
    else:
        print("No live coverage — repair out of pocket, or check recall databases")
        print("(recalls are free repairs regardless of warranty).")


def cmd_expiring(a):
    reg = load(a.file)
    jur = reg.get("jurisdiction") or "US"
    rows = []
    for e in reg["entries"]:
        for ly in layers_for(e, jur):
            left = days_left(ly["end"])
            if left is not None and 0 <= left <= a.days:
                rows.append((left, e, ly))
    rows.sort(key=lambda x: x[0])
    if not rows:
        print(f"nothing expires in the next {a.days} days")
        return
    print(f"EXPIRING WITHIN {a.days} DAYS — act now:\n")
    for left, e, ly in rows:
        print(f"  {e['id']:<14}{ly['name']:<38} ends {ly['end']} ({left}d)")
        if not e.get("registered") and (today() - d(e["purchased"])).days <= 90:
            print(f"  {'':<14}-> also: never registered — register NOW (may extend cover)")


def cmd_report(a):
    reg = load(a.file)
    jur = reg.get("jurisdiction") or "US"
    if a.jurisdiction:
        jur = a.jurisdiction
    if a.json:
        out = dict(jurisdiction=jur, total_value=sum(e.get("price") or 0
                     for e in reg["entries"]),
                   entries=[])
        for e in reg["entries"]:
            out["entries"].append(dict(id=e["id"], name=e.get("name"),
                price=e.get("price"), purchased=e["purchased"],
                category=e.get("category"),
                live_layers=[ly["name"] for ly in layers_for(e, jur) if ly["live"]],
                any_live=any(ly["live"] for ly in layers_for(e, jur))))
        print(json.dumps(out, indent=2))
        return
    print(f"VAULT REPORT — {len(reg['entries'])} items, "
          f"${sum(e.get('price') or 0 for e in reg['entries']):,.0f} total, jurisdiction {jur}\n")
    print(f"{'ID':<14}{'$':>7}{'AGE':>10}  COVERAGE NOW")
    print("-" * 78)
    for e in reg["entries"]:
        age = (today() - d(e["purchased"])).days
        lys = layers_for(e, jur)
        live = [ly["name"].split(" (")[0] for ly in lys if ly["live"]]
        print(f"{e['id']:<14}{e.get('price') or 0:>7,.0f}{age//365:>6}y{age%365//30:>3}m  "
              f"{', '.join(live) if live else '— none —'}")
    # health flags
    flags = []
    for e in reg["entries"]:
        age = (today() - d(e["purchased"])).days
        if not e.get("registered") and age <= 90:
            flags.append(f"{e['id']}: unregistered ({age}d old) — register now")
        if not e.get("receipt"):
            flags.append(f"{e['id']}: no receipt location recorded")
    if flags:
        print("\nFLAGS:")
        for f in flags:
            print(f"  [fix] {f}")
    # category totals
    cats = {}
    for e in reg["entries"]:
        cats[e.get("category") or "other"] = cats.get(e.get("category") or "other", 0) \
            + (e.get("price") or 0)
    if cats:
        print("\nBY CATEGORY:")
        for c, v in sorted(cats.items(), key=lambda x: -x[1]):
            print(f"  {c:<14}${v:,.0f}")


def cmd_claim(a):
    reg = load(a.file)
    e = need(reg, a.id)
    jur = a.jurisdiction or reg.get("jurisdiction") or "US"
    lys = layers_for(e, jur)
    live = [ly for ly in lys if ly["live"]]
    target = live[0] if live else None
    t = today()
    p = d(e["purchased"])
    age_mo = (t - p).days / 30.44
    print("=" * 68)
    print("WARRANTY / STATUTORY CLAIM LETTER — DRAFT (edit before sending)")
    print("=" * 68)
    print(f"""
[Your name]
[Your address]
Date: {t.isoformat()}

To: {target['counterparty'].upper() if target else '[COUNTERPARTY]'}

RE: {e.get('name')} ({e['id']}), purchased {e['purchased']} for
    ${e.get('price') or 0:,.0f}{'; serial ' + e['serial'] if e.get('serial') else ''}

On [date] the item developed the following fault:

    {a.fault or '[DESCRIBE FAULT: what happens, error codes, when it started]'}

The item has been used normally and maintained according to the manufacturer's
instructions, and the fault is not the result of misuse or accident.""")
    if target and "statutory" in target["name"]:
        if jur == "UK":
            print("""
Under the Consumer Rights Act 2015 (s.11–s.19), goods must be of satisfactory
quality and fit for purpose. """)
            if age_mo <= UK_BURDEN_MONTHS:
                print(f"""As the fault appeared within six months of delivery
(item age: {age_mo:.0f} months), it is presumed to have been present at the
time of sale and the burden of proof lies with you.""")
            else:
                print(f"""The nature of the fault indicates it was inherent at
the time of sale (item age: {age_mo:.0f} months); the defect is of a kind that
could not have arisen from normal use over this period.""")
            print("""
I request that you repair or replace the goods, or failing that, provide an
appropriate price reduction or refund.""")
        elif jur == "EU":
            print("""
Under the national implementation of Directive (EU) 2019/771, the goods do not
conform to the contract. I request repair or replacement within a reasonable
time and free of charge.""")
    elif target and "manufacturer" in target["name"]:
        print("""
This claim is made under the express manufacturer's warranty included with the
product. Please arrange inspection/repair under its terms.""")
    elif target and "plan" in target["name"]:
        print("""
This claim is made under the extended service plan referenced above. Please
advise the claim procedure and authorized service options.""")
    else:
        print("""
[Choose basis: express warranty / statutory rights / extended plan.]""")
    print(f"""
I expect a response within 14 days. This letter is sent in anticipation of
an amicable resolution; I reserve all rights.

Enclosures:
  - Proof of purchase ({e.get('receipt') or 'ATTACH: receipt/statement line'})
  - Photographs/video of the fault  [attach]
  - Serial number record{': ' + e['serial'] if e.get('serial') else '  [add]'}
{chr(10).join('  - ' + x for x in ['Registration confirmation'] if e.get('registered')) or ''}

CLAIM CHECKLIST BEFORE SENDING:
  [ ] Correct counterparty: {target['counterparty'] if target else '?'} (statutory = RETAILER)
  [ ] Fault described with dates, codes, photos
  [ ] Proof of purchase attached
  [ ] Sent in writing (email/portal) with delivery record
  [ ] 14-day calendar reminder set
""")
    if not live:
        print("[!] No live coverage found — consider recall check + repair quotes.")


def cmd_export(a):
    reg = load(a.file)
    print(json.dumps(reg, indent=2 if a.json else None))


def cmd_meta(a):
    reg = load(a.file)
    if a.jurisdiction:
        reg["jurisdiction"] = a.jurisdiction
    save(reg, a.file)


# --------------------------- cli -------------------------------------------
def main():
    p = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    def shared(sp):
        sp.add_argument("--file", default=DEFAULT_FILE, help="vault JSON path")

    sp = sub.add_parser("add", help="record a purchase")
    shared(sp)
    sp.add_argument("--id", required=True)
    sp.add_argument("--name")
    sp.add_argument("--category")
    sp.add_argument("--price", type=float, required=True)
    sp.add_argument("--purchased", required=True, help="YYYY-MM-DD")
    sp.add_argument("--warranty-mo", type=int, help="manufacturer warranty months")
    sp.add_argument("--receipt", help="where the receipt lives")
    sp.add_argument("--card", help=f"card used: {CARD_HINT}")
    sp.add_argument("--serial")
    sp.add_argument("--registered", help="YYYY-MM-DD registered with maker")
    sp.add_argument("--notes")
    sp.add_argument("--extended-mo", type=int)
    sp.add_argument("--extended-by")
    sp.add_argument("--extended-deductible", type=float)
    sp.add_argument("--jurisdiction", choices=JURISDICTIONS)
    sp.set_defaults(fn=cmd_add)

    sp = sub.add_parser("update", help="edit an entry")
    shared(sp)
    sp.add_argument("--id", required=True)
    for f in ("name", "category", "receipt", "card", "serial", "notes",
              "extended_by", "registered", "purchased"):
        sp.add_argument(f"--{f.replace('_', '-')}")
    for f in ("price", "warranty_mo", "extended_mo", "extended_deductible"):
        sp.add_argument(f"--{f.replace('_', '-')}", type=float)
    sp.add_argument("--mark-registered", action="store_true")
    sp.set_defaults(fn=cmd_update)

    sp = sub.add_parser("remove", help="delete an entry")
    shared(sp)
    sp.add_argument("--id", required=True)
    sp.set_defaults(fn=cmd_remove)

    sp = sub.add_parser("list", help="show the vault")
    shared(sp)
    sp.set_defaults(fn=cmd_list)

    sp = sub.add_parser("covered", help="what covers this item today")
    shared(sp)
    sp.add_argument("--id", required=True)
    sp.add_argument("--jurisdiction", choices=JURISDICTIONS)
    sp.set_defaults(fn=cmd_covered)

    sp = sub.add_parser("expiring", help="coverage ending soon")
    shared(sp)
    sp.add_argument("--days", type=int, default=90)
    sp.set_defaults(fn=cmd_expiring)

    sp = sub.add_parser("report", help="audit + totals")
    shared(sp)
    sp.add_argument("--jurisdiction", choices=JURISDICTIONS)
    sp.add_argument("--category")
    sp.add_argument("--json", action="store_true")
    sp.set_defaults(fn=cmd_report)

    sp = sub.add_parser("claim", help="draft a claim letter")
    shared(sp)
    sp.add_argument("--id", required=True)
    sp.add_argument("--fault", help="fault description")
    sp.add_argument("--jurisdiction", choices=JURISDICTIONS)
    sp.set_defaults(fn=cmd_claim)

    sp = sub.add_parser("export", help="dump vault JSON")
    shared(sp)
    sp.add_argument("--json", action="store_true")
    sp.set_defaults(fn=cmd_export)

    sp = sub.add_parser("meta", help="set default jurisdiction")
    shared(sp)
    sp.add_argument("--jurisdiction", choices=JURISDICTIONS)
    sp.set_defaults(fn=cmd_meta)

    a = p.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()
