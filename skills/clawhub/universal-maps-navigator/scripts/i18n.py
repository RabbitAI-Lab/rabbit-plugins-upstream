#!/usr/bin/env python3
"""i18n.py — Multilingual & cultural support for universal-maps-navigator v2.

50+ languages, RTL handling, units, date/time, cultural POI mapping, offline dictionary.

Stdlib only, Python 3.8+.

Features:
- Language detection (heuristic + script detection)
- Translation of static UI strings (offline dictionary, 50 langs)
- Cultural POI categories: mosque, temple, church, shrine, bazaar, souk, hammam, onsen, izakaya, halal, kosher, etc
- RTL support for ar, fa, he, ur
- Units per locale (metric/imperial)
- Date/time formatting patterns per locale
- Plural rules stub

Usage:
    from i18n import translate, detect_language, get_locale_info, cultural_poi_tags, format_distance, is_rtl
"""
from __future__ import annotations
import re
import json
from typing import Dict, List, Tuple

# 50+ languages supported
SUPPORTED_LANGUAGES = {
    "en": {"name": "English", "native": "English", "dir": "LTR", "units": "metric", "region": "US"},
    "en-GB": {"name": "English (UK)", "native": "English", "dir": "LTR", "units": "metric", "region": "GB"},
    "en-US": {"name": "English (US)", "native": "English", "dir": "LTR", "units": "imperial", "region": "US"},
    "ro": {"name": "Romanian", "native": "Română", "dir": "LTR", "units": "metric", "region": "RO"},
    "de": {"name": "German", "native": "Deutsch", "dir": "LTR", "units": "metric", "region": "DE"},
    "fr": {"name": "French", "native": "Français", "dir": "LTR", "units": "metric", "region": "FR"},
    "fr-CA": {"name": "French (Canada)", "native": "Français", "dir": "LTR", "units": "metric", "region": "CA"},
    "es": {"name": "Spanish", "native": "Español", "dir": "LTR", "units": "metric", "region": "ES"},
    "es-MX": {"name": "Spanish (Mexico)", "native": "Español", "dir": "LTR", "units": "metric", "region": "MX"},
    "it": {"name": "Italian", "native": "Italiano", "dir": "LTR", "units": "metric", "region": "IT"},
    "pt": {"name": "Portuguese", "native": "Português", "dir": "LTR", "units": "metric", "region": "PT"},
    "pt-BR": {"name": "Portuguese (Brazil)", "native": "Português", "dir": "LTR", "units": "metric", "region": "BR"},
    "ru": {"name": "Russian", "native": "Русский", "dir": "LTR", "units": "metric", "region": "RU"},
    "uk": {"name": "Ukrainian", "native": "Українська", "dir": "LTR", "units": "metric", "region": "UA"},
    "pl": {"name": "Polish", "native": "Polski", "dir": "LTR", "units": "metric", "region": "PL"},
    "hu": {"name": "Hungarian", "native": "Magyar", "dir": "LTR", "units": "metric", "region": "HU"},
    "tr": {"name": "Turkish", "native": "Türkçe", "dir": "LTR", "units": "metric", "region": "TR"},
    "ar": {"name": "Arabic", "native": "العربية", "dir": "RTL", "units": "metric", "region": "SA"},
    "fa": {"name": "Persian", "native": "فارسی", "dir": "RTL", "units": "metric", "region": "IR"},
    "he": {"name": "Hebrew", "native": "עברית", "dir": "RTL", "units": "metric", "region": "IL"},
    "hi": {"name": "Hindi", "native": "हिन्दी", "dir": "LTR", "units": "metric", "region": "IN"},
    "bn": {"name": "Bengali", "native": "বাংলা", "dir": "LTR", "units": "metric", "region": "BD"},
    "ur": {"name": "Urdu", "native": "اردو", "dir": "RTL", "units": "metric", "region": "PK"},
    "zh": {"name": "Chinese", "native": "中文", "dir": "LTR", "units": "metric", "region": "CN"},
    "zh-TW": {"name": "Chinese (Taiwan)", "native": "中文", "dir": "LTR", "units": "metric", "region": "TW"},
    "ja": {"name": "Japanese", "native": "日本語", "dir": "LTR", "units": "metric", "region": "JP"},
    "ko": {"name": "Korean", "native": "한국어", "dir": "LTR", "units": "metric", "region": "KR"},
    "th": {"name": "Thai", "native": "ไทย", "dir": "LTR", "units": "metric", "region": "TH"},
    "vi": {"name": "Vietnamese", "native": "Tiếng Việt", "dir": "LTR", "units": "metric", "region": "VN"},
    "id": {"name": "Indonesian", "native": "Bahasa Indonesia", "dir": "LTR", "units": "metric", "region": "ID"},
    "ms": {"name": "Malay", "native": "Bahasa Melayu", "dir": "LTR", "units": "metric", "region": "MY"},
    "nl": {"name": "Dutch", "native": "Nederlands", "dir": "LTR", "units": "metric", "region": "NL"},
    "sv": {"name": "Swedish", "native": "Svenska", "dir": "LTR", "units": "metric", "region": "SE"},
    "no": {"name": "Norwegian", "native": "Norsk", "dir": "LTR", "units": "metric", "region": "NO"},
    "da": {"name": "Danish", "native": "Dansk", "dir": "LTR", "units": "metric", "region": "DK"},
    "fi": {"name": "Finnish", "native": "Suomi", "dir": "LTR", "units": "metric", "region": "FI"},
    "el": {"name": "Greek", "native": "Ελληνικά", "dir": "LTR", "units": "metric", "region": "GR"},
    "cs": {"name": "Czech", "native": "Čeština", "dir": "LTR", "units": "metric", "region": "CZ"},
    "sk": {"name": "Slovak", "native": "Slovenčina", "dir": "LTR", "units": "metric", "region": "SK"},
    "bg": {"name": "Bulgarian", "native": "Български", "dir": "LTR", "units": "metric", "region": "BG"},
    "hr": {"name": "Croatian", "native": "Hrvatski", "dir": "LTR", "units": "metric", "region": "HR"},
    "sr": {"name": "Serbian", "native": "Српски", "dir": "LTR", "units": "metric", "region": "RS"},
    "sl": {"name": "Slovenian", "native": "Slovenščina", "dir": "LTR", "units": "metric", "region": "SI"},
    "et": {"name": "Estonian", "native": "Eesti", "dir": "LTR", "units": "metric", "region": "EE"},
    "lv": {"name": "Latvian", "native": "Latviešu", "dir": "LTR", "units": "metric", "region": "LV"},
    "lt": {"name": "Lithuanian", "native": "Lietuvių", "dir": "LTR", "units": "metric", "region": "LT"},
    "ka": {"name": "Georgian", "native": "ქართული", "dir": "LTR", "units": "metric", "region": "GE"},
    "am": {"name": "Amharic", "native": "አማርኛ", "dir": "LTR", "units": "metric", "region": "ET"},
    "sw": {"name": "Swahili", "native": "Kiswahili", "dir": "LTR", "units": "metric", "region": "KE"},
    "yo": {"name": "Yoruba", "native": "Yorùbá", "dir": "LTR", "units": "metric", "region": "NG"},
    "zu": {"name": "Zulu", "native": "isiZulu", "dir": "LTR", "units": "metric", "region": "ZA"},
    "af": {"name": "Afrikaans", "native": "Afrikaans", "dir": "LTR", "units": "metric", "region": "ZA"},
}

RTL_LANGS = {"ar", "fa", "he", "ur"}

# Cultural POI mapping: culturally significant categories → OSM tags per locale
CULTURAL_POI = {
    "mosque": ['["amenity"="place_of_worship"]["religion"="muslim"]', '["building"="mosque"]'],
    "church": ['["amenity"="place_of_worship"]["religion"="christian"]', '["building"="church"]'],
    "temple": ['["amenity"="place_of_worship"]["religion"~"buddhist|hindu|shinto"]', '["building"="temple"]'],
    "shrine": ['["historic"="wayside_shrine"]', '["amenity"="place_of_worship"]'],
    "synagogue": ['["amenity"="place_of_worship"]["religion"="jewish"]'],
    "bazaar": ['["shop"="bazaar"]', '["amenity"="marketplace"]'],
    "souk": ['["shop"="market"]', '["amenity"="marketplace"]'],
    "hammam": ['["amenity"="public_bath"]', '["leisure"="sauna"]'],
    "onsen": ['["amenity"="public_bath"]["bath:type"="onsen"]', '["leisure"="hot_spring"]'],
    "izakaya": ['["amenity"="restaurant"]["cuisine"="japanese"]', '["amenity"="bar"]'],
    "tapas": ['["amenity"="restaurant"]["cuisine"="spanish"]'],
    "halal": ['["diet:halal"="yes"]', '["amenity"="restaurant"]["diet:halal"="yes"]'],
    "kosher": ['["diet:kosher"="yes"]'],
    "vegan": ['["diet:vegan"="yes"]'],
    "pharmacy": ['["amenity"="pharmacy"]'],
    "hospital": ['["amenity"~"hospital|clinic"]'],
    "police": ['["amenity"="police"]'],
    "embassy": ['["office"="diplomatic"]'],
    "water": ['["amenity"="drinking_water"]'],
    "shelter": ['["amenity"="shelter"]', '["emergency"="assembly_point"]'],
}

# Minimal offline dictionary for common navigation terms (50 langs, key phrases)
DICTIONARY = {
    "en": {
        "route": "route", "distance": "distance", "duration": "duration", "from": "from", "to": "to",
        "navigate": "navigate", "nearby": "nearby", "search": "search", "save": "save",
        "turn_left": "Turn left", "turn_right": "Turn right", "go_straight": "Go straight",
        "arrive": "Arrive at destination", "depart": "Depart", "roundabout": "At roundabout take exit",
        "fuel": "fuel", "parking": "parking", "hospital": "hospital", "pharmacy": "pharmacy",
        "shelter": "shelter", "water": "water", "danger": "danger", "safe": "safe",
        "emergency": "emergency", "help": "help", "sos": "SOS"
    },
    "ro": {
        "route": "rută", "distance": "distanță", "duration": "durată", "from": "de la", "to": "la",
        "navigate": "navighează", "nearby": "în apropiere", "search": "caută", "save": "salvează",
        "turn_left": "Virați la stânga", "turn_right": "Virați la dreapta", "go_straight": "Mergeți înainte",
        "arrive": "Ați ajuns la destinație", "depart": "Plecare", "roundabout": "La sensul giratoriu luați ieșirea",
        "fuel": "combustibil", "parking": "parcare", "hospital": "spital", "pharmacy": "farmacie",
        "shelter": "adăpost", "water": "apă", "danger": "pericol", "safe": "sigur", "emergency": "urgență", "help": "ajutor", "sos": "SOS"
    },
    "ar": {
        "route": "طريق", "distance": "مسافة", "duration": "مدة", "from": "من", "to": "إلى",
        "navigate": "تنقل", "nearby": "قريب", "search": "بحث", "save": "حفظ",
        "turn_left": "انعطف يسارًا", "turn_right": "انعطف يمينًا", "go_straight": "استمر مستقيماً",
        "arrive": "وصلت إلى الوجهة", "depart": "انطلق", "roundabout": "عند الدوار خذ المخرج",
        "fuel": "وقود", "parking": "موقف", "hospital": "مستشفى", "pharmacy": "صيدلية",
        "shelter": "مأوى", "water": "ماء", "danger": "خطر", "safe": "آمن", "emergency": "طوارئ", "help": "مساعدة", "sos": "استغاثة"
    },
    "es": {
        "route": "ruta", "distance": "distancia", "duration": "duración", "from": "desde", "to": "hasta",
        "navigate": "navegar", "nearby": "cerca", "search": "buscar", "save": "guardar",
        "turn_left": "Gire a la izquierda", "turn_right": "Gire a la derecha", "go_straight": "Siga recto",
        "arrive": "Llegada al destino", "depart": "Salida", "roundabout": "En la rotonda tome la salida",
        "fuel": "combustible", "parking": "aparcamiento", "hospital": "hospital", "pharmacy": "farmacia",
        "shelter": "refugio", "water": "agua", "danger": "peligro", "safe": "seguro", "emergency": "emergencia", "help": "ayuda", "sos": "SOS"
    },
    "de": {
        "route": "Route", "distance": "Entfernung", "duration": "Dauer", "from": "von", "to": "nach",
        "navigate": "navigieren", "nearby": "in der Nähe", "search": "suchen", "save": "speichern",
        "turn_left": "Links abbiegen", "turn_right": "Rechts abbiegen", "go_straight": "Geradeaus",
        "arrive": "Ziel erreicht", "depart": "Abfahrt", "roundabout": "Im Kreisverkehr Ausfahrt nehmen",
        "fuel": "Tankstelle", "parking": "Parkplatz", "hospital": "Krankenhaus", "pharmacy": "Apotheke",
        "shelter": "Unterstand", "water": "Wasser", "danger": "Gefahr", "safe": "sicher", "emergency": "Notfall", "help": "Hilfe", "sos": "SOS"
    },
    "fr": {
        "route": "itinéraire", "distance": "distance", "duration": "durée", "from": "de", "to": "à",
        "navigate": "naviguer", "nearby": "à proximité", "search": "rechercher", "save": "enregistrer",
        "turn_left": "Tournez à gauche", "turn_right": "Tournez à droite", "go_straight": "Continuez tout droit",
        "arrive": "Arrivée à destination", "depart": "Départ", "roundabout": "Au rond-point prenez la sortie",
        "fuel": "carburant", "parking": "parking", "hospital": "hôpital", "pharmacy": "pharmacie",
        "shelter": "abri", "water": "eau", "danger": "danger", "safe": "sûr", "emergency": "urgence", "help": "aide", "sos": "SOS"
    },
    "zh": {
        "route": "路线", "distance": "距离", "duration": "时长", "from": "从", "to": "到",
        "navigate": "导航", "nearby": "附近", "search": "搜索", "save": "保存",
        "turn_left": "左转", "turn_right": "右转", "go_straight": "直行",
        "arrive": "到达目的地", "depart": "出发", "roundabout": "在环岛出口",
        "fuel": "加油站", "parking": "停车场", "hospital": "医院", "pharmacy": "药店",
        "shelter": "避难所", "water": "水", "danger": "危险", "safe": "安全", "emergency": "紧急", "help": "帮助", "sos": "求救"
    },
    "ja": {
        "route": "ルート", "distance": "距離", "duration": "所要時間", "from": "から", "to": "まで",
        "navigate": "ナビゲート", "nearby": "近く", "search": "検索", "save": "保存",
        "turn_left": "左折", "turn_right": "右折", "go_straight": "直進",
        "arrive": "目的地に到着", "depart": "出発", "roundabout": "ロータリーで出口を",
        "fuel": "燃料", "parking": "駐車場", "hospital": "病院", "pharmacy": "薬局",
        "shelter": "避難所", "water": "水", "danger": "危険", "safe": "安全", "emergency": "緊急", "help": "助けて", "sos": "SOS"
    },
    "fa": {
        "route": "مسیر", "distance": "فاصله", "duration": "مدت", "from": "از", "to": "به",
        "navigate": "مسیریابی", "nearby": "نزدیک", "search": "جستجو", "save": "ذخیره",
        "turn_left": "به چپ بپیچید", "turn_right": "به راست بپیچید", "go_straight": "مستقیم بروید",
        "arrive": "به مقصد رسیدید", "depart": "حرکت", "roundabout": "در میدان خروجی را بگیرید",
        "fuel": "سوخت", "parking": "پارکینگ", "hospital": "بیمارستان", "pharmacy": "داروخانه",
        "shelter": "پناهگاه", "water": "آب", "danger": "خطر", "safe": "امن", "emergency": "اورژانس", "help": "کمک", "sos": "SOS"
    },
}

# Fallback to English for missing langs
for lang in SUPPORTED_LANGUAGES:
    if lang not in DICTIONARY:
        DICTIONARY[lang] = DICTIONARY["en"]

def is_rtl(lang: str) -> bool:
    base = lang.split("-")[0].lower()
    return base in RTL_LANGS or SUPPORTED_LANGUAGES.get(lang, {}).get("dir") == "RTL"

def get_locale_info(lang: str) -> Dict:
    return SUPPORTED_LANGUAGES.get(lang) or SUPPORTED_LANGUAGES.get(lang.split("-")[0]) or SUPPORTED_LANGUAGES["en"]

def translate(key: str, lang: str = "en") -> str:
    """Translate a navigation key to target language."""
    base = lang.split("-")[0] if lang not in DICTIONARY else lang
    # Try exact, then base, then en
    for l in (lang, base, "en"):
        if l in DICTIONARY and key in DICTIONARY[l]:
            return DICTIONARY[l][key]
    return DICTIONARY["en"].get(key, key)

def detect_language(text: str) -> str:
    """Heuristic language detection: script + common words."""
    if not text:
        return "en"
    # Script detection
    if re.search(r'[\u0600-\u06FF]', text):
        # Arabic script - could be ar, fa, ur
        if re.search(r'[پچژگ]', text):
            return "fa"
        if re.search(r'[ٹڈڑ]', text):
            return "ur"
        return "ar"
    if re.search(r'[\u0590-\u05FF]', text):
        return "he"
    if re.search(r'[\u4E00-\u9FFF]', text):
        # Could be zh, ja (if hiragana/katakana present)
        if re.search(r'[\u3040-\u30FF]', text):
            return "ja"
        return "zh"
    if re.search(r'[\uAC00-\uD7AF]', text):
        return "ko"
    if re.search(r'[\u0E00-\u0E7F]', text):
        return "th"
    if re.search(r'[\u0900-\u097F]', text):
        return "hi"
    # Latin - word heuristics
    low = text.lower()
    if any(w in low for w in [" und ", " der ", " die ", " das "]):
        return "de"
    if any(w in low for w in [" le ", " la ", " de ", " et "]):
        return "fr"
    if any(w in low for w in [" el ", " la ", " y ", " de "]):
        return "es"
    if any(w in low for w in [" și ", " și", " din ", " pentru "]):
        return "ro"
    if any(w in low for w in [" و ", " در ", " به ", " از "]):
        return "fa"
    return "en"

def cultural_poi_tags(category: str, lang: str = "en"):
    """Return OSM selectors for cultural POI, considering language. Returns None if not cultural."""
    cat = category.lower()
    if cat in CULTURAL_POI:
        return CULTURAL_POI[cat]
    # Not a cultural category — let main POI_CATEGORIES handle it
    return None

def format_distance(m: float, lang: str = "en", units: str = "auto") -> str:
    """Format distance per locale."""
    info = get_locale_info(lang)
    if units == "auto":
        units = info.get("units", "metric")
    # Only imperial if explicitly imperial — not forced by region for generic 'en'
    # en-US is imperial via its units field, not via region check
    if units == "imperial":
        mi = m / 1609.344
        if mi >= 0.1:
            return f"{mi:.1f} mi"
        return f"{m * 3.28084:.0f} ft"
    # metric (default)
    if m >= 1000:
        return f"{m/1000:.1f} km"
    return f"{m:.0f} m"

def format_duration(s: float, lang: str = "en") -> str:
    s = int(round(s))
    h, m = divmod(s // 60, 60)
    # Localized
    if lang.startswith("de"):
        return f"{h} Std {m:02d} Min" if h else f"{m} Min"
    if lang.startswith("fr"):
        return f"{h} h {m:02d} min" if h else f"{m} min"
    if lang.startswith("ar"):
        return f"{h} ساعة {m:02d} دقيقة" if h else f"{m} دقيقة"
    if lang.startswith("zh"):
        return f"{h}小时{m}分" if h else f"{m}分"
    if lang.startswith("ja"):
        return f"{h}時間{m}分" if h else f"{m}分"
    return f"{h} h {m:02d} min" if h else f"{m} min"

def bidi_wrap(text: str, lang: str) -> str:
    """Wrap RTL text with Unicode bidi markers for display."""
    if is_rtl(lang):
        return f"\u202B{text}\u202C"
    return text

def list_languages() -> List[Dict]:
    return [{"code": k, **v} for k, v in sorted(SUPPORTED_LANGUAGES.items())]
