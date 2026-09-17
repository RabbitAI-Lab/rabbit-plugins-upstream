## Description:

Gorgias lets an agent search and read Gorgias account, ticket, customer, tag, and user data through an OOMOL-connected oo CLI account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and support teams use this skill to retrieve Gorgias helpdesk data through the OOMOL connector instead of calling the Gorgias API directly. It is focused on read-only account, ticket, customer, tag, and user lookup workflows with live schema inspection before each action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup instructs users to run remote installer scripts directly in a shell.

Mitigation: Review the installer path before use; prefer a signed or package-manager installation source, or download and verify the installer before running it.

Risk: The skill can read data exposed by the connected Gorgias account through OOMOL.

Mitigation: Connect only the intended Gorgias account and ensure its scopes expose only the data the agent should access.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-gorgias)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Gorgias homepage](https://www.gorgias.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live oo connector schemas before constructing action payloads; connector responses include data and execution metadata.]

## Skill Version(s):

1.0.2 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
