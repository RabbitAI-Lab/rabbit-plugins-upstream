## Description:

Turns a website URL into a promotional, social ad, or product demo video by capturing the site, deriving brand and storyboard inputs, adding voiceover, and building on a Remotion template.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content teams use this skill when a user provides a URL and wants an agent to create a promotional video, social ad, or product demo through the dLazy website-to-video template.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the skill sends prompts and options to the dLazy API, and attached local files are uploaded to dLazy media storage.

Mitigation: Only submit URLs and files appropriate for dLazy processing, and review dLazy service terms before use.

Risk: The skill depends on a pinned third-party CLI and a dLazy API key.

Mitigation: Review the dLazy CLI source before installing, prefer npx when a persistent global binary is not desired, and use a least-privilege API key that can be rotated or revoked.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-website-to-video)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and streamed CLI text output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference project outputs from the dLazy service; attached local files are uploaded to dLazy media storage.]

## Skill Version(s):

1.3.16 (source: server release metadata; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
