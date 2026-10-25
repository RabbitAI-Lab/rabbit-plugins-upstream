## Description:

Turns articles, text, and news into narrated explainer videos through dLazy's file-to-video workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can turn an article or other written material into a narrated explainer video, then continue refining the work in a project-based, multi-turn session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Documents attached to a task are uploaded to dLazy storage, and project sessions are saved for continued work.

Mitigation: Only send documents you are comfortable sharing with dLazy; review its data-handling terms and select the intended project before continuing.

Risk: Login saves an organization API key in the local CLI configuration.

Mitigation: Keep the saved key private; use the documented environment-variable authentication option when preferred.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-article-to-video)
- [dLazy CLI project page](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Video, Text, Shell commands]

**Output Format:** [Narrated explainer video, with conversational text and CLI commands for project interaction]

**Output Parameters:** [Project-scoped, multi-turn]

**Other Properties Related to Output:** [Optional local files are uploaded to dLazy storage; generated work is handled by the dLazy cloud service.]

## Skill Version(s):

1.0.36 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
