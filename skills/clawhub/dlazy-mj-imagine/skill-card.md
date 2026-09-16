## Description:

Midjourney style generation, supports aspect ratio, Bot type, and output position (grid/U1-U4), for artistic and strongly stylized creative image generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to run the dLazy Midjourney-style image-generation CLI with prompt, aspect ratio, bot type, and output selection options.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The @dlazy/cli package runs with the user's local privileges.

Mitigation: Review or otherwise trust @dlazy/cli@1.2.3 before installation, and prefer npx for on-demand use when a persistent global binary is not needed.

Risk: The skill requires a dLazy API key stored in local configuration or supplied by environment variable.

Mitigation: Keep the API key scoped to the organization, rotate or revoke it when needed, and avoid exposing it in prompts, logs, or shared shell history.

Risk: Prompts and local media paths supplied to the CLI are sent to dLazy hosted services for generation.

Mitigation: Only submit prompts and media files that are appropriate to upload to dLazy's hosted API and media storage.

## Reference(s):

- [dLazy homepage](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-mj-imagine)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Files, Guidance]

**Output Format:** [JSON result with hosted image URLs; optional local image file when --save is used]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return an asynchronous generateId when --no-wait is used.]

## Skill Version(s):

1.3.15 (source: server release evidence; artifact frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
