## Description:

Helps agents check factual claims in generated content against supplied sources and flag claims that lack support before publication.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content reviewers use this skill to check claims in AI-generated articles, reports, or replies against source material before publishing them as fact.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Declared permissions conflict with the documented local-file and web-search workflow.

Mitigation: Review the skill before installation, restrict access to intended claim and source files, and correct unnecessary Write access or inconsistent permissions metadata.

Risk: A source match may not establish that a claim is factually supported.

Mitigation: Check the cited source and claim manually before treating a supported label as publication-ready.

## Reference(s):

- [Fact Check Guard on ClawHub](https://clawhub.ai/zhaoxinghua09-cell/skills/fact-check-guard)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Plain text or JSON with per-claim labels and explanations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Labels claims supported, dubious, or unsourced; source matches need human review before publication.]

## Skill Version(s):

1.0.4 (source: ClawHub release metadata; bundled skill frontmatter says 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
