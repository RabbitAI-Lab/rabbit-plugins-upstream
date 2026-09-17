## Description:

Operate Checkly through an OOMOL-connected account using the oo CLI to retrieve checks, check results, statuses, and account details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Checkly account data, checks, statuses, and recent check results through an OOMOL-connected oo CLI workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on OOMOL as the credential broker for Checkly account access.

Mitigation: Install and use it only when the user accepts OOMOL-managed Checkly credentials, and treat sign-in plus connection setup as explicit account-changing steps.

Risk: Fallback setup documents remote installer commands for the oo CLI.

Mitigation: Prefer a verified or package-manager install path, or review the installer source before running remote install commands.

Risk: Connector actions execute against a live Checkly account using server-side credentials.

Mitigation: Fetch the live action schema before each payload and get explicit user approval before any future write or destructive action.

## Reference(s):

- [Checkly homepage](https://www.checklyhq.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-checkly)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, text]

**Output Format:** [Markdown guidance with inline shell commands and JSON output from the oo CLI]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; normal documented actions are read-oriented.]

## Skill Version(s):

1.0.2 (source: server evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
