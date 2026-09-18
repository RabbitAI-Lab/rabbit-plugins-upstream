## Description:

HR Partner (hrpartner.io). Use this skill for HR Partner requests that search and read employee, recruiting, company, and lookup data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and operators with authorized HR Partner access use this skill to retrieve read-only personnel, recruiting, company, and lookup records. The agent inspects the live action schema before running HR Partner connector actions with JSON payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup flow includes remote installer commands that could be unsafe if run blindly.

Mitigation: Install only from trusted OOMOL sources, prefer verified or pinned installation instructions, and inspect installer scripts before execution.

Risk: Connected HR Partner accounts can expose sensitive personnel and recruiting records.

Mitigation: Use authorized accounts with least-privilege access and avoid requesting or sharing records that are not needed for the task.

## Reference(s):

- [ClawHub HR Partner skill page](https://clawhub.ai/oomol/skills/oo-hr-partner)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [HR Partner homepage](https://www.hrpartner.io/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector results are expected as JSON responses for read-only HR Partner lookup and listing actions.]

## Skill Version(s):

1.0.2 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
