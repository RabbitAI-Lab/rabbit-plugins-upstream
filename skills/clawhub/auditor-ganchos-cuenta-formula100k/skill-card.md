## Description:

Audits an Instagram or TikTok account's recent short-form videos to compare top and bottom performers and produce hook-pattern findings, report assets, and editor-ready content concepts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[formula100k](https://clawhub.ai/user/formula100k)

### License/Terms of Use:

MIT-0

## Use Case:

Content teams, creators, and social media strategists use this skill to audit recent account videos, identify the hook patterns separating high and low performers, and turn those findings into reports, HTML summaries, and new hook concepts. It supports account-level reverse engineering rather than single-hook scoring or from-scratch ideation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated HTML reports may include untrusted text from third-party social media accounts.

Mitigation: Use a fixed HTML template and safely serialize and escape captions, transcripts, comments, and account text before sharing or opening generated reports.

Risk: Optional memory, Second Brain, or Yapper handoffs can persist or publish user data beyond the immediate audit.

Mitigation: Require explicit user confirmation before any memory write, workspace copy, scheduling action, or publishing handoff.

Risk: Social media performance data can be incomplete or biased, especially for recent posts or small sample sizes.

Mitigation: Label recent-content bias, treat carrier analysis as signal rather than proof for small samples, and integrate first-party metrics only when the user provides them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/formula100k/skills/auditor-ganchos-cuenta-formula100k)
- [Publisher profile](https://clawhub.ai/user/formula100k)
- [HTML report template](artifact/references/html-template.md)
- [Higgsfield prompt templates](artifact/references/prompts-higgsfield.md)
- [Markdown report template](artifact/references/reporte-md-template.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown reports, single-file HTML, JSON datasets, image assets, shell commands, and chat summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create an audit folder with dataset JSON, hook images, optional image mockups, a Markdown report, an HTML report, optional scripts or calendar files, and a ZIP for sharing.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
