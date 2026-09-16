## Description:

Cloudflare Worker lets an agent read, create, update, and delete Cloudflare Worker data through the OOMOL Cloudflare Worker connector instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to inspect live Cloudflare Worker connector schemas and run JSON-based actions for Worker scripts, builds, accounts, settings, secrets, and logs through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote shell installer commands for the oo CLI.

Mitigation: Install the oo CLI only through a verified release or package path instead of letting the agent run remote installer commands directly.

Risk: The skill can perform write, destructive, and secret-related Cloudflare Worker operations through a connected account.

Mitigation: Require explicit user confirmation of the target, payload, and expected effect before running write, delete, overwrite, or secret-read actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-cloudflare-worker)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Cloudflare Workers](https://workers.cloudflare.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before running actions; write, destructive, and secret-related operations require explicit confirmation.]

## Skill Version(s):

1.0.6 (source: server release evidence and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
