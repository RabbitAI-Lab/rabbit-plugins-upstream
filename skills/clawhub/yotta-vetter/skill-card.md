## Description:

Yuanshen (元审) is a pre-install skill security review protocol that guides source, code, permission, and risk checks, then produces an initial vetting report with optional deep-scan handoff.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers, security reviewers, and agent users use this skill before installing or evaluating unknown skills to create a structured initial security review and record a human-confirmed install decision.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may treat the initial vetting report as a final security decision.

Mitigation: Use the report as a review aid and require human confirmation before installing or rejecting a skill.

Risk: Broad installation modes can affect more agent environments than intended.

Mitigation: Use --agent or --dir for a single target agent unless broad installation is intentional.

Risk: Source metadata checks may rely on optional GitHub access or cached information.

Mitigation: Review source-check results as contextual evidence and continue manual review when network metadata is unavailable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-vetter)
- [Four-phase vetting checklist](references/checklist.md)
- [Vetting report template](references/vetting-report-template.md)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-vetter)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Plain text, JSON, and Markdown reports with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are review aids and require human confirmation before acting on installation decisions.]

## Skill Version(s):

0.1.5 (source: SKILL.md frontmatter, package.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
