## Description:

Converts a provided website URL into a promotional, social ad, or product demo video by capturing the site, deriving brand assets, storyboarding, adding voiceover, building, and validating a Remotion-based output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, marketers, and content teams use this skill to turn a website or landing-page URL into a promotional video, social ad, or product demo through the dLazy website-to-video template.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and any files passed to the CLI are sent to dLazy-hosted services.

Mitigation: Do not upload secrets, credentials, regulated data, or private documents unless you intend to share them with that service.

Risk: The skill depends on the third-party dLazy CLI and npm package.

Mitigation: Review the dLazy CLI source and npm package before installing; prefer npx or an isolated install over a global install.

Risk: Use requires a dLazy API key stored locally or supplied through the environment.

Mitigation: Use scoped keys, keep local configuration protected, and rotate or revoke keys when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-website-to-video)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx and a dLazy API key; prompts and attached files are sent to dLazy-hosted services.]

## Skill Version(s):

1.3.14 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
