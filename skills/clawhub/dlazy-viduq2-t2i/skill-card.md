## Description:

Generate high-quality images with Vidu Q2, supporting text-to-image and image-to-image requests through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to generate or edit images with Vidu Q2 through dLazy's hosted CLI/API, including optional reference images, aspect ratio, resolution, async generation, and save-to-file workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad image-generation triggers could route a generic image request through dLazy when that was not intended.

Mitigation: Use the skill only when dLazy routing is intended and review prompts plus referenced files before invocation.

Risk: Prompts and referenced local images may be sent to dLazy hosted endpoints for generation.

Mitigation: Avoid sending sensitive content unless approved for dLazy processing; use dry-run when checking payloads.

Risk: Saved dLazy API keys are stored in the local CLI configuration.

Mitigation: Prefer DLAZY_API_KEY for per-invocation credentials when persistence is undesirable, or verify permissions on ~/.dlazy/config.json and rotate keys as needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-viduq2-t2i)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [JSON response with image output URLs; optional downloaded image file when --save is used; async task metadata when --no-wait is used.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; prompts and referenced local images may be sent to dLazy hosted endpoints.]

## Skill Version(s):

1.3.12 (source: server release metadata; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
