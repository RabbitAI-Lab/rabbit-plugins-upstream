# RESIDUAL RISK — backup-chain (the acceptable-risk line, v1.1)

This annex is the line, not a disclaimer. It says what this skill does **not**
protect against, in one place, versioned with the code — so that every future
control addition has to pay for itself in honesty before it pays for itself in
safety.

## Standing premise

Nothing here is guaranteed. The protocol operates with probabilities: an
error probability that looks negligible will be ignored until it fires
spectacularly, and the correct response to that fact is not infinite
hardening — it is an explicit line between acceptable and unacceptable risk,
drawn *before* the strive for control ruins everything, the operators
included. Of the three values this kind of engineering usually serves —
scientific detachment, efficiency, control — control is the one whose
uncorrected excess does the most damage, because every control is also a new
failure surface wearing the costume of a fix.

## What backup-chain does NOT protect against

1. **Operator coercion or compromise.** The human is inside the trust
   boundary by definition. A coerced operator acks lies, approves bad
   registrations, and can rewrite every doc you are reading.
2. **Full workspace compromise at build or restore time.** An attacker who
   controls the machine controls the bytes, the manifest, the trace, and the
   drill. The chain detects accidents and infrastructure amnesia; it does not
   detect malice with build-time access.
3. **Ledger + writer co-subversion.** If the ledger channel *and* the
   workspace are subverted in coordination, the two-witness model of v1.1
   adds no separation — its alarms all come from witnesses that fail
   together.
4. **Silencing.** Deleting the archive store and the ledger together ends the
   chain. Append-only is not indestructible; it is unforgeable-in-place at
   best, and only until silenced.
5. **The restoring process itself.** G1–G8 verify the archive's past; they
   cannot verify the process doing the restoring, the target filesystem's
   future, or the operator reading the output.
6. **Shared-ledger counter fights.** Two chains pointed at one ledger channel
   will fight over the generation counter — visibly, but only to someone who
   reads the ledger.
7. **The witness lying surfaces.** Decision traces, acks, and event lines are
   authored text and forgeable like any ledger text. What bounds the damage:
   traces make checkable claims (`b` vs the member map, `f` by construction),
   so a lie tends to leave a detectable disagreement with evidence that
   survived it. *Tends to* — that is a probability, priced honestly.
8. **Everything not listed.** The absence of a risk from this list means it
   was not seen, not that it does not exist. That is the standing blind spot,
   and it belongs at the end of every version of this annex.

## The standing rule (control-inflation guard)

> **Every future control addition must name, in the same version, the blind
> spot it creates — or it is refused as control-inflation.**

This is the meta-failsafe: failsafes fail from blind spots, and naming the
blind spot is the only failsafe on failsafes that does not multiply them. In
practice, for every proposed feature or gate, answer three questions in the
changelog entry:

- What new failure does this control itself introduce? (If the answer is
  "none," the answer is wrong — look again.)
- Which witness does it duplicate, and what does the duplication cost?
- Does its failure mode fail loud (marked, refused) or silent? Silent
  failures are refused on sight.

## Language discipline

Words are the cheapest place a risk line erodes. Across all v1.1+ documents
and command output:

- **Permitted:** *witness, raises cost, probability shift, detects, marks,
  refuses, evidence, alarm.*
- **Forbidden:** *guarantee, tamper-proof, secure against, unforgeable,
  prevents.* (Where this annex says "unforgeable-in-place" above, read it as
  shorthand for "rewriting in place is detectable by the hash chain" — which
  itself assumes the hashes were not computed by the attacker. See item 2.)
- **The list is an example set, not the discipline.** A banned-word filter
  only stops the exact strings on it; it does nothing about a synonym that
  quietly imports the same certainty a banned word carried — "impossible to
  alter unnoticed," "immune to silent rewrite," "ensures integrity" claim
  exactly what "tamper-proof" claims, and are equally forbidden. Whoever
  edits this annex or SECURITY.md checks new wording against the *claim*
  (does this still say something no probability can back?), not against
  whether it happens to dodge the four words above. An automated version of
  this check — scoring prose against a similarity model — was considered and
  rejected here: this codebase has no embedding model, no semantic-distance
  scorer, and (for command output) no access to whatever process is calling
  it, so a "detector" built from what's actually on hand would be a keyword
  list with extra steps, claiming a rigor it doesn't have. That is precisely
  the control-inflation the standing rule below refuses — a check does not
  get to skip paying for itself in honesty just because it sounds like it
  measures something.

## Versioned movement

The risk line moves only by an explicit decision recorded in this annex with
the version that moves it, never by silent accumulation of one more
harmless-seeming check. If a change and its annex entry cannot be written in
the same commit, the change waits.
