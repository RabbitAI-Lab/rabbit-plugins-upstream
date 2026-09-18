"""Country-of-origin gate — guarantee every supplier in the data is IRANIAN.

v2.11. The database has one hard scope rule: **only Iranian suppliers**. Before
v2.11 nothing enforced it. :mod:`src.discovery.validator` merely *added* points
for Iranian-looking signals, so a foreign vendor that happened to mention
"Tehran" scored 30/100, and the entire social/Telegram path had no country
check at all. This module is the single enforcement point for both paths.

Design (from country-of-origin verification best practice)
----------------------------------------------------------
1. **Never single-source.** ccTLD is the strongest single signal but is neither
   necessary nor sufficient: 28 of our 35 seeded Iranian suppliers trade on
   ``.com``. A lone signal is therefore never enough to admit a supplier.
2. **Cross-reference >= 2 independent signals.** Independence matters: a ``.ir``
   domain and an Iranian IP are largely the same fact (Iranian hosting), so
   signals are grouped into *families* and only distinct families count.
3. **Default deny.** Insufficient evidence => ``REJECT``, never "probably fine".
   An unreachable site yields no evidence and so cannot be admitted.
4. **Disqualifying signals override everything.** Positive evidence cannot
   rescue a vendor that states a foreign HQ or is a known multinational.
5. **Auditable provenance.** Every verdict carries the evidence that produced
   it, each with source, matched value and confidence, plus a timestamp.

The brand-vs-supplier distinction (the subtle part)
---------------------------------------------------
Iranian lab-reagent vendors are overwhelmingly **importers**: they resell
Merck, Sigma-Aldrich, TCI and Gibco product. Their pages and posts are dense
with foreign brand names, foreign country-of-manufacture strings ("ساخت
آلمان" / "Made in Germany") and foreign catalogue numbers. Treating those as
foreign-origin evidence would wrongly delete the most valuable Iranian
suppliers in the dataset -- e.g. the Telegram channel ``merckmillipore`` is NOT
Merck KGaA, it is a Tehran importer (bio: "واردات مرك به صورت عمده", mobile
09121161187) that brand-squats the name.

So this module scores the **supplier entity**, never the goods:

  * foreign *brand* / country-of-manufacture mentions are recorded as
    :data:`BRAND_ORIGIN_CONTEXT` and explicitly do NOT count against a vendor;
  * a foreign HQ *statement about the vendor itself* ("headquartered in",
    "our head office in Darmstadt") IS disqualifying;
  * ownership of a known multinational's own domain/handle IS disqualifying.

Downstream consumers must present foreign brands as product metadata
(``brand``), never as a supplier country.
"""
from __future__ import annotations

import ipaddress
import re
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Dict, List, Optional
from urllib.parse import urlparse

IRAN = "IR"

# ---------------------------------------------------------------------------
# Signal families. Two signals only corroborate each other when their families
# differ, so "domain + hosting" (one underlying fact) can never admit a vendor.
# ---------------------------------------------------------------------------
FAMILY_DOMAIN = "domain"
FAMILY_TRUSTMARK = "trustmark"
FAMILY_REGISTRY = "registry"
FAMILY_PHONE = "phone"
FAMILY_ADDRESS = "address"
FAMILY_CURRENCY = "currency"
FAMILY_LANGUAGE = "language"
FAMILY_HOSTING = "hosting"

# Weight per SIGNAL, not merely per family: an explicit "+98 21 …" number is
# stronger proof than a bare "09xx" mobile, and a city+country pair is stronger
# than the word "Iran" alone. Aggregation takes the MAX weight within a family
# so repeating one kind of evidence can never inflate a score.
SIGNAL_WEIGHT: Dict[str, int] = {
    # trustmark / registry — state-verified identity
    "enamad": 50,           # Enamad: state-verified identity AND address
    "shenase_melli": 45,    # شناسه ملی — legal-entity national ID
    "code_eghtesadi": 45,   # کد اقتصادی
    "kod_posti": 35,        # کد پستی — 10-digit Iranian postal code
    "shomare_sabt": 35,     # شماره ثبت — company registration number
    # domain
    "cctld": 40,            # .ir / ایران.
    # phone
    "phone_+98": 35,        # explicit international dialling code
    "phone_landline": 30,   # 021/031/051… geographic prefix
    "phone_09xx": 30,       # Iranian mobile prefix
    "phone_fa_digits": 25,  # Persian-digit phone form
    # address
    "city+country": 30,     # Iranian city AND the country named
    "city_or_country": 15,  # one of the two — weak on its own
    # commerce / content
    "irr_pricing": 20,      # ریال / تومان
    "persian_content": 10,  # Persian is used beyond Iran — weak
    "iran_ip": 10,          # supporting evidence only, never decisive
}

#: Fallback when a signal has no explicit weight.
DEFAULT_SIGNAL_WEIGHT = 10

# Retained for backwards compatibility / reporting.
FAMILY_WEIGHT: Dict[str, int] = {
    FAMILY_TRUSTMARK: 50, FAMILY_REGISTRY: 45, FAMILY_DOMAIN: 40,
    FAMILY_PHONE: 35, FAMILY_ADDRESS: 30, FAMILY_CURRENCY: 20,
    FAMILY_LANGUAGE: 10, FAMILY_HOSTING: 10,
}


def score_evidence(evidence: List["Evidence"]) -> int:
    """Total weight = sum over families of the STRONGEST signal in each."""
    best: Dict[str, int] = {}
    for e in evidence:
        w = SIGNAL_WEIGHT.get(e.signal, DEFAULT_SIGNAL_WEIGHT)
        if w > best.get(e.family, 0):
            best[e.family] = w
    return sum(best.values())

ADMIT_SCORE = 60
ADMIT_FAMILIES = 2

# ---------------------------------------------------------------------------
# Positive Iranian signals
# ---------------------------------------------------------------------------
RE_ENAMAD = re.compile(r"(enamad\.ir|trustseal\.enamad|نماد اعتماد|رسانه‌?های دیجیتال)", re.I)
# شناسه ملی = 11 digits, کد اقتصادی = 12-14 digits, کد پستی = 10 digits.
RE_NATIONAL_ID = re.compile(r"(شناسه\s*ملی|شناسه\s*ملى)\D{0,20}(\d[\d\s\-]{9,15}\d)")
RE_ECONOMIC_CODE = re.compile(r"(کد\s*اقتصادی|كد\s*اقتصادى)\D{0,20}(\d[\d\s\-]{10,17}\d)")
RE_POSTAL_CODE = re.compile(r"(کد\s*پستی|كد\s*پستى)\D{0,20}(\d[\d\s\-]{8,14}\d)")
RE_REGISTRY_NUM = re.compile(r"(شماره\s*ثبت|ثبت\s*شرکت)\D{0,20}(\d{3,8})")

# +98 / 0098 international form, Iranian mobile 09xx, Tehran-style landlines.
RE_PHONE_INTL = re.compile(r"(?:\+\s?98|0098)[\s\-()]?\d{2,3}[\s\-()]?\d{3,4}[\s\-]?\d{4}")
RE_PHONE_MOBILE = re.compile(r"(?<!\d)09\d{2}[\s\-]?\d{3}[\s\-]?\d{4}(?!\d)")
RE_PHONE_LANDLINE = re.compile(r"(?<!\d)0(?:21|26|31|41|51|61|71|13|24|28|34|38|45|56|66|77|83|85|86|87)[\s\-]?\d{7,8}(?!\d)")
# Persian-digit phone forms (۰۲۱ / ۰۹۱۲ ...).
RE_PHONE_FA = re.compile(r"[۰-۹]{4}[\s\-]?[۰-۹]{3}[\s\-]?[۰-۹]{4}|۰(?:۲۱|۳۱|۵۱)[\s\-]?[۰-۹]{7,8}")

IRAN_CITIES = (
    r"Tehran|Isfahan|Esfahan|Karaj|Mashhad|Tabriz|Shiraz|Qom|Ahvaz|Kermanshah|Urmia|"
    r"Rasht|Zahedan|Hamadan|Kerman|Yazd|Ardabil|Bandar Abbas|Arak|Qazvin|Sanandaj|"
    r"تهران|اصفهان|کرج|مشهد|تبریز|شیراز|قم|اهواز|کرمانشاه|ارومیه|رشت|همدان|کرمان|"
    r"یزد|اردبیل|بندرعباس|اراک|قزوین|سنندج|زنجان|ساوه|شهرک صنعتی"
)
RE_IRAN_CITY = re.compile(IRAN_CITIES, re.I)
RE_IRAN_COUNTRY = re.compile(r"\b(Iran|Islamic Republic of Iran|I\.?R\.?\s?Iran)\b|ایران|ايران", re.I)
RE_CURRENCY = re.compile(r"(ریال|ريال|تومان|تومن|\bIRR\b|\brial\b|\btoman\b)", re.I)
RE_PERSIAN = re.compile(r"[\u0600-\u06FF]")

# ---------------------------------------------------------------------------
# Disqualifying (foreign) signals — these VETO admission.
# ---------------------------------------------------------------------------
# Foreign ccTLDs we may plausibly meet. Excludes .ir obviously; gTLDs (.com,
# .net, .org) are country-neutral and are NOT listed.
FOREIGN_CCTLDS = {
    "de": "DE", "cn": "CN", "in": "IN", "tr": "TR", "ae": "AE", "us": "US",
    "uk": "GB", "fr": "FR", "it": "IT", "es": "ES", "nl": "NL", "be": "BE",
    "ch": "CH", "at": "AT", "se": "SE", "no": "NO", "dk": "DK", "fi": "FI",
    "pl": "PL", "cz": "CZ", "ru": "RU", "ua": "UA", "jp": "JP", "kr": "KR",
    "sg": "SG", "my": "MY", "th": "TH", "id": "ID", "pk": "PK", "sa": "SA",
    "qa": "QA", "kw": "KW", "om": "OM", "bh": "BH", "iq": "IQ", "az": "AZ",
    "am": "AM", "ge": "GE", "af": "AF", "tm": "TM", "ca": "CA", "au": "AU",
    "br": "BR", "mx": "MX", "za": "ZA", "eg": "EG", "il": "IL", "gr": "GR",
    "pt": "PT", "ro": "RO", "hu": "HU", "bg": "BG", "hk": "HK", "tw": "TW",
}

# Domains/handles owned by multinationals. A vendor operating ON these is the
# multinational itself, not an Iranian reseller. Matched on registrable domain.
MULTINATIONAL_DOMAINS = {
    "merckmillipore.com": "DE", "merckgroup.com": "DE", "merck.com": "US",
    "sigmaaldrich.com": "US", "emdmillipore.com": "DE", "milliporesigma.com": "US",
    "thermofisher.com": "US", "fishersci.com": "US", "lifetechnologies.com": "US",
    "vwr.com": "US", "avantorsciences.com": "US", "honeywell.com": "US",
    "tcichemicals.com": "JP", "wako-chem.co.jp": "JP", "kanto.co.jp": "JP",
    "alfa.com": "US", "alfaaesar.com": "US", "acros.com": "BE",
    "carlroth.com": "DE", "roth.de": "DE", "applichem.com": "DE",
    "bdh.com": "GB", "fluka.com": "CH", "riedeldehaen.com": "DE",
    "basf.com": "DE", "bayer.com": "DE", "evonik.com": "DE", "clariant.com": "CH",
    "dow.com": "US", "dupont.com": "US", "solvay.com": "BE", "arkema.com": "FR",
    "lanxess.com": "DE", "wacker.com": "DE", "ineos.com": "GB",
    "sabic.com": "SA", "qapco.com": "QA", "borouge.com": "AE",
    "lgchem.com": "KR", "mitsuichem.com": "JP", "sinopec.com": "CN",
    "chemicalbook.com": "CN", "lookchem.com": "CN", "made-in-china.com": "CN",
    "alibaba.com": "CN", "1688.com": "CN", "echemi.com": "CN",
    "gelest.com": "US", "strem.com": "US", "cayman-chem.com": "US",
    "biorad.com": "US", "qiagen.com": "DE", "roche.com": "CH",
    "agilent.com": "US", "waters.com": "US", "shimadzu.com": "JP",
    "restek.com": "US", "supelco.com": "US", "hach.com": "US",
    "labshop.nl": "NL",
}

# Statements about the VENDOR's own seat. Deliberately narrow: they must bind a
# HQ verb to a place, so a product's "Made in Germany" never matches.
RE_FOREIGN_HQ = re.compile(
    r"(?:head\s?quarter(?:s|ed)?|head\s?office|registered\s+office|"
    r"our\s+(?:head\s?office|headquarters)|based\s+in|incorporated\s+in|"
    r"a\s+company\s+registered\s+in)"
    r"[^.\n]{0,40}?\b("
    r"Germany|Darmstadt|USA|United States|China|Shanghai|Beijing|India|Mumbai|"
    r"Turkey|Istanbul|UAE|Dubai|Sharjah|United Kingdom|England|London|France|Paris|"
    r"Italy|Milan|Spain|Netherlands|Amsterdam|Rotterdam|Switzerland|Zurich|Basel|"
    r"Japan|Tokyo|Osaka|Korea|Seoul|Singapore|Malaysia|Kuala Lumpur|Russia|Moscow|"
    r"Canada|Australia|Brazil|Saudi Arabia|Riyadh|Qatar|Doha|Kuwait|Iraq|Baghdad|"
    r"Azerbaijan|Baku|Pakistan|Karachi|Belgium|Austria|Vienna|Sweden|Poland"
    r")\b",
    re.I,
)

# Foreign phone country codes seen as the vendor's OWN contact number.
RE_FOREIGN_PHONE = re.compile(
    r"(?<![\d+])\+(?:"
    r"49|1|86|91|90|971|44|33|39|34|31|32|41|43|46|47|45|358|48|420|7|81|82|65|60|66|62|92|966|974|965|968|973|964|994|374|995|93|993|61|55|52|27|20|972|30|351|40|36|359|852|886"
    r")[\s\-()]?\d{6,14}"
)

# Foreign-only currency pricing (no IRR anywhere) is a weak foreign hint. It is
# NOT disqualifying on its own: Iranian exporters quote USD/EUR routinely.
RE_FOREIGN_CURRENCY = re.compile(r"(\bUSD\b|\bEUR\b|\bGBP\b|\bAED\b|\bCNY\b|\bTRY\b|€|£|\$)")

# Context that explains foreign words WITHOUT implying a foreign supplier.
BRAND_ORIGIN_CONTEXT = re.compile(
    r"(made\s+in|country\s+of\s+origin|origin\s*:|manufactured\s+by|brand\s*:|"
    r"ساخت|ساخت\s+کشور|کشور\s+سازنده|برند|مارک|تولید\s+کشور|اصل\s+آلمان|"
    r"وارداتی|واردات|وارد\s*کننده|وارد\s+کننده|نمایندگی|توزیع\s*کننده)",
    re.I,
)

IRAN_IP_CIDRS = (
    "2.144.0.0/14", "5.22.0.0/17", "5.52.0.0/16", "5.62.160.0/19", "5.116.0.0/14",
    "5.144.128.0/19", "5.160.0.0/16", "5.198.160.0/19", "5.200.64.0/18",
    "5.232.0.0/14", "5.234.128.0/19", "31.2.128.0/17", "31.14.80.0/20",
    "31.24.200.0/21", "31.47.32.0/19", "31.56.0.0/14", "31.170.48.0/20",
    "37.32.0.0/19", "37.98.0.0/16", "37.114.192.0/18", "37.129.0.0/16",
    "37.148.0.0/17", "37.156.0.0/18", "37.191.64.0/18", "37.202.128.0/17",
    "37.228.132.0/22", "37.235.16.0/20", "37.254.0.0/15", "46.18.248.0/21",
    "46.32.0.0/19", "46.36.96.0/20", "46.51.0.0/18", "46.100.0.0/16",
    "46.102.120.0/21", "46.143.0.0/18", "46.148.32.0/19", "46.164.128.0/18",
    "46.167.128.0/19", "46.209.0.0/16", "46.224.0.0/15", "46.245.0.0/18",
    "62.32.0.0/18", "62.60.128.0/17", "62.102.128.0/19", "62.193.0.0/19",
    "62.220.96.0/19", "77.36.128.0/17", "77.81.64.0/19", "77.104.64.0/18",
    "77.237.64.0/19", "78.38.0.0/15", "78.109.192.0/20", "78.111.0.0/20",
    "78.157.32.0/19", "79.127.0.0/17", "79.132.192.0/19", "79.175.128.0/18",
    "80.66.176.0/20", "80.191.0.0/16", "80.210.0.0/16", "80.242.0.0/20",
    "80.253.128.0/19", "81.12.0.0/17", "81.16.112.0/20", "81.28.32.0/19",
    "81.31.160.0/19", "81.90.144.0/20", "81.91.128.0/18", "82.99.192.0/18",
    "83.121.0.0/18", "83.147.192.0/18", "84.241.0.0/18", "85.9.64.0/18",
    "85.15.0.0/18", "85.132.192.0/18", "85.133.128.0/17", "85.185.0.0/16",
    "85.198.0.0/19", "86.104.32.0/19", "86.105.128.0/19", "86.106.192.0/19",
    "86.107.0.0/19", "86.109.32.0/19", "87.107.0.0/16", "87.236.208.0/20",
    "87.247.160.0/19", "87.248.128.0/18", "88.135.32.0/19", "89.32.0.0/19",
    "89.34.128.0/19", "89.36.96.0/19", "89.37.0.0/19", "89.39.208.0/20",
    "89.42.192.0/19", "89.144.128.0/19", "89.165.0.0/18", "89.196.0.0/16",
    "89.219.192.0/18", "89.221.80.0/20", "89.235.64.0/18", "91.92.104.0/21",
    "91.98.0.0/15", "91.106.64.0/19", "91.108.128.0/18", "91.184.64.0/19",
    "91.186.192.0/19", "91.192.10.0/24", "91.199.9.0/24", "91.208.166.0/24",
    "91.212.252.0/24", "91.213.36.0/24", "91.220.16.0/24", "91.222.204.0/24",
    "91.225.52.0/22", "91.227.71.0/24", "91.228.196.0/22", "91.229.214.0/24",
    "91.239.202.0/24", "91.240.180.0/22", "91.243.84.0/22", "91.245.228.0/22",
    "92.42.48.0/21", "92.50.0.0/18", "92.61.176.0/20", "92.114.16.0/20",
    "92.242.192.0/19", "93.110.0.0/16", "93.113.224.0/19", "93.115.144.0/20",
    "93.117.32.0/19", "93.126.0.0/18", "94.24.32.0/19", "94.74.128.0/17",
    "94.101.128.0/19", "94.176.4.0/22", "94.182.0.0/15", "94.184.0.0/16",
    "94.199.128.0/19", "94.232.168.0/21", "95.38.0.0/16", "95.64.0.0/18",
    "95.80.128.0/19", "95.81.64.0/18", "95.156.224.0/19", "95.162.0.0/16",
    "95.181.128.0/19", "95.215.60.0/22", "109.74.224.0/19", "109.94.160.0/19",
    "109.107.128.0/19", "109.110.160.0/19", "109.122.192.0/18", "109.125.128.0/18",
    "109.162.128.0/17", "109.201.0.0/18", "109.203.128.0/18", "109.206.240.0/20",
    "109.230.192.0/19", "109.238.176.0/20", "128.65.176.0/22", "146.66.32.0/21",
    "149.11.16.0/20", "151.232.0.0/14", "151.236.24.0/21", "151.238.0.0/16",
    "151.240.0.0/13", "158.58.184.0/21", "158.255.74.0/23", "164.138.128.0/18",
    "176.12.64.0/19", "176.31.0.0/17", "176.56.144.0/20", "176.65.192.0/19",
    "176.99.0.0/19", "176.101.48.0/20", "176.102.216.0/21", "176.221.64.0/19",
    "176.223.80.0/20", "178.21.20.0/22", "178.22.72.0/21", "178.63.0.0/17",
    "178.131.0.0/16", "178.157.0.0/19", "178.169.0.0/17", "178.173.128.0/17",
    "178.215.128.0/19", "178.216.248.0/21", "178.236.32.0/19", "178.239.144.0/20",
    "178.251.208.0/20", "178.252.128.0/19", "178.253.32.0/19", "185.1.72.0/24",
    "185.2.12.0/22", "185.4.28.0/22", "185.8.172.0/22", "185.11.68.0/22",
    "185.12.100.0/22", "185.13.228.0/22", "185.14.160.0/22", "185.16.60.0/22",
    "185.18.156.0/22", "185.19.100.0/22", "185.20.160.0/22", "185.22.28.0/22",
    "185.23.128.0/22", "185.24.104.0/22", "185.26.236.0/22", "185.27.132.0/22",
    "185.28.60.0/22", "185.30.176.0/22", "185.32.128.0/22", "185.33.24.0/22",
    "185.34.48.0/22", "185.36.100.0/22", "185.37.52.0/22", "185.38.152.0/22",
    "185.39.32.0/22", "185.40.20.0/22", "185.41.192.0/22", "185.42.212.0/22",
    "185.43.212.0/22", "185.44.36.0/22", "185.45.192.0/22", "185.46.96.0/22",
    "185.47.232.0/22", "185.48.180.0/22", "185.49.84.0/22", "185.50.36.0/22",
    "185.51.200.0/22", "185.52.84.0/22", "185.53.8.0/22", "185.55.224.0/22",
    "185.56.28.0/22", "185.57.152.0/22", "185.58.116.0/22", "185.59.100.0/22",
    "185.60.32.0/22", "185.61.140.0/22", "185.62.236.0/22", "185.63.100.0/22",
    "185.64.176.0/22", "185.65.100.0/22", "185.66.76.0/22", "185.67.156.0/22",
    "185.68.20.0/22", "185.69.56.0/22", "185.70.108.0/22", "185.71.116.0/22",
    "185.72.4.0/22", "185.73.148.0/22", "185.74.20.0/22", "185.75.204.0/22",
    "185.76.104.0/22", "185.77.216.0/22", "185.78.20.0/22", "185.79.156.0/22",
    "185.80.196.0/22", "185.81.96.0/22", "185.82.20.0/22", "185.83.112.0/22",
    "185.84.4.0/22", "185.85.180.0/22", "185.86.180.0/22", "185.88.152.0/22",
    "185.89.112.0/22", "185.90.104.0/22", "185.91.196.0/22", "185.92.4.0/22",
    "185.94.96.0/22", "185.95.24.0/22", "185.96.0.0/22", "185.97.116.0/22",
    "185.98.112.0/22", "185.99.212.0/22", "185.100.40.0/22", "185.101.104.0/22",
    "185.102.192.0/22", "185.103.128.0/22", "185.104.180.0/22", "185.105.100.0/22",
    "185.106.216.0/22", "185.107.184.0/22", "185.108.156.0/22", "185.109.60.0/22",
    "185.110.180.0/22", "185.111.184.0/22", "185.112.32.0/22", "185.113.56.0/22",
    "185.114.4.0/22", "185.115.72.0/22", "185.116.160.0/22", "185.117.204.0/22",
    "185.118.152.0/22", "185.119.212.0/22", "185.120.196.0/22", "185.121.128.0/22",
    "185.126.200.0/22", "185.129.168.0/22", "185.130.76.0/22", "185.131.84.0/22",
    "185.132.36.0/22", "185.133.16.0/22", "185.134.20.0/22", "185.135.228.0/22",
    "185.136.148.0/22", "185.137.144.0/22", "185.138.168.0/22", "185.139.72.0/22",
    "185.140.64.0/22", "185.141.36.0/22", "185.142.156.0/22", "185.143.232.0/22",
    "185.144.12.0/22", "185.145.8.0/22", "185.146.24.0/22", "185.147.16.0/22",
    "185.148.4.0/22", "185.149.72.0/22", "185.150.64.0/22", "185.151.24.0/22",
    "185.152.64.0/22", "185.153.208.0/22", "185.154.72.0/22", "185.155.72.0/22",
    "185.156.172.0/22", "185.157.4.0/22", "185.158.156.0/22", "185.159.152.0/22",
    "185.160.104.0/22", "185.161.112.0/22", "185.162.232.0/22", "185.163.116.0/22",
    "185.164.72.0/22", "185.165.40.0/22", "185.166.104.0/22", "185.167.100.0/22",
    "185.168.180.0/22", "185.169.16.0/22", "185.170.236.0/22", "185.171.52.0/22",
    "185.172.68.0/22", "185.173.104.0/22", "185.174.176.0/22", "185.175.204.0/22",
    "185.176.220.0/22", "185.177.152.0/22", "185.178.72.0/22", "185.179.176.0/22",
    "185.180.196.0/22", "185.181.180.0/22", "185.182.180.0/22", "185.183.128.0/22",
    "185.184.32.0/22", "185.185.36.0/22", "185.186.240.0/22", "185.187.48.0/22",
    "185.188.24.0/22", "185.189.192.0/22", "185.190.104.0/22", "185.191.76.0/22",
    "185.192.112.0/22", "185.193.124.0/22", "185.194.24.0/22", "185.195.24.0/22",
    "185.196.208.0/22", "185.197.144.0/22", "185.198.72.0/22", "185.199.72.0/22",
    "185.200.104.0/22", "185.201.96.0/22", "185.202.20.0/22", "185.203.72.0/22",
    "185.204.168.0/22", "185.205.176.0/22", "185.206.92.0/22", "185.207.100.0/22",
    "185.208.172.0/22", "185.209.152.0/22", "185.210.92.0/22", "185.211.56.0/22",
    "185.212.48.0/22", "185.213.164.0/22", "185.214.104.0/22", "185.215.228.0/22",
    "185.216.132.0/22", "185.217.28.0/22", "185.218.132.0/22", "185.219.132.0/22",
    "185.220.228.0/22", "185.221.184.0/22", "185.222.116.0/22", "185.223.100.0/22",
    "185.224.16.0/22", "185.225.16.0/22", "185.226.116.0/22", "185.227.112.0/22",
    "185.228.236.0/22", "185.229.52.0/22", "185.230.100.0/22", "185.231.180.0/22",
    "185.232.176.0/22", "185.233.16.0/22", "185.234.12.0/22", "185.235.132.0/22",
    "185.236.36.0/22", "185.237.12.0/22", "185.238.72.0/22", "185.239.104.0/22",
    "185.240.56.0/22", "185.241.100.0/22", "185.242.180.0/22", "185.243.48.0/22",
    "185.244.128.0/22", "185.245.84.0/22", "185.246.84.0/22", "185.247.72.0/22",
    "185.248.128.0/22", "185.249.100.0/22", "185.250.60.0/22", "185.251.24.0/22",
    "185.252.28.0/22", "185.253.128.0/22", "185.254.28.0/22", "185.255.84.0/22",
    "188.0.240.0/20", "188.34.0.0/17", "188.40.0.0/17", "188.75.64.0/18",
    "188.93.224.0/20", "188.121.96.0/19", "188.136.128.0/17", "188.158.0.0/15",
    "188.208.192.0/19", "188.209.48.0/20", "188.211.128.0/18", "188.212.64.0/18",
    "188.213.64.0/18", "188.229.0.0/17", "188.240.192.0/18", "188.253.0.0/18",
    "193.176.240.0/22", "193.176.244.0/22", "194.5.188.0/22", "194.9.68.0/22",
    "194.60.216.0/21", "194.104.184.0/22", "194.146.152.0/22", "194.225.0.0/16",
    "195.146.32.0/19", "195.181.208.0/20", "195.191.0.0/19", "195.211.240.0/22",
    "195.214.192.0/19", "195.219.216.0/21", "195.229.0.0/17", "212.16.64.0/19",
    "212.33.192.0/19", "212.80.0.0/19", "212.120.144.0/20", "212.146.0.0/17",
    "212.183.128.0/19", "213.109.192.0/19", "213.176.0.0/17", "213.195.0.0/18",
    "213.207.192.0/19", "213.217.32.0/19", "213.233.160.0/19", "217.11.16.0/20",
    "217.24.144.0/20", "217.60.0.0/16", "217.66.192.0/19", "217.79.128.0/19",
    "217.144.104.0/21", "217.146.208.0/20", "217.164.0.0/16", "217.171.144.0/20",
    "217.174.16.0/20", "217.196.0.0/19", "217.198.128.0/19", "217.218.0.0/15",
    "217.219.0.0/16",
)


@dataclass
class Evidence:
    """One auditable country signal."""
    family: str
    signal: str
    value: str
    country: str
    confidence: str  # high | medium | low
    source: str

    def as_dict(self) -> dict:
        return {
            "family": self.family, "signal": self.signal, "value": self.value,
            "country": self.country, "confidence": self.confidence, "source": self.source,
        }


@dataclass
class CountryVerdict:
    """Result of the gate. ``admitted`` is the only thing callers must obey."""
    admitted: bool
    country: Optional[str]
    score: int
    families: List[str] = field(default_factory=list)
    evidence: List[Evidence] = field(default_factory=list)
    disqualifiers: List[Evidence] = field(default_factory=list)
    reason: str = ""
    confidence: str = "low"
    verified_at: str = ""

    def as_dict(self) -> dict:
        return {
            "admitted": self.admitted,
            "country": self.country,
            "country_confidence": self.confidence,
            "score": self.score,
            "families": sorted(self.families),
            "reason": self.reason,
            "country_evidence": [e.as_dict() for e in self.evidence],
            "disqualifiers": [d.as_dict() for d in self.disqualifiers],
            "verified_at": self.verified_at,
        }


def registrable_domain(host: str) -> str:
    """Best-effort registrable domain (no PSL dependency, handles .co.ir etc.)."""
    host = (host or "").strip().lower()
    if "//" in host:
        host = urlparse(host).netloc or urlparse(host).path
    host = host.split("/")[0].split(":")[0]
    if host.startswith("www."):
        host = host[4:]
    parts = [p for p in host.split(".") if p]
    if len(parts) <= 2:
        return ".".join(parts)
    second_level = {"co", "ac", "gov", "org", "net", "com", "sch", "id"}
    if parts[-2] in second_level and len(parts) >= 3:
        return ".".join(parts[-3:])
    return ".".join(parts[-2:])


def _strip_brand_context(text: str) -> str:
    """Neutralise foreign words that describe the GOODS, not the vendor.

    Any line carrying an import/brand/origin marker is removed before foreign
    detection, so "ساخت آلمان" or "Made in Germany, imported by us" on an
    Iranian importer's page cannot produce a foreign disqualifier.
    """
    kept = []
    for line in (text or "").splitlines():
        if BRAND_ORIGIN_CONTEXT.search(line):
            continue
        kept.append(line)
    return "\n".join(kept)


def collect_evidence(*, url: str = "", content: str = "", ip: str = "",
                     source: str = "web") -> List[Evidence]:
    """Gather every positive Iranian signal available. No judgement here."""
    ev: List[Evidence] = []
    host = ""
    if url:
        parsed = urlparse(url if "//" in url else "http://" + url)
        host = (parsed.netloc or parsed.path).lower().split("/")[0]

    if host.endswith(".ir") or host.endswith(".ایران") or ".ir:" in host:
        ev.append(Evidence(FAMILY_DOMAIN, "cctld", host, IRAN, "high", source))

    text = content or ""
    if text:
        m = RE_ENAMAD.search(text)
        if m:
            ev.append(Evidence(FAMILY_TRUSTMARK, "enamad", m.group(0)[:60], IRAN, "high", source))
        for rx, name in ((RE_NATIONAL_ID, "shenase_melli"),
                         (RE_ECONOMIC_CODE, "code_eghtesadi"),
                         (RE_POSTAL_CODE, "kod_posti"),
                         (RE_REGISTRY_NUM, "shomare_sabt")):
            m = rx.search(text)
            if m:
                ev.append(Evidence(FAMILY_REGISTRY, name, m.group(0)[:60], IRAN, "high", source))
                break
        for rx, name, conf in ((RE_PHONE_INTL, "phone_+98", "high"),
                               (RE_PHONE_MOBILE, "phone_09xx", "medium"),
                               (RE_PHONE_LANDLINE, "phone_landline", "medium"),
                               (RE_PHONE_FA, "phone_fa_digits", "medium")):
            m = rx.search(text)
            if m:
                ev.append(Evidence(FAMILY_PHONE, name, m.group(0)[:40], IRAN, conf, source))
                break
        city = RE_IRAN_CITY.search(text)
        country = RE_IRAN_COUNTRY.search(text)
        if city and country:
            ev.append(Evidence(FAMILY_ADDRESS, "city+country",
                               f"{city.group(0)}/{country.group(0)}", IRAN, "medium", source))
        elif city or country:
            ev.append(Evidence(FAMILY_ADDRESS, "city_or_country",
                               (city or country).group(0), IRAN, "low", source))
        m = RE_CURRENCY.search(text)
        if m:
            ev.append(Evidence(FAMILY_CURRENCY, "irr_pricing", m.group(0), IRAN, "medium", source))
        fa = len(RE_PERSIAN.findall(text))
        if fa >= 50 and fa / max(len(text), 1) > 0.02:
            ev.append(Evidence(FAMILY_LANGUAGE, "persian_content", f"{fa} chars",
                               IRAN, "low", source))

    if ip and is_iranian_ip(ip):
        ev.append(Evidence(FAMILY_HOSTING, "iran_ip", ip, IRAN, "low", source))
    return ev


def collect_disqualifiers(*, url: str = "", content: str = "",
                          source: str = "web") -> List[Evidence]:
    """Gather foreign-supplier signals that VETO admission."""
    dq: List[Evidence] = []
    host = ""
    if url:
        parsed = urlparse(url if "//" in url else "http://" + url)
        host = (parsed.netloc or parsed.path).lower().split("/")[0]
    dom = registrable_domain(host) if host else ""

    if dom and dom in MULTINATIONAL_DOMAINS:
        dq.append(Evidence(FAMILY_DOMAIN, "multinational_domain", dom,
                           MULTINATIONAL_DOMAINS[dom], "high", source))
    if host:
        tld = host.rsplit(".", 1)[-1]
        if tld in FOREIGN_CCTLDS:
            dq.append(Evidence(FAMILY_DOMAIN, "foreign_cctld", host,
                               FOREIGN_CCTLDS[tld], "high", source))

    body = _strip_brand_context(content or "")
    if body:
        m = RE_FOREIGN_HQ.search(body)
        if m:
            dq.append(Evidence(FAMILY_ADDRESS, "foreign_hq_statement",
                               re.sub(r"\s+", " ", m.group(0))[:80],
                               "??", "high", source))
    return dq


def is_iranian_ip(host: str) -> bool:
    try:
        ip = ipaddress.ip_address(host)
    except ValueError:
        return False
    return any(ip in ipaddress.ip_network(c) for c in IRAN_IP_CIDRS)


def evaluate(*, url: str = "", content: str = "", ip: str = "",
             source: str = "web", name: str = "") -> CountryVerdict:
    """Decide whether an entity may enter the database. Default: DENY.

    Admission requires ALL of:
      * zero disqualifiers;
      * >= :data:`ADMIT_FAMILIES` independent signal families;
      * total weight >= :data:`ADMIT_SCORE`.
    """
    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    haystack = "\n".join(x for x in (name, content) if x)
    ev = collect_evidence(url=url, content=haystack, ip=ip, source=source)
    dq = collect_disqualifiers(url=url, content=haystack, source=source)

    families = sorted({e.family for e in ev})
    score = score_evidence(ev)

    if dq:
        return CountryVerdict(False, dq[0].country, score, families, ev, dq,
                              reason=f"disqualified: {dq[0].signal}={dq[0].value}",
                              confidence="high", verified_at=now)
    if not ev:
        return CountryVerdict(False, None, 0, [], [], [],
                              reason="no country evidence (default deny)",
                              confidence="low", verified_at=now)
    if len(families) < ADMIT_FAMILIES:
        return CountryVerdict(False, None, score, families, ev, [],
                              reason=(f"insufficient corroboration: {len(families)} signal "
                                      f"family/families ({', '.join(families)}), need "
                                      f"{ADMIT_FAMILIES} independent"),
                              confidence="low", verified_at=now)
    if score < ADMIT_SCORE:
        return CountryVerdict(False, None, score, families, ev, [],
                              reason=f"evidence too weak: score {score} < {ADMIT_SCORE}",
                              confidence="low", verified_at=now)

    high = sum(1 for e in ev if e.confidence == "high")
    conf = "high" if (high >= 1 and score >= 80) else "medium"
    return CountryVerdict(True, IRAN, score, families, ev, [],
                          reason=f"verified Iranian: {len(families)} independent families, score {score}",
                          confidence=conf, verified_at=now)


def assert_iranian(**kwargs) -> CountryVerdict:
    """Strict helper: raise :class:`ForeignSupplierRejected` unless Iranian."""
    v = evaluate(**kwargs)
    if not v.admitted:
        raise ForeignSupplierRejected(v)
    return v


class ForeignSupplierRejected(Exception):
    def __init__(self, verdict: CountryVerdict):
        self.verdict = verdict
        super().__init__(f"supplier rejected — {verdict.reason}")
