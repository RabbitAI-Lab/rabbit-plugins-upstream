## Description:

元审 yotta-vetter helps agents perform a pre-install skill security review using a four-phase source, code, permissions, and risk checklist plus a lightweight checker.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers, agent users, and reviewers use this skill before installing or evaluating skills from marketplaces, GitHub, or shared sources to produce a structured vetting report and identify whether human review or deeper scanning is needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The installer can persist the skill into multiple agent skill directories without a confirmation step.

Mitigation: Review the install command before running it; prefer --dir or --agent for one intended agent, avoid global installation unless deliberate, and remove the skill folder from any skills directory where it should not be active.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-vetter)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-vetter)
- [Agent Skills standard](https://agentskills.io/)
- [Four-phase vetting checklist](references/checklist.md)
- [SKILL VETTING REPORT template](references/vetting-report-template.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown report, optional JSON output, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include severity-filtered findings, source checks, verdicts, decision records, timestamps, and handoff guidance for deeper scanning.]

## Skill Version(s):

0.2.3 (source: SKILL.md frontmatter, CHANGELOG.md, package.json, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
