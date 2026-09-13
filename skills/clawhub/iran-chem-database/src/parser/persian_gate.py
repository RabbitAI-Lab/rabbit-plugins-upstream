"""Persian/Farsi language gate — v2.12.

Policy: **every Telegram channel in this database must be Iranian AND must
publish Persian/Farsi text.** Country provenance alone is not enough — an
Iranian-owned channel that posts only English is out of scope for a Persian
supplier index, and (more usefully) the Persian requirement is a strong,
cheap, content-level corroboration of the country gate in
:mod:`src.discovery.country_gate`.

Two levels, because they answer different questions:

* :func:`channel_persian_profile` — *is this channel Persian-speaking?*
  Measured over a whole mirrored channel as the share of posts containing
  Persian script. Robust to individual English catalogue posts.
* :func:`post_language` — *what language is this post?* Used for reporting
  and for the mixed-script reality of real Iranian reagent channels, whose
  posts are frequently Persian boilerplate wrapped around a Latin IUPAC name
  (``006123 Exir Melamine, 99% 500g`` + «موجود و آماده تحویل»).

Critically, the post-level check is **not** used to throw product data away:
a Latin-only catalogue line inside a verified Persian channel is exactly the
high-value structured data this release is trying to capture. Enforcement is
at the CHANNEL level; post language is recorded as metadata.

Arabic-script disambiguation
----------------------------
Persian and Arabic share a Unicode block, so "contains U+0600..U+06FF" alone
would accept an Arabic channel. Persian-exclusive letters (گ چ پ ژ ک ی) and
common Persian function words are therefore scored separately, and a channel
whose script is Arabic-but-not-Persian is reported as ``ar`` and refused.
"""
from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass, field
from typing import Dict, Iterable, List

# Any Arabic-script codepoint (shared by Persian, Arabic, Urdu).
RE_ARABIC_SCRIPT = re.compile(r"[\u0600-\u06FF\uFB50-\uFDFF\uFE70-\uFEFF]")

# Letters used in Persian but NOT in standard Arabic — the strongest cheap
# discriminator between fa and ar.
RE_PERSIAN_LETTERS = re.compile(r"[\u067E\u0686\u0698\u06A9\u06AF\u06CC]")  # پ چ ژ ک گ ی

# Arabic-specific letters/marks rare in Persian text.
RE_ARABIC_ONLY = re.compile(r"[\u0629\u064A\u0643\u0649]")  # ة ي ك ى

#: High-frequency Persian function words. Presence of several is decisive.
PERSIAN_STOPWORDS = (
    "است", "این", "آن", "که", "را", "برای", "با", "از", "به", "در", "های",
    "شده", "می‌شود", "میشود", "کنید", "دارد", "هستند", "ما", "شما", "بود",
    "نیز", "یا", "هم", "تا", "بر", "روی", "خود", "بین", "طور", "باشد",
)

#: Arabic function words that do NOT occur in normal Persian prose. Used only
#: to reject Arabic-script channels that are not Persian.
ARABIC_STOPWORDS = (
    "في", "من", "إلى", "على", "التي", "الذي", "هذا", "هذه", "ذلك", "أن",
    "كان", "يكون", "لكن", "أو", "ثم", "قد", "لا", "ما", "هو", "هي",
    "نحن", "بكم", "لدينا", "يرجى", "الاتصال", "شركة", "المواد", "الكيميائية",
)

#: Persian words that specifically indicate chemical commerce.
PERSIAN_TRADE_WORDS = (
    "موجود", "قیمت", "تومان", "ریال", "فروش", "خرید", "عرضه", "تأمین",
    "تامین", "واردات", "وارد", "پخش", "بسته", "کیلو", "گرم", "لیتر",
    "خلوص", "گرید", "مواد", "شیمیایی", "آزمایشگاهی", "صنعتی", "تحویل",
    "ارسال", "سفارش", "انبار", "درصد", "برند",
)

#: A channel must reach this share of Persian posts to be admitted.
MIN_CHANNEL_PERSIAN_RATIO = 0.30
#: …measured over at least this many text posts (below it, judgement is weak).
MIN_PROFILE_POSTS = 5
#: A post counts as Persian at/above this many Persian-script characters.
MIN_POST_PERSIAN_CHARS = 3


def normalize_persian(text: str) -> str:
    """Canonicalise Persian text for reliable matching.

    Real channel text mixes Arabic and Persian codepoints for the same letter
    (ي/ی, ك/ک), uses zero-width non-joiners inconsistently, and writes digits
    in Persian, Arabic-Indic or ASCII. Normalising once here means every
    downstream matcher (aliases, trade words, units) sees one spelling.
    """
    if not text:
        return ""
    text = unicodedata.normalize("NFKC", text)
    # Unify Arabic variants onto their Persian equivalents.
    trans = {
        "\u064A": "\u06CC",  # ي -> ی
        "\u0649": "\u06CC",  # ى -> ی
        "\u0643": "\u06A9",  # ك -> ک
        "\u0629": "\u0647",  # ة -> ه
        "\u0623": "\u0627", "\u0625": "\u0627", "\u0622": "\u0627",  # أ إ آ -> ا
        "\u0624": "\u0648",  # ؤ -> و
        "\u0626": "\u06CC",  # ئ -> ی
        "\u200c": " ",       # ZWNJ -> space
        "\u200f": "", "\u200e": "",
    }
    text = text.translate(str.maketrans(trans))
    # Strip Arabic diacritics (harakat) — decorative in Persian prose.
    text = re.sub(r"[\u064B-\u0652\u0670]", "", text)
    return re.sub(r"[ \t]+", " ", text)


def fa_digits_to_en(text: str) -> str:
    """Persian (۰-۹) and Arabic-Indic (٠-٩) digits -> ASCII."""
    if not text:
        return ""
    out = []
    for ch in text:
        o = ord(ch)
        if 0x06F0 <= o <= 0x06F9:
            out.append(chr(o - 0x06F0 + 48))
        elif 0x0660 <= o <= 0x0669:
            out.append(chr(o - 0x0660 + 48))
        else:
            out.append(ch)
    return "".join(out)


def persian_char_count(text: str) -> int:
    return len(RE_ARABIC_SCRIPT.findall(text or ""))


def post_language(text: str) -> str:
    """Classify one post: ``fa`` | ``ar`` | ``en`` | ``mixed`` | ``none``."""
    if not text or not text.strip():
        return "none"
    norm = normalize_persian(text)
    script = persian_char_count(norm)
    latin = len(re.findall(r"[A-Za-z]", norm))

    if script < MIN_POST_PERSIAN_CHARS:
        return "en" if latin >= 3 else "none"

    # Distinguish Persian from Arabic. NOTE: this must be measured on the RAW
    # text — normalize_persian() folds ي->ی and ك->ک, which would erase exactly
    # the letters that tell the two languages apart.
    fa_letters = len(RE_PERSIAN_LETTERS.findall(text))
    ar_only = len(RE_ARABIC_ONLY.findall(text))
    # Stopword/trade matching uses the normalised form so spelling variants
    # still match, but Arabic function words are checked too.
    fa_words = sum(1 for w in PERSIAN_STOPWORDS if w in norm)
    fa_trade = sum(1 for w in PERSIAN_TRADE_WORDS if w in norm)
    ar_words = sum(1 for w in ARABIC_STOPWORDS if w in text)

    # Arabic-exclusive letters outnumbering Persian-exclusive ones, with no
    # Persian vocabulary to counterbalance, means this is Arabic.
    if ar_only > fa_letters and fa_words + fa_trade == 0:
        return "ar"
    if ar_words >= 2 and fa_letters == 0:
        return "ar"

    is_fa = fa_letters > 0 or fa_words >= 1 or fa_trade >= 1
    if not is_fa:
        return "ar" if script >= 10 else "mixed"
    return "mixed" if latin >= max(10, script) else "fa"


def is_persian_post(text: str) -> bool:
    return post_language(text) in ("fa", "mixed")


@dataclass
class PersianProfile:
    """Channel-level Persian verdict with the numbers behind it."""
    channel: str
    posts_total: int = 0
    posts_with_text: int = 0
    posts_persian: int = 0
    posts_arabic: int = 0
    posts_latin: int = 0
    persian_ratio: float = 0.0
    persian_chars: int = 0
    trade_words_seen: List[str] = field(default_factory=list)
    is_persian: bool = False
    reason: str = ""

    def as_dict(self) -> dict:
        return {
            "channel": self.channel,
            "posts_total": self.posts_total,
            "posts_with_text": self.posts_with_text,
            "posts_persian": self.posts_persian,
            "posts_arabic": self.posts_arabic,
            "posts_latin": self.posts_latin,
            "persian_ratio": round(self.persian_ratio, 3),
            "persian_chars": self.persian_chars,
            "trade_words_seen": self.trade_words_seen,
            "is_persian": self.is_persian,
            "reason": self.reason,
        }


def channel_persian_profile(channel: str, texts: Iterable[str]) -> PersianProfile:
    """Measure whether a channel genuinely publishes Persian.

    ``texts`` is every post body mirrored for the channel.
    """
    prof = PersianProfile(channel=channel)
    trade: set = set()
    for text in texts:
        prof.posts_total += 1
        if not text or not text.strip():
            continue
        prof.posts_with_text += 1
        lang = post_language(text)
        if lang in ("fa", "mixed"):
            prof.posts_persian += 1
            prof.persian_chars += persian_char_count(text)
            norm = normalize_persian(text)
            for w in PERSIAN_TRADE_WORDS:
                if w in norm:
                    trade.add(w)
        elif lang == "ar":
            prof.posts_arabic += 1
        elif lang == "en":
            prof.posts_latin += 1

    prof.trade_words_seen = sorted(trade)[:15]
    prof.persian_ratio = (prof.posts_persian / prof.posts_with_text
                          if prof.posts_with_text else 0.0)

    if prof.posts_with_text == 0:
        prof.is_persian = False
        prof.reason = "no text posts to judge"
    elif prof.posts_with_text < MIN_PROFILE_POSTS:
        # Small sample: judge on the evidence available rather than refusing.
        # A tiny channel that is unambiguously Persian is still Persian; the
        # verdict is simply marked low-confidence via `reason`. Refusing here
        # would also make the gate untestable on small fixtures and would drop
        # genuine low-volume Iranian vendors.
        prof.is_persian = (prof.posts_persian > prof.posts_arabic
                           and prof.persian_ratio >= MIN_CHANNEL_PERSIAN_RATIO)
        prof.reason = (f"small sample ({prof.posts_with_text} text posts): "
                       f"{'Persian' if prof.is_persian else 'not Persian'} "
                       f"on {prof.posts_persian} fa / {prof.posts_arabic} ar")
    elif prof.posts_arabic > prof.posts_persian:
        prof.is_persian = False
        prof.reason = (f"Arabic-script but not Persian "
                       f"({prof.posts_arabic} ar > {prof.posts_persian} fa)")
    elif prof.persian_ratio < MIN_CHANNEL_PERSIAN_RATIO:
        prof.is_persian = False
        prof.reason = (f"Persian ratio {prof.persian_ratio:.2f} < "
                       f"{MIN_CHANNEL_PERSIAN_RATIO}")
    else:
        prof.is_persian = True
        prof.reason = (f"Persian verified: {prof.posts_persian}/"
                       f"{prof.posts_with_text} posts "
                       f"({prof.persian_ratio:.0%}), "
                       f"{len(prof.trade_words_seen)} trade terms")
    return prof


def verify_channel_persian(channel: str, texts: Iterable[str]) -> Dict[str, object]:
    """Convenience wrapper returning the profile as a plain dict."""
    return channel_persian_profile(channel, texts).as_dict()
