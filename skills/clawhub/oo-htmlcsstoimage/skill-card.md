## Description:

Operates HTML/CSS to Image through OOMOL's oo CLI to create images from HTML/CSS or public webpage URLs, retrieve usage metrics, and delete generated images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate an HTML/CSS to Image account from an agent workflow. It supports generating images, checking usage, and deleting generated assets through the OOMOL-connected oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include direct execution of internet-downloaded installer scripts.

Mitigation: Install the oo CLI from a verified package source, or download and inspect or verify the installer before executing it.

Risk: Create and delete actions can change or remove assets in the connected HTML/CSS to Image account.

Mitigation: Confirm the exact action payload and target resources with the user before running write or destructive commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-htmlcsstoimage)
- [HTML/CSS to Image homepage](https://htmlcsstoimage.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May run HTML/CSS to Image create/delete actions through the OOMOL-connected oo CLI after user confirmation for write or destructive actions.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
