## Description:

Turns written articles, text, or news into narrated explainer videos with outline, storyboard, voiceover, build, and validation steps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to start or continue dLazy projects that turn articles, text, news, or documents into narrated explainer, courseware, report, or training videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API keys may be stored in the local dLazy CLI configuration file.

Mitigation: Prefer per-invocation DLAZY_API_KEY for sensitive environments and check permissions on ~/.dlazy/config.json when using dlazy login.

Risk: Attached files are uploaded to dLazy's cloud media storage before being used by the hosted agent.

Mitigation: Attach only files that are appropriate to send to dLazy's cloud service, especially when working with confidential documents.

Risk: The pinned CLI package is installed or run from npm and calls external dLazy API endpoints.

Mitigation: Review the pinned @dlazy/cli package and source before installing, and account for network access to api.dlazy.com and files.dlazy.com.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-article-to-video)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Configuration]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the dLazy CLI to stream hosted agent responses and may upload attached local files to dLazy media storage.]

## Skill Version(s):

1.0.14 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
