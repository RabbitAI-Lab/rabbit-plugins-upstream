## Description:

Doubao Seedream helps an agent generate or edit images through an OOMOL-connected Doubao Seedream connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to inspect the Doubao Seedream action schema, build a matching JSON payload, and run image generation or image editing actions through the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Image-generation actions may process user prompts or image inputs externally and may consume account credit.

Mitigation: Confirm the exact prompt, image inputs, output count, and expected billing impact with the user before running generation or editing actions.

Risk: The skill recommends remote pipe-to-shell installer commands for first-time setup.

Mitigation: Avoid pipe-to-shell installation unless the installer source and integrity have been independently verified.

Risk: The release security verdict is suspicious because the skill under-describes image-generation and billing impact.

Mitigation: Review the skill before installation and treat it as an external image-generation connector rather than a read-only helper.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-doubao-seedream)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Doubao Seedream homepage](https://www.volcengine.com/product/ark)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce structured JSON payloads for oo CLI connector actions and should surface execution metadata when actions run.]

## Skill Version(s):

1.0.2 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
