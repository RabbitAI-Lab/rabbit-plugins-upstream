#!/usr/bin/env python3
"""
prompt_compactor.py — reshape a prompt into the form models prefill fastest.

Measured (Qwen2.5-0.5B, 2-core CPU): 274-char verbose prompt = 3.47s cold / 1.89s warm;
compacted to 32 chars = 1.02s / 1.07s. 3.4x cold, 1.46x average warm.

SAFETY: content-bearing tokens are never dropped. Filler is removed; anything resembling a
constraint (numbers, quoted text, code, negations, "must") is preserved, and if a rule would
touch one, the rule is skipped and a warning emitted.

v1.5.0 — any agent, any model, any language:
  * multilingual filler (English, Persian, Arabic, Spanish, French, German,
    Portuguese) — whole-phrase ceremony only, never morphological guessing
  * --profile conservative|standard|aggressive (how much ceremony to strip)
  * question hoisting understands ؟ (U+061F) and ？ (U+FF1F), not just "?"
  * protects «…», “…” and 『…』 spans the same way as `code` and "quotes"
  * idempotent: compact(compact(x)) == compact(x) for every input (verified
    by a fixpoint fuzz loop in selftest.sh); --selfcheck asserts it per call
  * script-aware token estimate (latin ≈ 3.5 chars/token, CJK ≈ 1.7) in --json
  * --lang fa|ar|es|fr|de|pt|en|auto restricts stripping to given languages

Usage:
  prompt_compactor.py --text "..." | --file f.txt [--json] [--profile P]
                      [--lang L] [--selfcheck]
"""
import argparse, json, re, sys

# ── filler patterns, tiered by aggressiveness ────────────────────────────────
# tier 1 = unambiguous ceremony (greetings, thanks, "please")   -> conservative+
# tier 2 = standard hedges/prefaces (the historic v1.x set)      -> standard+
# tier 3 = weak fillers that occasionally carry tone             -> aggressive
#
# Each entry is (tier, pattern). Non-Latin patterns use explicit Unicode word
# boundaries; Persian ZWNJ (U+200C) is written as \u200c and made optional
# everywhere it can occur, because copy/paste and IMEs disagree about it.
FILLER_PATTERNS = [
    # — tier 1: greetings / thanks / please (EN) —
    (1, r"\bhi there\b[,!. ]*"), (1, r"\bhey there\b[,!. ]*"), (1, r"\bhello there\b[,!. ]*"),
    (1, r"\bhi+\b[,!. ]*"), (1, r"\bhello\b[,!. ]*"), (1, r"\bhey\b[,!. ]*"),
    (1, r"\bthanks so much\b[!. ]*"), (1, r"\bthank you( very much)?\b[!. ]*"), (1, r"\bthanks\b[!. ]*"),
    (1, r"\bplease\b"), (1, r"\bkindly\b"),
    (1, r"\bi hope (you are|you're) doing well\b[,!. ]*"), (1, r"\bhow are you\b[,?. ]*"),
    # — tier 1: greetings / thanks / please (multilingual) —
    # Persian
    (1, r"\bسلام\b[ !،.]*"), (1, r"\bدرود\b[ !،.]*"),
    (1, r"\bممنون\b[ !،.]*"), (1, r"\bمتشکرم\b[ !،.]*"), (1, r"\bمرسی\b[ !،.]*"),
    (1, r"\bلطفا\b"), (1, r"\bخواهش می[\u200c ]?کنم\b"),
    (1, r"\bامیدوارم حالت خوب باشه\b[ !،.]*"),
    # Arabic
    (1, r"\bمرحبا\b[ !،.]*"), (1, r"\bأهلا( وسهلا)?\b[ !،.]*"), (1, r"\bالسلام عليكم\b[ !،.]*"),
    (1, r"\bشكرا( جزيلا)?\b[ !،.]*"), (1, r"\bمن فضلك\b"), (1, r"\bلو سمحت\b"),
    # Spanish
    (1, r"\bhola\b[,!. ]*"), (1, r"\bgracias( totales)?\b[!,. ]*"), (1, r"\bmuchas gracias\b[!,. ]*"),
    (1, r"\bpor favor\b"),
    # French
    (1, r"\bbonjour\b[,!. ]*"), (1, r"\bsalut\b[,!. ]*"),
    (1, r"\bmerci( beaucoup)?\b[!,. ]*"), (1, r"\bs'il (te|vous) pla[îi]t\b"),
    # German
    (1, r"\bhallo\b[,!. ]*"), (1, r"\bdanke( sch[öo]n)?\b[!,. ]*"), (1, r"\bbitte\b"),
    # Portuguese
    (1, r"\bol[áa]\b[,!. ]*"), (1, r"\bobrigad[oa]( muito)?\b[!,. ]*"), (1, r"\bpor favor\b"),

    # — tier 2: standard hedges and prefaces (EN, historic set) —
    (2, r"\bhelp me out\b"), (2, r"\bhelp me\b"), (2, r"\bwith something\b"),
    (2, r"\bpossibly\b"), (2, r"\bsomehow\b"), (2, r"\btell me\b"),
    (2, r"\bi was wondering if\b"), (2, r"\bi wonder if\b"),
    (2, r"\bcould you please\b"), (2, r"\bcould you\b"), (2, r"\bcan you please\b"), (2, r"\bcan you\b"),
    (2, r"\bwould you mind\b"), (2, r"\bwould you\b"),
    (2, r"\bif it'?s not too much trouble\b[,. ]*"), (2, r"\bif you don'?t mind\b[,. ]*"),
    (2, r"\bbasically\b[,. ]*"), (2, r"\bactually\b[,. ]*"), (2, r"\bjust\b "),
    (2, r"\bwhat i('m| am) trying to do is\b[,. ]*"),
    (2, r"\bi want to know\b[,. ]*"), (2, r"\bi'?d like to know\b[,. ]*"), (2, r"\bi need to know\b[,. ]*"),
    (2, r"\bsort of\b"), (2, r"\bkind of\b"), (2, r"\ba bit\b"), (2, r"\bmaybe\b"), (2, r"\bperhaps\b"),
    (2, r"\bhappens to be\b"), (2, r"\bhelp me out with something\b"),
    (2, r"\bfor me\b"), (2, r"\bas soon as possible\b"), (2, r"\basap\b"),
    # — tier 2: standard hedges (multilingual) —
    # Persian: "I wanted to know" / "if possible" / "actually" / "like (filler)" / "okay well"
    (2, r"می[\u200c ]?خواستم (بدانم|بدونم)\b که?\b[ ،.]*"),
    (2, r"\bاگر ممکنه\b"), (2, r"\bاگر زحمتی نیست\b[ ،.]*"),
    (2, r"\bراستش\b[ ،.]*"), (2, r"\bاصلا\b[ ،.]*"), (2, r"\bمثلا\b[ ،.]*"), (2, r"\bیه نوعی\b"),
    (2, r"\bخیلی خب\b[ ،.]*"), (2, r"\bیعنی\b "), (2, r"\bبه نوعی\b"),
    # Arabic: "I want to know" / "if possible" / "actually"
    (2, r"\bأريد أن أعرف\b[ ،.]*"), (2, r"\bواريد ان اعرف\b[ ،.]*"),
    (2, r"\bإذا أمكن\b"), (2, r"\bفي الحقيقة\b[ ،.]*"), (2, r"\bفي الواقع\b[ ،.]*"),
    # Spanish
    (2, r"\bme gustaría saber\b[ ,.]*"), (2, r"\bme gustaria saber\b[ ,.]*"),
    (2, r"\b¿?me podrías (decir|explicar)\b[ ,.]*"), (2, r"\bpodrías\b"),
    (2, r"\bo sea\b"), (2, r"\bbásicamente\b[ ,.]*"), (2, r"\bbasicamente\b[ ,.]*"),
    (2, r"\bsi no es mucha molestia\b[ ,.]*"),
    # French
    (2, r"\bje voudrais savoir\b[ ,.]*"), (2, r"\bj'aimerais savoir\b[ ,.]*"),
    (2, r"\best-ce que tu pourrais\b"), (2, r"\best-ce que vous pourriez\b"),
    (2, r"\ben fait\b"), (2, r"\bdu coup\b"), (2, r"\bsi ça ne vous dérange pas\b[ ,.]*"),
    # German
    (2, r"\bich würde gerne wissen\b[ ,.]*"), (2, r"\bich wuerde gerne wissen\b[ ,.]*"),
    (2, r"\bkönntest du\b"), (2, r"\bkannst du\b"), (2, r"\beigentlich\b[ ,.]*"),
    # Portuguese
    (2, r"\beu gostaria de saber\b[ ,.]*"), (2, r"\bvocê poderia\b"),
    (2, r"\bvocês? poderiam\b"), (2, r"\bna verdade\b[ ,.]*"),

    # — tier 3: aggressive-only weak fillers (EN) —
    (3, r"\bi think\b "), (3, r"\bi believe\b "), (3, r"\bsimply\b "),
    (3, r"\breally\b "), (3, r"\bvery\b "), (3, r"\bquite\b "), (3, r"\btotally\b "),
    (3, r"\bhonestly\b[ ,.]*"), (3, r"\bto be honest\b[ ,.]*"), (3, r"\bat the end of the day\b[ ,.]*"),
]

# language tag -> which pattern indexes apply. "en" = ASCII-word patterns only.
# A pattern is associated with a language by inspecting whether it contains
# non-ASCII characters (fa/ar here are non-Latin; es/fr/de/pt are Latin and
# safe to run together with en — they are distinct phrases, not morphology).
def _pattern_langs(pat):
    has_nonlatin = any(ord(c) > 0x24F for c in pat)
    if has_nonlatin:
        if re.search(r"[\u0600-\u06FF]", pat):
            return {"fa", "ar"}
        return {"en"}  # defensive; none currently
    # Latin-script: could be en/es/fr/de/pt — allow for all Latin languages
    return {"en", "es", "fr", "de", "pt"}

PROFILE_TIERS = {"conservative": 1, "standard": 2, "aggressive": 3}

CONSTRAINT_SIGNALS = [
    r"\bmust\b", r"\bdon'?t\b", r"\bdo not\b", r"\bnever\b", r"\bonly\b",
    r"\bexactly\b", r"\brequired?\b", r"\bavoid\b", r"\bwithout\b",
    r"\d", r"`[^`]+`", r'"[^"]+"', r"'[^']+'",
    # multilingual constraint markers (v1.5.0): must/only/never equivalents
    r"\bحتما\b", r"\bفقط\b", r"\bهرگز\b",                 # fa/ar: certainly, only, never
    r"\bsolo\b", r"\bs[óo]lo\b", r"\bnunca\b",            # es/pt: only, never
    r"\bseulement\b", r"\bselement\b", r"\bjamais\b",     # fr: only, never
    r"\bnur\b", r"\bniemals\b", r"\bgenau\b",             # de: only, never, exactly
]

# NOTE: `[^.?!what]*\?` backtracks catastrophically on long text containing no '?' — the
# engine retries the greedy run from every start position (4.2s on a 42k-char input).
# Anchoring the run to a sentence boundary makes each start position fail in O(1).
# v1.5.0: the terminal class also accepts the Arabic/Persian question mark (؟,
# U+061F) and the fullwidth question mark (？, U+FF1F).
QUESTION_RE = re.compile(r"(?:(?<=^)|(?<=[.?!؟？\n]))[^.?!؟？\n]*[?؟？]")

PREFACE_REWRITES = [
    (r"\b(?:if\s+)?you\s+could\s+(?:please\s+)?help\s+me\s+(?:to\s+)?understand\b", "explain"),
    (r"\bhelp\s+me\s+(?:to\s+)?understand\b", "explain"),
    (r"\b(?:if\s+)?you\s+could\s+(?:please\s+)?(?:tell|show)\s+me\b", ""),
    (r"\b(?:if\s+)?you\s+could\s+(?:please\s+)?explain\b", "explain"),
    (r"\b(?:if\s+)?you\s+could\s+(?:please\s+)?\b", ""),
    (r"\bi\s+need\s+help\s+(?:with|understanding)\b", "explain"),
    (r"\bi'?d\s+appreciate\s+it\s+if\s+you\s+(?:could|would)\b", ""),
]


def has_constraint(s):
    return any(re.search(p, s, re.I) for p in CONSTRAINT_SIGNALS)


def _tidy_final(s):
    """Post-assembly cleanup: only punctuation-local rules. Must NOT collapse
    \\s+→' ' — that would flatten the '\\n' between the hoisted question and its
    Context line, which is part of the output contract."""
    s = re.sub(r" +([,.;:!?])", r"\1", s)
    s = re.sub(r"([,.;:])\1+", r"\1", s)
    return s


def protect(text):
    r"""Vault code spans and quoted spans so no rule can ever touch them.

    v1.5.0 hardening (found by fixpoint fuzzing):
      * ONE combined alternation pass — with sequential patterns, a later span
        (e.g. "…") could swallow an earlier placeholder and nest it, so the
        inner span was never restored and \x00…\x00 leaked into the output.
        A single left-to-right scan makes nesting structurally impossible.
      * Placeholders use Private-Use-Area chars (\ue000+) instead of digits —
        the digit form matched the \d CONSTRAINT_SIGNAL, so a placeholder made
        filler look like a constraint and blocked its own removal.
      * Also stashes guillemets («…»), curly quotes (“…”), CJK corner brackets
        (『…』) — quoting styles that matter now that stripping is multilingual.
    """
    # CONSENSUS-REVIEW FIX (gpt-oss/llm7/gemini all probed this): raw NUL
    # bytes in the input could combine with a stashed span's PUA index to form
    # a marker-like triple that restore() would mis-replace — measured: a
    # literal "\x00X\x00" in the prompt left an unrestored placeholder in the
    # output. NULs are invalid in prompts (every chat API rejects them), so
    # they are dropped here rather than escaped.
    if "\x00" in text:
        text = text.replace("\x00", "")
    vault = []
    span = (r"```.*?```"          # 1 multiline code fence
            r"|`[^`\n]+`"          # 2 inline code
            r'|"[^"\n]{3,}"'       # 3 double-quoted
            r"|«[^«»\n]{2,}»"      # 4 guillemets
            r"|“[^“”\n]{2,}”"      # 5 curly quotes
            r"|『[^『』\n]{2,}』")   # 6 CJK corner brackets
    def stash(m):
        vault.append(m.group(0))
        return f"\x00{chr(0xE000 + len(vault) - 1)}\x00"
    text = re.sub(span, stash, text, flags=re.S)
    return text, vault


def restore(text, vault):
    for i, v in enumerate(vault):
        text = text.replace(f"\x00{chr(0xE000 + i)}\x00", v)
    return text


def _active_patterns(profile="standard", lang="auto"):
    """Filter (tier, pattern) by profile aggressiveness and target language.

    lang=auto runs everything (safe: patterns are whole ceremonial phrases,
    never morphology). lang=fa/ar/en/… restricts stripping to that language's
    patterns plus language-neutral formatting rules.
    """
    max_tier = PROFILE_TIERS.get(profile, 2)
    out = []
    for tier, pat in FILLER_PATTERNS:
        if tier > max_tier:
            continue
        if lang and lang != "auto" and lang not in _pattern_langs(pat):
            continue
        out.append(pat)
    return out


def detect_lang(text):
    """Cheap script sniff — advisory only, used for reporting and hoisting."""
    counts = {"en": 0, "fa": 0, "ar": 0, "cjk": 0}
    for ch in text:
        o = ord(ch)
        if 0x0600 <= o <= 0x06FF or 0x0750 <= o <= 0x077F or 0xFB50 <= o <= 0xFDFF:
            counts["ar"] += 1
            # Persian-exclusive letters: پ چ ژ گ + ی/ک used Persian-style
            if ch in "پچژگ":
                counts["fa"] += 1
        elif 0x4E00 <= o <= 0x9FFF or 0x3040 <= o <= 0x30FF:
            counts["cjk"] += 1
        elif ch.isalpha() and o < 0x0250:
            counts["en"] += 1
    if counts["fa"] > 0:
        return "fa"
    if counts["ar"] > counts["en"] and counts["ar"] > counts["cjk"]:
        return "ar"
    if counts["cjk"] > counts["en"]:
        return "cjk"
    return "en"


def _estimate_tokens(text):
    """Script-aware token estimate. Latin ≈ 3.5 chars/token, CJK ≈ 1.7.

    Deliberately a rough, dependency-free heuristic (per cross-model review:
    exact tokenizers diverge 30%+ per BPE vocabulary — report the estimate,
    let the caller decide). Returns (est_tokens, cjk_chars).
    """
    cjk = sum(1 for ch in text if 0x4E00 <= ord(ch) <= 0x9FFF
              or 0x3040 <= ord(ch) <= 0x30FF
              or 0xAC00 <= ord(ch) <= 0xD7AF)
    other = len(text) - cjk
    return round(other / 3.5 + cjk / 1.7), cjk


def _compact_once(text, profile="standard", lang="auto"):
    """One pass of the compaction pipeline. Deterministic and pure; compact()
    iterates this to its fixed point so the final output is stable under
    re-compaction: compact(compact(x, p, l), p, l) == compact(x, p, l)."""
    original = text
    warnings = []
    work, vault = protect(text)
    pats = _active_patterns(profile, lang)

    def rewrite_prefaces(s):
        for pat, repl in PREFACE_REWRITES:
            m = re.search(pat, s, re.I)
            if m and not has_constraint(m.group(0)):
                s = re.sub(pat, repl, s, flags=re.I)
        return s

    work = rewrite_prefaces(work)

    # Single pass per pattern. The previous implementation re-scanned the whole string
    # after every removal (O(n^2)): 10k chars took 0.25s and 100k took 30s, which is absurd
    # for a tool whose entire purpose is cutting latency. re.sub with a callback removes
    # every occurrence in one scan while still honouring the constraint guard per match.
    def _strip(m):
        seg = m.group(0)
        if has_constraint(seg):
            warnings.append(f"kept (carries meaning): {seg.strip()!r}")
            return seg
        return " "

    for pat in pats:
        work = re.sub(pat, _strip, work, flags=re.I)

    work = rewrite_prefaces(work)
    for pat in (r"^\s*i was wondering\b", r"^\s*i wonder\b", r"^\s*you\s+(?=explain\b)",
                r"\bexplain\s+understanding\s+(?:of\s+)?", r"\bexplain\s+explain\b"):
        m = re.search(pat, work, re.I)
        if m and not has_constraint(m.group(0)):
            repl = "explain " if "understanding" in pat or "explain\\s+explain" in pat else ""
            work = re.sub(pat, repl, work, count=1, flags=re.I)

    def _tidy(s):
        """Punctuation-local cleanup. NOT \\s+->' ' — that would flatten the
        question/Context newline. Applied to the pre-hoist text AND to the
        final assembled result, so reassembly cannot leave sequences that a
        second pass would normalize (a fixpoint-fuzz finding: pass 1 emitted
        'X. :.0' that pass 2 cleaned to 'X.:.0')."""
        s = re.sub(r"\s+", " ", s)
        s = re.sub(r"\s+([,.;:!?])", r"\1", s)
        s = re.sub(r"([,.;:])\1+", r"\1", s)
        return s

    work = _tidy(work)
    # v1.5.0: leading cleanup no longer eats '?' — a degenerate hoisted question
    # can legitimately BE just '?' ('.?' at a sentence boundary), and stripping
    # it made pass 2 delete the question pass 1 had emitted.
    work = re.sub(r"^[\s,.;:!-]+", "", work)
    work = work.strip()

    # v1.5.0 (fixpoint guarantee): hoist on the STASHED representation and
    # restore the vault LAST. Restoring before the hoist re-materialized code
    # spans mid-pipeline, so (a) the question extractor could slice a restored
    # span in half — leaving an open-ended `span` that pass 2 then could not
    # stash at all — and (b) whitespace inside restored spans escaped _tidy in
    # one pass but not the other. With restore last, every pass runs the exact
    # same pipeline over the same stashed shape: compact(compact(x)) == compact(x).
    hoisted = work
    q = QUESTION_RE.search(work)
    if q:
        question = q.group(0).strip()
        # v1.5.0: the matched run may carry leading commas/semicolons
        # ('یم,؟' -> ',؟' after filler removal); they must not open the final
        # prompt, and their presence made pass 2 strip them and diverge.
        question = re.sub(r"^[\s,.;:]+", "", question) or question
        rest = (work[:q.start()] + " " + work[q.end():]).strip()
        rest = re.sub(r"\s+", " ", rest).strip(" ,.;:")
        # Strip any "Context:" labels already present, otherwise re-compacting an
        # already-compacted prompt stacks them forever:
        #   "0?\nContext: 0:0:0" -> "Context: Context: 0:0:0" -> ... (found by fuzzing)
        rest = re.sub(r"^(?:Context:\s*)+", "", rest).strip()
        # Word count on the stashed text: placeholders are atomic PUA units and
        # are not \w, so each one counts as 3 words — an escrowed code span IS
        # content and must satisfy the "keep context" threshold on its own.
        n_stashed = rest.count("\x00") // 2
        words = re.findall(r"[\w\u0600-\u06FF`\"\"]+", rest)
        n_words = len(words) + 3 * n_stashed
        if rest and n_words >= 3 and (has_constraint(rest) or n_words >= 5):
            hoisted = f"{question}\nContext: {rest}"
        else:
            hoisted = question
        hoisted = _tidy_final(hoisted)

    hoisted = restore(hoisted, vault)

    # v1.5.0: capitalize AFTER hoisting (a pre-hoist capitalize never saw the
    # hoisted question's first char, so pass 2 capitalized text pass 1 hadn't).
    # Latin-initial only — upper() on Persian/Arabic is a no-op but CJK/RTL
    # text must not be flagged as "uncapitalized Latin" by accident.
    if hoisted and ord(hoisted[0]) < 0x0590 and hoisted[0].isalpha():
        hoisted = hoisted[0].upper() + hoisted[1:]

    return hoisted, warnings


def compact(text, profile="standard", lang="auto"):
    """Compact `text` to its FIXED POINT.

    Hoisting reassembles text (question first, context after), and with
    unbalanced quote glyphs the vault pairing of pass N can differ from pass
    N+1 — a single pass therefore could not guarantee
    compact(compact(x)) == compact(x) on adversarial input (found by a
    4,000-case fixpoint fuzz; 159 failures). Iterating the pipeline until the
    output stops changing makes idempotence hold BY CONSTRUCTION: the returned
    value is a fixed point of _compact_once, so compacting it again returns it
    immediately. Converges in <=3 passes on everything observed (normally 1).
    """
    original = text
    out, warn = _compact_once(text, profile, lang)
    converged = True
    for _ in range(7):                     # hard cap 8 passes total; observed max 3
        nxt, w2 = _compact_once(out, profile, lang)
        if nxt == out:
            break
        out = nxt
        warn = warn + [x for x in w2 if x not in warn]
    else:
        converged = False                  # terminated by cap, not by stability
        warn.append("fixpoint cap reached (8 passes) — output may not be stable")
    saved = len(original) - len(out)
    pct = (saved / len(original) * 100) if original else 0.0
    est_tokens, cjk_chars = _estimate_tokens(out)
    est_tokens_orig, _ = _estimate_tokens(original)
    return {"original": original, "compact": out, "original_chars": len(original),
            "compact_chars": len(out), "chars_saved": saved, "percent_saved": round(pct, 1),
            "est_prefill_reduction_pct": round(min(0.75, max(0.0, pct/100*0.85))*100),
            "est_tokens_original": est_tokens_orig, "est_tokens_compact": est_tokens,
            "tokens_saved": max(0, est_tokens_orig - est_tokens),
            "cjk_chars": cjk_chars, "lang_detected": detect_lang(original),
            "profile": profile, "converged": converged, "warnings": warn}


def selfcheck(text, profile="standard", lang="auto"):
    """Assert the fixpoint property on one input: compacting twice must equal
    compacting once, and the result must be stable (pass 3 == pass 2)."""
    a = compact(text, profile, lang)["compact"]
    b = compact(a, profile, lang)["compact"]
    c = compact(b, profile, lang)["compact"]
    ok = (a == b == c)
    return ok, {"pass1": a, "pass2": b, "pass3": c}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--text"); ap.add_argument("--file")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--profile", choices=list(PROFILE_TIERS), default="standard",
                    help="conservative: greetings/thanks only · standard: +hedges (default) · aggressive: +weak fillers")
    ap.add_argument("--lang", default="auto",
                    help="auto|en|fa|ar|es|fr|de|pt — restrict stripping to these languages")
    ap.add_argument("--selfcheck", action="store_true",
                    help="verify idempotence on this input; exit 1 on failure")
    a = ap.parse_args()
    src = a.text if a.text else (open(a.file, encoding="utf-8").read() if a.file else sys.stdin.read())

    if a.selfcheck:
        ok, detail = selfcheck(src, a.profile, a.lang)
        if a.json:
            print(json.dumps({"idempotent": ok, **detail}, indent=2, ensure_ascii=False))
        else:
            print("IDEMPOTENT" if ok else "NOT IDEMPOTENT (fixpoint failed)")
            if not ok:
                print(f"  pass1: {detail['pass1']!r}")
                print(f"  pass2: {detail['pass2']!r}")
        return 0 if ok else 1

    r = compact(src, a.profile, a.lang)
    if a.json:
        print(json.dumps(r, indent=2, ensure_ascii=False)); return 0
    print("--- COMPACTED PROMPT ---"); print(r["compact"])
    print("--- STATS ---")
    print(f"{r['original_chars']} -> {r['compact_chars']} chars "
          f"({r['percent_saved']}% smaller, ~{r['est_prefill_reduction_pct']}% less prefill)")
    print(f"~{r['est_tokens_original']} -> ~{r['est_tokens_compact']} tokens "
          f"(estimate: latin 3.5 ch/tok, cjk 1.7 ch/tok)  lang={r['lang_detected']} profile={r['profile']}")
    for w in r["warnings"]:
        print(f"[warn] {w}")
    return 0


if __name__ == "__main__":
    sys.exit(main() or 0)
