## Description:

OnePageCRM (onepagecrm.com). Use this skill for reading, creating, and updating CRM contacts and deals through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to operate OnePageCRM workflows through the OOMOL connector, including listing, retrieving, and creating contacts and deals. Write actions should be used only after confirming the exact payload and effect with the user.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote installer pipe commands for the OOMOL CLI.

Mitigation: Avoid automatic approval of those commands; independently verify the installer or use a signed or package-managed installation path.

Risk: The skill can create CRM contacts and deals, changing OnePageCRM data.

Mitigation: Run write actions only for user-directed work and confirm the exact JSON payload and expected effect before execution.

## Reference(s):

- [OnePageCRM homepage](https://www.onepagecrm.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-one-page-crm)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; connector responses are JSON.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
