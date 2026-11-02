## Description:

blog to video, blog post to video, article to video — convert a blog post into a narrated video with storyboard, voiceover, and build. Use when the user gives a blog post (text or link) and wants a video version for social or YouTube.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content creators use this skill to turn a blog post supplied as text or a link into a narrated video with a storyboard and voiceover for social media or YouTube. It supports starting a new project or continuing a project-scoped video task.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached files are sent to dLazy's hosted service, and attached files are uploaded to its media storage.

Mitigation: Submit only material you are permitted to upload, select the intended organization and project, and review service retention policies.

Risk: Video generation may consume organization credits and incur costs.

Mitigation: Consider generation costs and check the intended organization's available credits before starting a task.

Risk: The CLI can save an organization API key in the local user configuration.

Mitigation: Protect the local configuration, or use the documented per-invocation environment variable; rotate or revoke keys when needed.

## Reference(s):

- [CLI project homepage](https://github.com/dlazy-ai/cli)
- [npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Files, Text, Guidance]

**Output Format:** [Narrated video files with storyboard and voiceover, plus streamed text responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project-scoped sessions; attached local files may be uploaded for use as references]

## Skill Version(s):

1.0.35 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
