import pathlib
"""
Property-based test suite for arena-turn-accelerator.

Instead of checking hand-picked examples, this asserts the INVARIANTS the plugin's
documentation promises, and lets Hypothesis search for counterexamples.

Run:  python3 -m pytest fuzz/test_properties.py -q
"""
import os
import re
import sys

from hypothesis import given, settings, strategies as st, HealthCheck, assume

SCRIPTS = str(pathlib.Path(__file__).resolve().parent.parent / "scripts")
sys.path.insert(0, SCRIPTS)

import prompt_compactor as pc  # noqa: E402
import spine  # noqa: E402
import register as reg  # noqa: E402
import quarry  # noqa: E402

SET = settings(max_examples=1500, deadline=None,
               suppress_health_check=[HealthCheck.too_slow])

# Printable text including unicode, punctuation, RTL, emoji.
text_st = st.text(
    alphabet=st.characters(blacklist_categories=("Cs",)),
    min_size=0, max_size=400)


# ---------------------------------------------------------------- compactor
@given(text_st)
@SET
def test_compact_never_crashes(t):
    pc.compact(t)


@given(text_st)
@SET
def test_compact_never_grows_much(t):
    """Compaction must not inflate input. Hoisting can add one 'Context: ' prefix."""
    r = pc.compact(t)
    assert r["compact_chars"] <= r["original_chars"] + len("\nContext: "), r


@given(text_st)
@SET
def test_compact_is_idempotent_ish(t):
    """Compacting twice must not keep shrinking without bound (must reach a fixpoint)."""
    a = pc.compact(t)["compact"]
    b = pc.compact(a)["compact"]
    c = pc.compact(b)["compact"]
    assert b == c, f"no fixpoint:\n1={a!r}\n2={b!r}\n3={c!r}"


DIGITS = re.compile(r"\d+")


@given(st.integers(min_value=1, max_value=99999), text_st)
@SET
def test_compact_preserves_numbers(n, t):
    """DOCUMENTED PROMISE: constraint-bearing tokens (numbers) are never dropped."""
    prompt = f"Hi, could you please make it retry exactly {n} times? Thanks!"
    out = pc.compact(prompt)["compact"]
    assert str(n) in out, f"lost number {n} -> {out!r}"


@given(st.text(alphabet="abcdefghijklmnopqrstuvwxyz ", min_size=1, max_size=40))
@SET
def test_compact_preserves_code_spans(body):
    assume("`" not in body)
    prompt = f"Hi, please explain what `{body}` does? Thanks!"
    out = pc.compact(prompt)["compact"]
    assert f"`{body}`" in out, f"code span mangled: {out!r}"


# ---------------------------------------------------------------- spine
@given(text_st)
@SET
def test_classify_never_crashes(t):
    c = spine.classify(t)
    assert c["verdict"] in {
        "NEUTRAL", "PURE SOCIAL PRESSURE", "NEW EVIDENCE",
        "EVIDENCE (with heat)", "EVIDENCE BURIED IN PRESSURE"}


@given(text_st)
@SET
def test_scores_non_negative(t):
    c = spine.classify(t)
    assert c["evidence_score"] >= 0 and c["pressure_score"] >= 0


@given(text_st)
@SET
def test_evidence_never_yields_pure_pressure(t):
    """INVARIANT: if any evidence is detected, the verdict must not be PURE SOCIAL PRESSURE.
    Violating this means a real fact could be dismissed as mere pressure."""
    c = spine.classify(t)
    if c["evidence_score"] > 0:
        assert c["verdict"] != "PURE SOCIAL PRESSURE", c


@given(text_st)
@SET
def test_guard_only_when_not_neutral(t):
    """A guard must never fire on a NEUTRAL message (that would be crying wolf)."""
    c = spine.classify(t)
    g = spine.GUARDS.get(c["verdict"], "")
    if c["verdict"] == "NEUTRAL":
        assert g == ""
    else:
        assert g != ""


@given(text_st)
@SET
def test_classification_deterministic(t):
    assert spine.classify(t) == spine.classify(t)


# ---------------------------------------------------------------- register
@given(text_st, st.sampled_from(["low", "normal", "high"]),
       st.sampled_from(["cold", "warm"]))
@SET
def test_register_never_crashes(t, stakes, rapport):
    r = reg.pick(t, stakes, rapport)
    assert r["register"] in {"PLAIN", "COMIC (optional)"}


@given(text_st, st.sampled_from(["cold", "warm"]))
@SET
def test_high_stakes_never_comic(t, rapport):
    """DOCUMENTED PROMISE: comedy is blocked when stakes are high."""
    r = reg.pick(t, "high", rapport)
    assert r["register"] == "PLAIN", r


@given(text_st, st.sampled_from(["low", "normal", "high"]))
@SET
def test_cold_rapport_never_comic(t, stakes):
    r = reg.pick(t, stakes, "cold")
    assert r["register"] == "PLAIN", r


GRIEF = ["funeral", "died", "passed away", "my grandfather", "my mother", "cancer"]


@given(st.sampled_from(GRIEF), text_st)
@SET
def test_grief_always_blocks_comedy(word, t):
    r = reg.pick(f"{t} {word}", "low", "warm")
    assert r["register"] == "PLAIN", (word, r)


# ---------------------------------------------------------------- quarry
@given(text_st, st.integers(min_value=0, max_value=200), st.booleans())
@SET
def test_opening_never_crashes(t, turns, urgent):
    quarry.read_opening(t, turns, urgent)


@given(text_st, st.integers(min_value=0, max_value=200))
@SET
def test_urgent_always_blocks(t, turns):
    """GOVERNING CLAUSE: utility is immediate and unconditional."""
    r = quarry.read_opening(t, turns, urgent=True)
    assert r["blocked"], r


BLOCKERS = ["production", "broken", "urgent", "medical", "legal", "how do i", "what is"]


@given(st.sampled_from(BLOCKERS), text_st, st.integers(min_value=0, max_value=200))
@SET
def test_utility_blockers_always_block(word, t, turns):
    r = quarry.read_opening(f"{t} {word}", turns, urgent=False)
    assert r["blocked"], (word, r)


@given(text_st)
@SET
def test_seed_never_crashes(t):
    s = quarry.find_seed(t)
    assert set(s) == {"emotional_seeds", "costumes", "odd_words", "repeated_words"}
