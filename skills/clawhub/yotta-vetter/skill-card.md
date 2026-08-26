## Description:

元审 yotta-vetter helps agents perform a four-stage pre-install skill safety review covering source, code, permissions, and risk, with lightweight local checks and optional GitHub source metadata.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill before installing or evaluating unknown agent skills from marketplaces, GitHub, or shared packages. It produces an initial vetting report and decision record, while leaving the final install decision to a human reviewer.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads the target skill directory during review.

Mitigation: Run it only against skill directories intended for review and avoid pointing it at unrelated sensitive folders.

Risk: The skill can write a report to a user-provided path.

Mitigation: Choose an explicit report destination and review generated findings before acting on them.

Risk: The source-check command may contact GitHub for repository metadata.

Mitigation: Use the source check only when that network lookup is acceptable; otherwise rely on local check mode and documented manual review.

Risk: Installing globally can activate the skill across multiple agents.

Mitigation: Install it only into the agent intended for use unless cross-agent activation is deliberate.

Risk: The checker provides an initial assessment and can miss context-specific risk.

Mitigation: Keep the documented human review step as the final decision point, especially for medium or higher findings.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-vetter)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-vetter)
- [Four-stage checklist](references/checklist.md)
- [Vetting report template](references/vetting-report-template.md)
- [Yotta Security Audit](https://github.com/YottaMeta/yotta-security-audit)
- [Yotta Memory](https://github.com/YottaMeta/yotta-memory)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Plain text reports, JSON summaries, Markdown vetting reports, and suggested shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional report-file output; GitHub source checks use metadata lookup with local cache fallback.]

## Skill Version(s):

0.1.2 (source: SKILL.md frontmatter, package.json, release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
