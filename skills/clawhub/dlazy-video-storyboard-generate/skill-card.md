## Description:

Converts storyboard details into a video-generation pipeline that an agent can add to a canvas.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to turn storyboard context, dialogue, and video prompts into a structured video generation pipeline for canvas-based workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send prompts, selected media paths or files, and generation data to dLazy services through the hosted CLI workflow.

Mitigation: Use it only for workflows where that data sharing is acceptable, avoid sensitive media, and verify the configured dLazy account and API key before use.

Risk: The artifact includes global third-party CLI installation and terminal-generation instructions that may not match ordinary storyboard canvas use.

Mitigation: Prefer npx or an isolated environment, verify the @dlazy/cli package and version, and remove or clarify unrelated terminal-generation instructions before deployment.

Risk: API keys may be stored in the user's dLazy CLI configuration or supplied through an environment variable.

Mitigation: Protect the local CLI configuration, use least-privilege credentials where available, and rotate or revoke keys from the dLazy dashboard when access changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-video-storyboard-generate)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON pipeline snippets and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses storyboard aspect ratio, resolution, dialogue text, and video prompts to define audio, image, and video canvas elements.]

## Skill Version(s):

1.2.11 (source: server release metadata; artifact frontmatter lists 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
