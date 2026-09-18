## Description:

Roboflow helps agents inspect connector schemas, read project and inference metadata, and run hosted object detection or workflows through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and workflow operators use this skill to interact with Roboflow projects, versions, inference servers, and workflows through an authenticated OOMOL connector without handling raw Roboflow API credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup instructions include direct execution of remote installer scripts.

Mitigation: Review setup instructions before installation and prefer a signed or package-manager-based oo CLI source, or download and verify the installer before running it.

Risk: The skill can submit image or runtime inputs to Roboflow workflow and object detection actions.

Mitigation: Confirm user intent and data sensitivity before sending private images or workflow inputs to the connected Roboflow service.

## Reference(s):

- [Roboflow homepage](https://roboflow.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Action schemas should be inspected before payload construction; connector responses include data and execution metadata.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
