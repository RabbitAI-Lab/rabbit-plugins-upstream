## Description:

Use when the user wants a concise daily or weekly site/growth standup from TrustGrowth history when connected or from validated available evidence and repository artifacts otherwise.

This skill is ready for commercial/non-commercial use.

## Publisher:

[trustgrowth](https://clawhub.ai/user/trustgrowth)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, SEO operators, and growth teams use this skill to generate concise daily or weekly site and growth standups from TrustGrowth history when connected, or from validated imported evidence and repository or audit artifacts otherwise.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may use configured analytics, SEO, or paid vendor connectors.

Mitigation: Use only connectors the user already trusts and has configured, review cost preflights before approving paid batches, and never expose credentials.

Risk: Missing helper documentation may leave source-selection workflows unclear.

Mitigation: Ask for clarification when referenced helper docs are unavailable instead of guessing connector behavior.

Risk: Standup summaries can overstate trend movement when no persisted comparison baseline exists.

Mitigation: State no comparable baseline when history is unavailable and keep unsupported values unknown.

## Reference(s):

- [Connectors and categories](references/connectors.md)
- [Reporting contract](references/reporting.md)
- [WHY-NOT-SLOP](https://github.com/techwright-lab/groundcrew-seo/blob/main/WHY-NOT-SLOP.md)
- [ETHICS](https://github.com/techwright-lab/groundcrew-seo/blob/main/ETHICS.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Concise Markdown standup summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Keeps each site summary brief, labels missing baselines, limits recommendations to at most one materially useful missing connector, and requires claims to trace to validated evidence.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
