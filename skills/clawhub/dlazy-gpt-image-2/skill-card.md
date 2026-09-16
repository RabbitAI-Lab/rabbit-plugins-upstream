## Description:

GPT Image 2 generates images from text prompts and edits or synthesizes images from reference inputs through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to generate images from prompts or edit and synthesize images from provided references using dLazy's hosted image-generation service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, reference images, and generated media are processed through dLazy cloud endpoints.

Mitigation: Use the skill only when uploading that content to dLazy is acceptable, and avoid sensitive prompts or images unless authorized.

Risk: The skill depends on trusting dLazy's npm CLI and local API-key configuration.

Mitigation: Prefer the pinned npx invocation for nonpersistent use, review the published CLI source or package as needed, and rotate or revoke dLazy API keys according to organization policy.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-gpt-image-2)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Files]

**Output Format:** [CLI command guidance and JSON responses containing generated image URLs, with optional saved image files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key and uploads prompts and reference media to dLazy cloud endpoints.]

## Skill Version(s):

1.3.16 (source: server release evidence; artifact frontmatter shows 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
