## Description:

Audits Markdown for empty labels, duplicate URLs, raw URLs, suspicious schemes, and missing image alt text before publication.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hmahmadcs](https://clawhub.ai/user/hmahmadcs)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and documentation authors use this skill to review pasted Markdown or excerpts for link hygiene issues and get prioritized, minimally invasive fixes before publishing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live link checks may access URLs in user-provided Markdown.

Mitigation: Do not fetch links by default; require explicit approval for each URL before checking it.

## Reference(s):

- [Markdown Link Auditor on ClawHub](https://clawhub.ai/hmahmadcs/skills/markdown-link-auditor)
- [Publisher profile](https://clawhub.ai/user/hmahmadcs)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Categorized findings with short quotes and suggested rewrites, an issue count, and a prioritized checklist.]

## Skill Version(s):

1.0.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
