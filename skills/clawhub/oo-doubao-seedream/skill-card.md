## Description:

Doubao Seedream lets agents generate or edit images through the OOMOL-connected Doubao Seedream connector using schema-validated oo CLI actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agent users use this skill to generate or edit images with Doubao Seedream through an OOMOL-connected account. It guides the agent to inspect live action schemas, build JSON payloads, and execute the `generate_image` action with confirmation for write behavior.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup directs users to install the oo CLI with a remotely fetched installer script.

Mitigation: Review the oo CLI installation path before installing and prefer official package-manager, signed, or checksum-verified installation steps.

Risk: Image generation and editing are write actions that may consume connected-account resources.

Mitigation: Confirm the exact image-generation payload and intended effect with the user before running the action.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-doubao-seedream)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Doubao Seedream Homepage](https://www.volcengine.com/product/ark)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces schema-first oo CLI commands and structured connector responses; write actions require payload confirmation.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
