## Description:

Adapts web novel material into Chinese webtoon drama structure, including genre setup, plot breakdown, episode tagging, per-episode script writing, and guided dLazy CLI image-generation steps when media generation is requested.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, writers, and developers use this skill to turn web novel chapters into structured Chinese webtoon adaptation plans and episode scripts. When image generation is requested, the skill guides dLazy CLI authentication and one-at-a-time generation commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires installing or running the third-party dLazy CLI and authenticating with a dLazy API key.

Mitigation: Review the CLI before use, prefer a sandbox or npx for limited runs, and rotate or revoke keys when access is no longer needed.

Risk: The dLazy CLI stores credentials locally when using login or auth setup.

Mitigation: Protect the local CLI configuration file, or pass DLAZY_API_KEY per invocation when a persistent local credential is not desired.

Risk: Prompts and selected image, video, or audio files may be uploaded to dLazy services for processing.

Mitigation: Avoid unpublished, private, or sensitive manuscripts and media unless the service terms and retention behavior are acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-webtoon-adapter)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown conversation output with structured Chinese adaptation sections and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm/npx and dLazy API authentication; prompts or selected media files may be sent to dLazy services.]

## Skill Version(s):

1.3.16 (source: server release metadata, released 2026-09-14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
