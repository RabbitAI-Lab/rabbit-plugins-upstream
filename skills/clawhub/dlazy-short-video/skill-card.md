## Description:

Creates finished 15-25 second vertical short videos for TikTok, YouTube Shorts, Reels, Douyin, and similar social platforms using storyboarded shots, generated clips, voiceover, and burned-in subtitles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and agents use this skill to request a complete 9:16 social short video from a prompt. It is suited to social shorts where the desired deliverable is a rendered vertical MP4 rather than only a script or storyboard.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on dLazy's hosted service and sends prompts, options, and attached files to dLazy endpoints.

Mitigation: Use only with data intended for dLazy processing, review service terms, and avoid attaching confidential files unless upload is intended.

Risk: Authentication uses a dLazy API key stored locally or supplied through an environment variable.

Mitigation: Protect the local config and environment, and rotate or revoke the API key if the CLI or machine is no longer trusted.

Risk: The CLI is installed or executed through npm/npx, which introduces package execution risk.

Mitigation: Prefer npx or a local install when possible and review the pinned package or source before running it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-short-video)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown and CLI-oriented text guidance for invoking dLazy short-video projects]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides use of a hosted dLazy service that returns agent responses and can produce a finished 15-25 second vertical MP4.]

## Skill Version(s):

1.2.16 (source: release evidence; artifact frontmatter lists 1.2.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
