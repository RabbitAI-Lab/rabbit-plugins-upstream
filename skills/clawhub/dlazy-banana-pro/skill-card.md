## Description:

Generate and edit images with Nano Banana Pro using text-to-image and image-to-image workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to ask an agent to generate or edit images through the dLazy Nano Banana Pro CLI. It supports prompts, reference images, aspect ratio selection, output size selection, dry runs, and asynchronous generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and referenced image files may be sent to dLazy cloud services.

Mitigation: Install and use the skill only when cloud processing by dLazy is acceptable for the intended prompt and media content.

Risk: The dLazy API key can be stored in a local CLI configuration file.

Mitigation: Use OS account protections, rotate or revoke keys from the dLazy dashboard when needed, and prefer per-invocation environment variables for temporary use.

Risk: Broad image-generation trigger phrases may invoke this third-party skill unintentionally.

Mitigation: Use vendor-specific phrasing such as dLazy Nano Banana Pro when requesting the skill.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-banana-pro)
- [dLazy Homepage](https://dlazy.com)
- [dLazy CLI Source Link](https://github.com/dlazyai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with CLI commands and JSON result payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated image results are returned as hosted image URLs; asynchronous requests may return a generateId for later status polling.]

## Skill Version(s):

1.2.11 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
