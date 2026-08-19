## Description:

Helps an agent answer or plan work by read-only lookup of locally organized project history, file summaries, stable knowledge, decisions, rules, and prior troubleshooting experience.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zzusp](https://clawhub.ai/user/zzusp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill when current work may depend on prior local project context, file summaries, historical decisions, stable rules, or similar past failures. It narrows candidates through local indexes, checks source records or current files, and answers only from verified read-back evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill automatically consults a broad local knowledge store, which can mix records from unrelated projects, customers, or sensitive contexts.

Mitigation: Review the contents and boundaries of ~/.agent-knowledge/ before use, and avoid deployment where cross-project or sensitive records should not be queried together.

Risk: Stored indexes and summaries may be stale, incomplete, or inconsistent with current files.

Mitigation: Treat indexes as navigation aids only, verify conclusions against source records or the current workspace, and state evidence gaps when records are missing or inconsistent.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zzusp/skills/use-self-improving)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Analysis]

**Output Format:** [Natural-language answer or guidance, typically in Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only local knowledge lookup; does not write, correct, archive, or delete knowledge-base content.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
