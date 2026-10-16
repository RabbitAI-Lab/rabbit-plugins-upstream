## Description:

Helps turn a static character image into an action video using Jimeng Dream Actor through dLazy's cloud service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use the skill to generate action videos from character images and text prompts through the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authentication requires a dLazy API key that may be stored on the local device.

Mitigation: Use an approved key, protect local credentials, and rotate or revoke the key if exposed.

Risk: Images or videos supplied as local files are uploaded to dLazy's cloud service.

Mitigation: Submit only media approved for external processing.

Risk: Running the skill installs or executes a third-party npm CLI.

Mitigation: Review the referenced CLI before use and prefer the pinned on-demand command if a persistent global install is unnecessary.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-dream-actor)
- [dLazy CLI source linked in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and result guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The service returns generated media links or an asynchronous task ID.]

## Skill Version(s):

1.3.30 (source: ClawHub release metadata; artifact frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
