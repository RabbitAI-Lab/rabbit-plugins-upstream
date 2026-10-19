## Description:

Helps agents generate digital-human presenter videos from a portrait image and audio or text using Jimeng OmniHuman 1.5.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request digital-human presenter videos from a portrait and audio or text through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected portrait, video, or audio files are sent to dLazy-hosted services.

Mitigation: Share only media you are authorized to upload, and review dLazy's terms before use.

Risk: The external CLI requires an API key and may save it in local configuration.

Mitigation: Review the CLI before installation; use the documented on-demand installation option if preferred, and rotate or revoke the key if needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-omnihuman-1-5)
- [dLazy CLI project (skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with CLI commands and generated media links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The service may return a media URL or an asynchronous task ID; a local download is optional.]

## Skill Version(s):

1.3.30 (source: ClawHub release; bundled frontmatter states 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
