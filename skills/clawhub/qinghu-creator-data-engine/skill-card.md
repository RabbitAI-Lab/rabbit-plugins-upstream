## Description:

Qinghu AI Creator Data Engine helps an agent collect creator account metrics from Douyin, Xiaohongshu, and Bilibili profile URLs and export standardized Excel reports for competitor-account and creator-partner monitoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and operators use this skill to collect creator account metrics from supported social-platform profile links, monitor competitor accounts, track partner creators, and export standardized Excel data tables. The skill is intended for single-run data export workflows backed by QHKit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release security summary says the skill gives the agent broad setup and credential-handling authority.

Mitigation: Install only when QHKit creator-data exports are intended, confirm any Node or package installation before execution, and use a managed secret or environment variable for the token.

Risk: The workflow can submit paid generate actions that consume Qinghu credits.

Mitigation: Run an estimate first, report the expected credit cost, and require explicit user approval before any generate action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-creator-data-engine)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with bash and JSON examples; QHKit returns JSON status and Excel file links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The workflow accepts up to five creator profile links per submission and produces XLSX data tables when the remote job completes.]

## Skill Version(s):

0.1.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
