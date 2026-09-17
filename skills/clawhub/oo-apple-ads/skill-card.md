## Description:

Operate Apple Ads through an OOMOL-connected account for reading, creating, updating, deleting, and reporting on Apple Ads data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and advertising operators use this skill to inspect live Apple Ads connector schemas and run actions for account, campaign, ad group, creative, keyword, reporting, location, brand, and budget workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can run high-impact Apple Ads budget, bidding, create, update, and delete actions.

Mitigation: Require explicit user review of the selected action, target resources, payload, and expected effect before any write or destructive connector run.

Risk: First-time setup includes pipe-to-shell installer commands for the oo CLI.

Mitigation: Verify the installer through a trusted channel or use a safer installation path before running installer commands.

Risk: The connector operates through an OOMOL-connected Apple Ads account with server-side credentials.

Mitigation: Install and use the skill only when the OOMOL publisher and the connected Apple Ads account permissions are trusted.

## Reference(s):

- [ClawHub Apple Ads Skill Page](https://clawhub.ai/oomol/skills/oo-apple-ads)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Apple Ads](https://ads.apple.com/)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector actions may read, create, update, or delete Apple Ads resources depending on the selected action.]

## Skill Version(s):

1.0.2 (source: evidence release and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
