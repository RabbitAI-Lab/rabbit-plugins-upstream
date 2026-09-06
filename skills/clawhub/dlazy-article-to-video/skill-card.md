## Description:

Turns articles or documents into narrated explainer videos by guiding outline, storyboard, voiceover, build, and validation through the dLazy hosted service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill when a user provides an article, document, or reference file and wants an explainer, report broadcast, courseware, or training video produced through dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected files may be sent to dLazy hosted APIs and file storage.

Mitigation: Use the skill only with content suitable for the dLazy service, review uploaded files before invoking the CLI, and follow the service terms.

Risk: A dLazy API key may be stored in the local CLI configuration for future use.

Mitigation: Use per-invocation DLAZY_API_KEY or npx when lower persistence is preferred, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: The skill depends on npm or npx to run a third-party CLI and on access to dLazy API endpoints.

Mitigation: Install the pinned CLI version only in environments approved for third-party packages and verify network access to api.dlazy.com and files.dlazy.com.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-article-to-video)
- [Publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with CLI commands and service status or result text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference generated video project state returned by the dLazy hosted service.]

## Skill Version(s):

1.0.15 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
