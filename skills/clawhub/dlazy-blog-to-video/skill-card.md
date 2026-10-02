## Description:

Helps turn blog posts and other documents into narrated videos using dLazy's file-to-video service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and teams use this skill to request narrated videos from blog posts or other documents, with storyboards and voiceovers generated through dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Despite its blog-to-video name, the workflow handles general files and documents, which may be uploaded to dLazy.

Mitigation: Use it only when broader document-to-video processing is intended; review attachments and avoid sensitive files unless you trust the service.

Risk: Prompts and attached files are sent to dLazy, and login can save an API key locally.

Mitigation: Use non-sensitive prompts and files; consider per-invocation API keys and on-demand CLI use if you prefer not to keep a saved key or global installation.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-blog-to-video)
- [dLazy CLI repository (listed in skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Streaming conversational text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video generation runs through the dLazy service.]

## Skill Version(s):

1.0.23 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
