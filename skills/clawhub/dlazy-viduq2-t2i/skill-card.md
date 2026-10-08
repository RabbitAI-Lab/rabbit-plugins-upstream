## Description:

Guides agents to generate Vidu Q2 images from prompts or reference images through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to instruct an agent to generate images from text prompts or reference images with Vidu Q2 through dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media files are sent to dLazy's hosted service.

Mitigation: Share only prompts and files you are comfortable sending to dLazy.

Risk: Authentication may save an API key in the local CLI configuration.

Mitigation: Use per-invocation credentials if you do not want a locally saved key.

Risk: Image generation can consume API credits.

Mitigation: Check estimated cost before calling the API and monitor credit usage.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-viduq2-t2i)
- [dLazy CLI source (listed in skill metadata; not verified skill provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images are returned as hosted URLs; optional local download or asynchronous task ID.]

## Skill Version(s):

1.3.26 (source: server-resolved ClawHub release; skill frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
