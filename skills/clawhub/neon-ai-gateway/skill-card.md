## Description:

Helps developers configure the branch-scoped Neon AI Gateway and use it for model inference, embeddings, and AI agents through familiar SDKs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[andrelandgraf](https://clawhub.ai/user/andrelandgraf)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to enable Neon AI Gateway on a project branch and connect applications or agents to language and embedding models using Neon credentials.

### Deployment Geography for Use:

AWS aws-us-east-2, aws-us-east-1, aws-eu-central-1, and aws-ap-southeast-1

## Known Risks and Mitigations:

Risk: Enabling the gateway may require a paid Neon plan and use paid resources.

Mitigation: Check the project plan and expected charges; approve provisioning before running Neon CLI changes.

Risk: Gateway credentials may be written to local environment files.

Mitigation: Keep credential files private and out of version control; review credential-handling commands before running them.

Risk: The skill suggests installing a parent Neon skill.

Mitigation: Review the parent skill and explicitly approve its installation before proceeding.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/andrelandgraf/skills/neon-ai-gateway)
- [Neon AI Gateway overview](https://neon.com/docs/ai-gateway/overview.md)
- [Neon AI Gateway getting started](https://neon.com/docs/ai-gateway/get-started.md)
- [Neon AI Gateway models](https://neon.com/docs/ai-gateway/models.md)
- [Neon AI Gateway embeddings](https://neon.com/docs/ai-gateway/embeddings)
- [Neon AI Gateway authentication](https://neon.com/docs/ai-gateway/authentication.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration]

**Output Format:** [Markdown with TypeScript, Bash, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Branch-scoped gateway setup and model-selection guidance]

## Skill Version(s):

1.0.2 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
