## Description:

Pingdom skill for searching and reading uptime checks, account credits, and probe data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to inspect Pingdom uptime checks, account credits, and probe locations through the OOMOL oo CLI without handling raw Pingdom tokens.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that can execute code on the user's machine.

Mitigation: Review the installer source and prefer an official package manager or an installer with a published checksum or signature before running it.

Risk: Connecting Pingdom gives OOMOL-mediated access to Pingdom account data.

Mitigation: Connect only the intended Pingdom account, verify the live connector schema before each action, and limit use to the disclosed read operations unless the user explicitly authorizes a change.

## Reference(s):

- [ClawHub Pingdom skill page](https://clawhub.ai/oomol/skills/oo-pingdom)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Pingdom homepage](https://www.pingdom.com)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands call the OOMOL oo CLI and may return JSON data from Pingdom connector actions.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
