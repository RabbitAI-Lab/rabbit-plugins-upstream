## Description:

Turn articles and documents into narrated explainer videos through dLazy's hosted workflow, including outlining, storyboarding, voiceover, building, and validation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

People who want to turn an article or document into a narrated explainer, report, course, or training video can use this skill to guide the hosted dLazy workflow and continue work in a project.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Messages, options, and attached files are sent to dLazy's hosted service; attachments are uploaded to its media storage.

Mitigation: Use only articles and attachments you are comfortable sending to dLazy.

Risk: Login saves an API key in the local CLI configuration.

Mitigation: Keep the local configuration protected, use the documented environment-variable option when appropriate, and rotate or revoke keys from the dashboard if needed.

Risk: Video generation may consume service credits and uses an organization and project context.

Mitigation: Select the intended organization and project and consider service-credit costs before running a task.

## Reference(s):

- [dLazy homepage](https://dlazy.com)
- [CLI repository link listed in skill metadata](https://github.com/dlazy-ai/cli)
- [@dlazy/cli package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Video, Guidance, Shell commands, Configuration instructions]

**Output Format:** [Narrated video produced through dLazy, with Markdown guidance and inline shell commands for operating the workflow]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project-based, multi-turn workflow; optional article or document attachments]

## Skill Version(s):

1.0.38 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
