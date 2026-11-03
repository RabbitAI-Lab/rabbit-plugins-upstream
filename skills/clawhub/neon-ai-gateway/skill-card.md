## Description:

Helps developers configure Neon AI Gateway to call hosted language and embedding models from apps and agents using familiar SDKs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[andrelandgraf](https://clawhub.ai/user/andrelandgraf)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to enable Neon AI Gateway on a branch, connect model SDKs and agent frameworks, route requests across available models, and generate embeddings.

### Deployment Geography for Use:

AWS regions aws-us-east-2, aws-us-east-1, aws-eu-central-1, and aws-ap-southeast-1

## Known Risks and Mitigations:

Risk: The example todo tool reads every row, which could expose other users’ tasks to the AI service.

Mitigation: Enforce authenticated user and tenant boundaries, filter for open tasks, and limit returned fields and rows.

Risk: Prompts, tool results, and embedding inputs are sent to hosted inference.

Mitigation: Send only content approved for the hosted AI service.

Risk: Gateway setup can write credentials to local environment files and change branch configuration or spend.

Mitigation: Protect generated environment files and review branch changes and expected costs before deployment.

## Reference(s):

- [Neon AI Gateway overview](https://neon.com/docs/ai-gateway/overview)
- [Neon AI Gateway models](https://neon.com/docs/ai-gateway/models)
- [Neon AI Gateway embeddings guide](https://neon.com/docs/ai-gateway/embeddings)
- [Neon AI Gateway troubleshooting](https://neon.com/docs/ai-gateway/troubleshooting)
- [Neon models catalog](https://models.dev/providers/neon)
- [Neon parent skill](https://neon.com/docs/ai/skills/neon/SKILL.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions, API calls]

**Output Format:** [Markdown with TypeScript, JavaScript, shell, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Model availability and gateway requirements depend on the Neon region, plan, and current model catalog.]

## Skill Version(s):

1.0.5 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
