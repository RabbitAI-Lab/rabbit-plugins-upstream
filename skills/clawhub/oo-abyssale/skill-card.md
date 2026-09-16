## Description:

Abyssale lets an agent operate an OOMOL-connected Abyssale account to inspect designs, generate banners, create projects, and retrieve generated image metadata through the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, designers, and operations users use this skill to work with Abyssale assets from an agent, including listing designs and fonts, generating banner images, managing projects, and retrieving dynamic image URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes pipe-to-shell installer commands for the oo CLI.

Mitigation: Review before installing and prefer a verified manual or package-manager install path for the oo CLI.

Risk: Some Abyssale actions can create projects, dynamic image URLs, or generated assets.

Mitigation: Confirm the exact payload and expected effect with the user before running write-capable actions.

Risk: Banner generation may be treated as read-only even though it can create a generated asset.

Mitigation: Treat banner generation as an action that may change account state and confirm the request when appropriate.

## Reference(s):

- [Abyssale homepage](https://www.abyssale.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-abyssale)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return Abyssale connector JSON responses with data and execution metadata.]

## Skill Version(s):

1.0.4 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
