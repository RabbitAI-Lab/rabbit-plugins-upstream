## Description:

Converts a submitted website URL into a promotional, social ad, or product demo video by using the dLazy website-to-video template to capture the site, derive brand elements, storyboard, add voiceover, build, and validate a Remotion-based video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, marketers, and agent operators use this skill when a user provides a website URL and wants a promo, social ad, or product demo generated through the dLazy CLI and hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, options, and attached files are sent to the dLazy hosted service.

Mitigation: Avoid sending sensitive prompts or files, review dLazy service terms before use, and attach only files intended for upload.

Risk: The skill depends on a third-party npm-distributed CLI and hosted API.

Mitigation: Prefer the pinned npx on-demand path when a persistent global CLI is not needed, and review the linked source and npm package before installation.

Risk: A dLazy API key may be saved in local CLI configuration.

Mitigation: Protect the local config file, use DLAZY_API_KEY for per-invocation credentials when appropriate, and rotate or revoke keys from the dLazy dashboard if exposed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-website-to-video)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with dlazy CLI commands and streamed service responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; attached local files may be uploaded to dLazy media storage when the --files option is used.]

## Skill Version(s):

1.3.13 (source: evidence.release.version; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
