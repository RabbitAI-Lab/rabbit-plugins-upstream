## Description:

Connects an agent to dLazy's hosted sandbox for project-scoped, multi-turn conversations and skill execution.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other dLazy users can start or continue project-based conversations with a hosted sandbox agent, optionally selecting a skill or attaching files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and files explicitly attached with --files are sent to the hosted dLazy service.

Mitigation: Avoid sharing sensitive prompts or files unless their transfer to dLazy is acceptable.

Risk: Logging in saves a dLazy API key in local CLI configuration.

Mitigation: Protect the local configuration or use DLAZY_API_KEY per run instead of saving a key.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-chat)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Streamed conversational text; format varies with the selected skill and prompt]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses retain project conversation context across turns.]

## Skill Version(s):

1.2.34 (source: server-resolved release metadata; artifact frontmatter says 1.2.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
