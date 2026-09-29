## Description:

Turns articles and documents into narrated explainer videos using dLazy's hosted video-generation workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and teams use this skill to turn written articles or documents into narrated explainer videos with outlines, storyboards, voiceover, and validation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected attachments may be sent to dLazy's hosted service.

Mitigation: Only attach files you are comfortable uploading to dLazy.

Risk: Signing in stores a dLazy API key locally, and a global CLI install persists on the machine.

Mitigation: Protect or revoke the API key as needed, and use the pinned npx option to avoid a persistent global CLI installation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-article-to-video)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Text and Markdown responses from a hosted video-generation project]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video work is managed in a dLazy-hosted project; attached files are uploaded to dLazy.]

## Skill Version(s):

1.0.25 (source: server release metadata; skill frontmatter says 1.0.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
