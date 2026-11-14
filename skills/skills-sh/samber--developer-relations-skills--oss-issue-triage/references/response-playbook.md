# Response playbook

Contents:

- the per-item decision path
- reply templates with weak/strong pairs
- pull-request deltas
- the rejection knowledge base

## Per-item decision path

Run the same five questions on every item, stopping at the first that resolves it. The order is queue removed per minute spent, not cost: duplicates and already-shipped items lead because each closes an item outright for a search, while the scope decision costs the most thought and only hands the item onward.

- efficiency: duplicate > already answered or shipped > actionable as written > in scope > accept and classify
- effort: duplicate == already answered (one search each) > actionable as written (read the report against a required-fields list) > accept and classify (three axes to set) > in scope (the judgment that starts arguments, and the one that escalates)

The effort tie is real: both are a single search, and which runs first is a coin flip. Re-rank against the queue's shape - a tracker that is mostly usage questions resolves more items on question 2 than on question 1.

1. **Duplicate?** Search by concept, not by the reporter's wording. If it is one, link both directions and close the newer.
2. **Already answered or shipped?** Point at the release, docs page or code, then close.
3. **Reproducible / actionable as written?** A bug needs an environment and a reproduction; a feature request needs a problem statement. If a required element is missing, ask for exactly that one thing and set the waiting-on-reporter state.
4. **In scope?** Decide against the project's stated scope, not against how convincing the reporter is. Out of scope → decline, record why (rejection knowledge base below), close.
5. **In scope and real?** Set type, priority and area, then assign it or mark it unstaffed. "Accepted" without an owner is an honest state; "accepted" implying someone is working on it is not.

Time-box the pass. Most items resolve in under two minutes; the ones that do not are worth batching for a maintainer decision rather than blocking the queue.

## Reply templates

Fill the bracketed parts with specifics from the item. Generic replies read as form letters and produce another round-trip.

**Needs information**

```
Thanks for the report. To reproduce this I need [the exact missing element:
version + OS, or a minimal script using only project APIs].

What we know so far:
- [established fact 1]
- [established fact 2]

I have set [state label]; comment with that and it goes back in the queue.
Without it I will close this in [N] days, and you can reopen any time.
```

Weak: "Please provide more information." The reporter cannot tell what is missing, so the round-trip repeats.
Strong: "I need the output of `tool --version` and the config file with secrets removed." One specific ask, answerable in a minute.

Record what is already established, or a resumed conversation re-asks resolved questions - the fastest way to lose a reporter who was still willing to help.

**Support question routed off the tracker**

```
This is a usage question rather than a defect, so it belongs in [forum / chat /
discussions link] where more people will see it and the answer stays findable.
Short answer: [answer it anyway, in one or two lines].
```

Answering while redirecting makes the redirect land as help rather than a brush-off. A third arrival of the same question is a documentation defect - route it to a docs page instead of a fourth answer.

**Out of scope**

```
Thanks for taking the time to write this up. [Feature] is out of scope for the
project because [reason tied to stated scope, one sentence]. [Link to the
scope statement or the prior decision.] [Where to get it instead, if anywhere.]
Closing: the reasoning is recorded in [link] so it does not get re-litigated.
```

Weak: closing with no comment, or "not planned". Both read as dismissal and reliably generate a follow-up issue.
Strong: two sentences, a reason, a link, a door left open for a different framing of the problem.

**Confirmed bug, unstaffed**

```
Reproduced on [version/environment]: [what happens]. Setting [labels].
Nobody is working on this right now; [contribution pointer].
```

An honest "real, unstaffed, no date" ages far better than silence or an optimistic estimate.

## Pull requests

A pull request is an issue with code attached: same states, same clocks, three deltas.

- **Verify the claim against the diff**, not the description - check it out, run the tests, say what happened.
- **Route by ownership** (owner file, area label) before review, so the wait sits on a named person rather than the queue.
- **Stale-PR cost is asymmetric.** An unanswered issue costs the reporter nothing after they walk away; an unanswered PR cost someone hours already spent. Give PRs the tighter first-response target when capacity forces a choice.
- Externally-authored PRs are triage work; a maintainer's own in-flight PR is not.

## Rejection knowledge base

Keep one file per rejected _concept_ (not per issue) - `dark-mode.md`, `plugin-system.md` - each holding the decision, the reasoning and the prior issues that asked for it. When the request returns under a new name, link the file instead of re-arguing. The reasoning then survives the maintainer who made the call, and a contributor considering the same work reads the answer before writing code.

Rejected requests only. Something already implemented gets a pointer to where it lives.

## Tone rules that hold everywhere

- Thank first, decide second, close third - in that order, in two sentences.
- Never close silently; every close carries its reason, even one line.
- First-time reporters get the patient version, frequent contributors the terse one. The difference is deliberate.
- Disclose machine-generated triage comments; reporters can tell anyway, and undisclosed automation reads as contempt.
- Hostile or abusive behaviour is not a triage decision - hand it to the conduct process.
