## Description:

Guides developers in configuring Neon AI Gateway and calling multiple LLMs through a branch-scoped Neon credential.

This skill is ready for commercial/non-commercial use.

## Publisher:

[andrelandgraf](https://clawhub.ai/user/andrelandgraf)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to configure Neon AI Gateway, send branch-scoped LLM requests, and integrate model calls into apps or agents using supported SDKs.

### Deployment Geography for Use:

Global use; gateway availability is limited to aws-us-east-2, aws-us-east-1, aws-eu-central-1, and aws-ap-southeast-1 regions as documented in the skill.

## Known Risks and Mitigations:

Risk: Installing the parent Neon skill adds another skill to the environment.

Mitigation: Review and approve the parent skill before installing it.

Risk: Neon deploy or config commands can change project or branch configuration.

Mitigation: Review the target branch and proposed changes before running deployment or configuration commands.

Risk: Pulling gateway credentials can write NEON_AI_GATEWAY_TOKEN into local environment files.

Mitigation: Confirm the destination and protect local credential files before pulling credentials.

## Reference(s):

- [Neon AI Gateway overview](https://neon.com/docs/ai-gateway/overview.md)
- [Neon AI Gateway getting started](https://neon.com/docs/ai-gateway/get-started.md)
- [Neon AI Gateway authentication](https://neon.com/docs/ai-gateway/authentication.md)
- [Neon AI Gateway models](https://neon.com/docs/ai-gateway/models.md)
- [Neon model catalog](https://models.dev/providers/neon)
- [Parent Neon skill](https://neon.com/docs/ai/skills/neon/SKILL.md)
- [ClawHub skill release](https://clawhub.ai/andrelandgraf/skills/neon-ai-gateway)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with code examples and commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May provide a working inference request or agent configuration.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
