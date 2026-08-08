## Description:

LYGO Ops Detector is a local deterministic CLI skill that scores operator-supplied text for evasion, coordination, and policy-refusal discourse signals while excluding identity profiling and doxing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[deepseekoracle](https://clawhub.ai/user/deepseekoracle)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agent operators use this skill to run reproducible local checks on pasted or consented text for discourse-pattern signals, inspect JSON or text reports, show signal boundaries, and rerun the public labeled evaluation suite.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Heuristic false positives or false negatives could cause reputational harm if scores are treated as proof about a person.

Mitigation: Treat outputs as weak discourse signals only; require human review, primary sources, and cited pattern hits before any consequential action.

Risk: Private messages, logs, or association strings may contain sensitive data.

Mitigation: Prefer redacted pasted text; use file inputs only when the operator has authority and passes --i-consent.

Risk: The tool could be misused for identity, profession, affiliation, or social-graph profiling.

Mitigation: Invoke only for explicit ops-detector or evasion-index requests, analyze text rather than people, and do not score bare job or affiliation labels as operational signals.

Risk: Short-suite calibration metrics can be mistaken for production performance.

Mitigation: Use the documented operational bar for strong language, present calibration only as ranking evidence, and rerun the evaluation suite after pattern changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/deepseekoracle/skills/lygo-ops-detector)
- [Project homepage](https://github.com/DeepSeekOracle/lygo-protocol-stack)
- [AETHON D9 blueprint](references/AETHON_D9_BLUEPRINT.md)
- [Security and ethics notes](references/SECURITY.md)
- [SkillSpector audit response](references/SKILLSPECTOR_AUDIT.md)
- [Labeled discourse evaluation suite](tests/labeled_discourse_suite.json)
- [Last evaluation report](tests/last_eval_report.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Plain text or JSON reports, markdown guidance, and runnable Python CLI commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Core analysis is local and deterministic; file-based inputs require operator consent; evaluation report writes are constrained to tests/.]

## Skill Version(s):

1.2.2 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
