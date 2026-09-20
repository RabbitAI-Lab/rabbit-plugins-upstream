## Description:

Guides an agent to generate short-video spoken scripts with high contrast, emotional resonance, story structure, and personal IP attributes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and content teams use this skill to draft short-video spoken scripts for character stories, personal IP viewpoints, and topic-driven social video narration. It structures output around a seven-step hook, story, viewpoint, and punchline pattern.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill advertises spoken-script writing but also includes dLazy image-generation CLI installation and execution guidance.

Mitigation: Install and invoke it only when the dLazy workflow is intended; for pure spoken-script generation, revise or split the skill before deployment.

Risk: Prompts, parameters, and referenced media files may be sent to dLazy services and media storage.

Mitigation: Review prompts and local file inputs before use, avoid sensitive content, and confirm users understand the SaaS data flow.

Risk: The dLazy API key can be stored in local CLI configuration.

Mitigation: Protect the local config file, prefer environment-scoped credentials where appropriate, and rotate or revoke API keys when access changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-text-spoken-script)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Plain text or Markdown script content, with optional inline shell commands for dLazy CLI workflows.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a seven-step spoken-script structure; artifact behavior may also guide dLazy CLI image-generation execution.]

## Skill Version(s):

1.3.19 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
