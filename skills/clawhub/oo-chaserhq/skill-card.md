## Description:

ChaserHQ lets an agent search and read ChaserHQ customer, invoice, invoice history, organisation, and API status data through an OOMOL-connected oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let an agent retrieve ChaserHQ customers, invoices, invoice history, organisation details, and API status through the OOMOL-connected oo CLI. It is intended for read-oriented ChaserHQ workflows where credentials are managed by OOMOL rather than handled directly by the agent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote installer commands that pipe downloaded scripts directly into a shell.

Mitigation: Do not let an agent run remote installer commands automatically; install the oo CLI only from a verified source trusted by the user.

Risk: Future ChaserHQ actions that write, delete, overwrite, or otherwise change data could have account or business impact.

Mitigation: Require explicit user confirmation of the exact action payload and expected effect before running any non-read ChaserHQ action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-chaserhq)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ChaserHQ homepage](https://www.chaserhq.com/)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill directs the agent to inspect live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
