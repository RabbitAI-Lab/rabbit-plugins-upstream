## Description:

ImageTranslate.AI lets an agent translate text in public images through the OOMOL oo CLI connector while preserving layout and returning a rendered PNG.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to translate text in public images with ImageTranslate.AI from an agent workflow after inspecting the live connector schema and supplying a matching JSON payload.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The translate_image action may incur ImageTranslate.AI charges even though the artifact does not label it as a write action.

Mitigation: Confirm the user's intent, image URL, output settings, and possible cost before running translate_image.

Risk: Connector inputs can be malformed if the action schema is assumed from stale documentation.

Mitigation: Inspect the live connector schema before constructing the JSON payload.

Risk: Authentication, connection, or billing issues can block execution.

Mitigation: Use the first-time setup and billing guidance only after a matching command failure.

## Reference(s):

- [ImageTranslate.AI homepage](https://imagetranslate.ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-imagetranslate-ai)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance, Files]

**Output Format:** [Markdown with inline shell commands and JSON connector payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return a rendered PNG up to 50 MB through transit storage.]

## Skill Version(s):

1.0.0 (source: release evidence and frontmatter metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
