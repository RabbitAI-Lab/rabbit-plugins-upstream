## Description:

HighLevel (gohighlevel.com). Use this skill for HighLevel requests, including reading, creating, updating, and deleting contact data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate HighLevel contacts from an agent through an OOMOL-connected account. It supports contact lookup and search, plus confirmed create, update, and delete actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unverified remote script execution for installing the oo CLI.

Mitigation: Review the setup path before installation and prefer official, verifiable package-manager or checksum/signature-verified oo CLI installation steps.

Risk: The skill can create, update, and delete HighLevel CRM contacts.

Mitigation: Require the agent to confirm exact payloads and expected effects before write actions, and to get explicit approval before destructive delete actions.

## Reference(s):

- [HighLevel homepage](https://www.gohighlevel.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [HighLevel skill on ClawHub](https://clawhub.ai/oomol/skills/oo-high-level)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill instructs the agent to inspect each live action schema before constructing connector payloads.]

## Skill Version(s):

1.0.2 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
