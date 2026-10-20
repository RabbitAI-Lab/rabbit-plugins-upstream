## Description:

Helps turn blog posts and other documents into narrated videos with storyboards and voiceovers through dLazy's video-generation service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and teams use this skill to turn blog posts, articles, and documents into narrated videos for social media, explainers, and training.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The blog-to-video title understates the broader document and file-to-video functionality.

Mitigation: Review the requested task and attached content before enabling the service for sensitive workflows.

Risk: Prompts and attached files may be sent to dLazy, and an API key may be stored locally.

Mitigation: Upload only authorized content, protect the local API key, and verify the pinned CLI package before installation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-blog-to-video)
- [dLazy CLI (link supplied in skill metadata; release import provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Text and Markdown with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video-generation work is handled by the dLazy service; the agent can return project updates and generated video links.]

## Skill Version(s):

1.0.31 (source: ClawHub release metadata; bundled skill frontmatter says 1.0.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
