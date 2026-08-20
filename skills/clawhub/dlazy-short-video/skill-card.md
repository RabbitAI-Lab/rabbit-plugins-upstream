## Description:

Creates finished 15-25 second vertical short videos for TikTok, YouTube Shorts, Instagram Reels, Douyin, and similar social platforms through dLazy's hosted short-video workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, creators, and developers use this skill to ask a dLazy hosted agent to generate social-media-ready vertical short videos rather than scripts. It is suited to social shorts; for conversion-focused product ads, use a product-ad workflow instead.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached files may be sent to dLazy's hosted service.

Mitigation: Use the skill only for content that is acceptable to process through dLazy, and avoid attaching sensitive files unless the user accepts that service flow.

Risk: A dLazy API key may be stored locally under ~/.dlazy/config.json.

Mitigation: Use the DLAZY_API_KEY environment variable for per-run credentials when persistent local storage is not desired, and rotate or revoke keys from the dLazy dashboard as needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-short-video)
- [dLazy CLI homepage](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Files]

**Output Format:** [Markdown with inline bash code blocks and generated MP4 media through the dLazy workflow]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; attached local files may be uploaded to dLazy storage.]

## Skill Version(s):

1.2.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
