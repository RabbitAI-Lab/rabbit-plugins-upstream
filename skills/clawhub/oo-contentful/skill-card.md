## Description:

Contentful helps agents read, create, and update Contentful data through the OOMOL oo CLI connector instead of calling the Contentful API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate Contentful through an OOMOL-connected account, including listing spaces, environments, content types, and entries, and creating or updating entries when explicitly reviewed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup recommends pipe-to-shell installation commands for the oo CLI.

Mitigation: Use a safer verified installation method for the oo CLI before installing or running connector actions.

Risk: OOMOL mediates access to the connected Contentful account.

Mitigation: Confirm the OOMOL account, connected Contentful workspace, and granted scopes are appropriate before use.

Risk: Create and update actions can change Contentful content.

Mitigation: Inspect the live action schema and require explicit review of the exact payload and expected effect before executing write actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-contentful)
- [ClawHub publisher profile](https://clawhub.ai/user/oomol)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Contentful homepage](https://www.contentful.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Write actions require explicit user review of the target payload and expected effect before execution.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
