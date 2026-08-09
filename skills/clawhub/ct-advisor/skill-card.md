## Description:

Ct Advisor Claw helps clinical-trial teams answer methodology, design, regulatory, quality-control, and operational questions, and routes sample-size, registry, safety, literature, and competitive-intelligence needs to related ct-series skills.

This skill is ready for commercial/non-commercial use.

## Publisher:

[medstatstar](https://clawhub.ai/user/medstatstar)

### License/Terms of Use:

MIT

## Use Case:

Clinical-trial practitioners, clinicians, nurses, and medical students use this skill to get structured clinical-development guidance and route data or computation requests to sibling skills. Outputs should be reviewed against official sources before regulatory submissions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends every user question and draft answer to the author-hosted Coze endpoint by default.

Mitigation: Do not use it with confidential sponsor strategy, unpublished trial data, patient information, credentials, or regulated internal documents unless the external processor is approved.

Risk: Automatic sanitization may not remove all sensitive or identifying information before outbound processing.

Mitigation: Users should remove sensitive details before prompting and validate organizational approval for any external transmission.

Risk: Clinical and regulatory guidance may be incomplete or unsuitable for a specific submission or jurisdiction.

Mitigation: Review outputs against official sources and qualified clinical, statistical, regulatory, or legal reviewers before operational or submission use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/medstatstar/skills/ct-advisor)
- [Project homepage](https://github.com/medstatstar/ct-advisor)
- [English README](https://github.com/medstatstar/ct-advisor/blob/main/README.md)
- [Chinese README](https://github.com/medstatstar/ct-advisor/blob/main/README_zh-CN.md)
- [Workflow steps](references/steps.md)
- [External search-site routing table](references/search-sites.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Shell commands, Configuration]

**Output Format:** [Markdown conversational answers with occasional inline commands or configuration notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include citations, official-source verification notes, routing summaries, or handoff instructions for sibling skills.]

## Skill Version(s):

0.9.50 (source: artifact/SKILL.md frontmatter and evidence.release.version, released 2026-08-09)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
