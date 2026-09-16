## Description:

Operates HTML/CSS to Image through OOMOL's oo CLI for creating images from HTML/CSS or public URLs, retrieving usage metrics, and deleting generated images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage HTML/CSS to Image tasks through an OOMOL-connected account, including image creation from markup or webpage URLs, usage reporting, and approved deletion workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence flags first-time setup instructions that run remote installer scripts directly in a shell.

Mitigation: Review installation steps before use, install the oo CLI through a trusted and verifiable method, and do not let an agent run remote installer commands automatically.

Risk: Write and destructive connector actions can create images or delete generated images and cached content.

Mitigation: Confirm the exact action, target, payload, and expected effect with the user before running write or destructive actions.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/oomol/skills/oo-htmlcsstoimage)
- [HTML/CSS to Image homepage](https://htmlcsstoimage.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce oo CLI commands that call HTML/CSS to Image connector actions and return JSON responses.]

## Skill Version(s):

1.0.3 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
