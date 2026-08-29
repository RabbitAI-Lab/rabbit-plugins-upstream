## Description:

Creates 15-25 second vertical short videos for TikTok, YouTube Shorts, Instagram Reels, Douyin, and similar social platforms using a hook-first storyboard, first-frame and image-to-video generation, TTS voiceover, Remotion assembly, and burned-in subtitles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and social-content teams use this skill to invoke the dLazy short-video workflow from an agent session and produce finished vertical MP4 videos rather than only scripts or storyboards.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached files are sent to dLazy's hosted service for processing.

Mitigation: Use the skill only with content approved for dLazy processing and avoid attaching sensitive files unless that transfer is acceptable.

Risk: The workflow stores or uses a dLazy organization API key locally.

Mitigation: Prefer per-invocation credentials or npx when appropriate, protect the local CLI config, and rotate or revoke the API key from the dLazy dashboard if needed.

Risk: A persistent global CLI install may remain on the system after use.

Mitigation: Use the documented npx invocation when a non-persistent CLI run is preferred.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-short-video)
- [dLazy CLI homepage](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with bash command examples; the hosted workflow can return project updates and a finished MP4 video file.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx, a dLazy API key, and access to dLazy hosted API and file endpoints.]

## Skill Version(s):

1.2.10 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
