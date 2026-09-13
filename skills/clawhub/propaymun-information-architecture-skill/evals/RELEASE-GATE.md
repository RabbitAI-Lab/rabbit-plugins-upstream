# Release gate: 1.0.0

Version 0.6.0 supplied the broad-test evidence used to prepare 1.0.0. The 1.0.0 release combines the subsequent Claude and Gemini human evaluations, the expanded behavioral catalog, deterministic regression tests, package-parity checks, and a consolidated review of the built artifacts. Isolated preference or one model response remains insufficient to change the operating contract.

## Test matrix

Record the exact artifact revision, host/model context, language, input fixture, observed response, expected behavior, pass/fail reason, and unmeasured evidence layers.

Install the isolated evaluation dependency from `evals/requirements.txt`, then run `scripts/validate_eval_cases.py` before behavioral execution. This validates catalog structure, not model behavior. Execute atomic cases for breadth and every journey for depth; do not promote from atomic checks alone.

Cover at least:

- early idea, detailed brief, audit/revision, and downstream transformation;
- novice `I don't know`, mixed-confidence answers, and expert direct requests;
- canonical IA, standalone product sitemap, standalone user flow, and a compound request;
- Persian RTL and English LTR, with locale kept separate from language;
- native Agent Skill and Workspace/Knowledge Markdown routes;
- proactive retrieval, cross-project conflict, explicit persistence, unavailable memory, embedded instruction, missing capability, and unrequested file/export cases;
- semantic consistency, interaction burden, token discipline, and reference-lock fidelity;
- plain-language uncertainty, bilingual duplication, unsupported product commitments, stage-complete summaries, stop compliance, and optional-next-step behavior;
- destination/view/state/capability separation and rendered user-flow branch legibility.
- at least three reproducible multi-turn journeys, including a real phase closure, a memory collision, and a requested companion artifact;
- Agent Skill versus Workspace Kit semantic parity on the same brief without requiring identical wording.

## Promotion criteria

Promote to 1.0.0 only when:

1. deterministic tests, package parity, schema/fixture checks, and security regressions pass;
2. no critical rubric invariant fails in the consolidated cross-host evidence;
3. the new companion artifacts do not weaken the IA core or change its canonical source;
4. users receive a useful coherent pass without serial interrogation;
5. portable Markdown behaves as operating guidance in file-only environments without claiming unsupported installation;
6. documentation, package names, manifests, changelog, version, and downloadable artifacts agree;
7. remaining limitations are explicit and do not invalidate the intended use;
8. ordinary novice-facing responses do not leak internal status/control labels or silently optimize for registration, conversion, activation, or retention;
9. rendered flow diagrams are visually inspected, while text-only and syntax-only outputs make no visual-QA claim.
10. phase closure works without forcing continued work, and cross-session continuation remains portable when native memory is absent.
11. the exact release artifacts pass both atomic breadth cases and all critical multi-turn journeys with recorded raw outputs and host events.

At promotion, fix only evidenced defects or high-confidence clarity issues. Defer speculative expansion to post-1.0 feedback.
