## Description:

Guides an agent to generate short text-to-video or image-to-video clips with Google Veo 3.1 Fast through dLazy's service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to prompt short video generation from text or images, or extend an existing video, using a dLazy account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied media may be uploaded to dLazy's cloud service.

Mitigation: Avoid submitting confidential prompts or media unless the service's terms and handling meet your requirements.

Risk: Video generation may consume account credits.

Mitigation: Check the cost estimate with the CLI's dry-run option before generating.

Risk: The CLI can store an API key locally and a global install persists the package.

Mitigation: Protect the key and consider the pinned on-demand npm invocation instead of a global install.

## Reference(s):

- [dLazy CLI source (linked in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON results]

**Output Format:** [Markdown with shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media is accessed via returned URLs or optional local download; asynchronous jobs can return a task ID.]

## Skill Version(s):

1.3.29 (source: ClawHub release metadata; skill frontmatter says 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
