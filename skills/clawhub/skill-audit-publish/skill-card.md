## Description:

Audit and prepare OpenClaw skills for publication to ClawHub, SkillHub, and GitHub with sanitization checks and approval gates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and skill publishers use this agent to audit, sanitize, transform, and verify OpenClaw skills before publishing them across supported registries and GitHub.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary reports possible overwriting of original files and publishing to additional platforms beyond the requested destination.

Mitigation: Review proposed file operations and target platforms, work from a separate staging folder, and confirm the exact destinations before approving each external publish.

Risk: The security guidance says the scan covered only part of the package and some checks were partial.

Mitigation: Review the full package, including unresolved references and any content the scan could not fully inspect, before relying on the audit.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/haiyangchenbj/skills/skill-audit-publish)
- [Publish rules](references/publish-rules.md)
- [SkillHub publishing guide](references/skillhub-publish.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Files, Shell commands, Code]

**Output Format:** [Markdown checklists and approval summaries, with shell commands and publish-ready skill files when requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include a staged skill package, file manifest, and verification instructions.]

## Skill Version(s):

1.5.11 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
