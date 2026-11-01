## Description:

Turns user-provided documents into explainer, report, or training videos through the dLazy file-to-video workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

People who need an explainer, report, or training video can use the skill to turn a document into a storyboarded video through dLazy. They can start a new project or continue an existing one with follow-up instructions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Attached documents and prompts are sent to dLazy’s hosted service, and attached files are uploaded to its media storage.

Mitigation: Only attach documents you are permitted to share with dLazy, and review the service’s retention terms before uploading.

Risk: The organization API key is saved in the local CLI configuration and could be exposed if that configuration is accessed by others.

Mitigation: Protect the saved key and rotate or revoke it from the organization dashboard if it may have been exposed.

Risk: A request could be continued in an unintended project and use the wrong project context.

Mitigation: Check the project ID with `dlazy projects list` and select the intended project before continuing.

## Reference(s):

- [CLI repository listed in skill metadata](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)
- [dLazy organization API key settings](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Video, Text, Markdown, Guidance]

**Output Format:** [Generated video with terminal text or Markdown responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project-based, multi-turn workflow; attached files are uploaded to dLazy media storage.]

## Skill Version(s):

1.0.33 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
