## Description:

Turns written articles, text, news, essays, or documents into narrated explainer videos with outline, storyboard, voiceover, build, and validation support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke the dLazy CLI for turning article, text, news, essay, or document inputs into narrated explainer, report, courseware, or training videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, options, and attached files are sent to a third-party SaaS service.

Mitigation: Use the skill only for content intended for dLazy processing, and avoid attaching sensitive files unless they are approved for that service.

Risk: The dLazy CLI may save an API key in local user configuration.

Mitigation: Use organization-scoped keys, rotate or revoke keys from the dLazy dashboard when needed, and prefer per-invocation environment variables where local persistence is not desired.

Risk: The workflow installs or runs a pinned third-party npm CLI.

Mitigation: Review the pinned CLI source or npm package before installation and use the npx path when a persistent global install is unnecessary.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-article-to-video)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides an agent to authenticate with dLazy, start or continue dLazy projects, and attach files for hosted video-generation workflows.]

## Skill Version(s):

1.0.21 (source: evidence release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
