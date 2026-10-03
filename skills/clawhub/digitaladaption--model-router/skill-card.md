## Description:

A comprehensive AI model routing system that automatically selects the optimal model for any task. Set up multiple AI providers (Anthropic, OpenAI, Gemini, Moonshot, Z.ai, GLM) with secure API key storage, then route tasks to the best model based on task type, complexity, and cost optimization. Includes interactive setup wizard, task classification, and cost-effective delegation patterns. Use when you need "use X model for this", "switch model", "optimal model", "which model should I use", or to balance quality vs cost across multiple AI providers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[digitaladaption](https://clawhub.ai/user/digitaladaption)

### License/Terms of Use:


## Use Case:

Developers and agent users use this skill to classify tasks, configure provider credentials and model mappings, and choose cost-appropriate models for delegated sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Provider API keys are stored locally under ~/.model-router.

Mitigation: Install only if local credential storage is acceptable, keep the files restricted to the owner account, and rotate provider keys if local access may have been exposed.

Risk: The skill may route sensitive tasks or data to third-party model providers.

Mitigation: Use only approved providers for confidential, customer, regulated, or business-critical data, and avoid sending such data through suggested models until provider approval is confirmed.

Risk: Generated sessions_spawn commands and model aliases may not map to the intended provider or canonical model.

Mitigation: Manually review each generated command and reconcile aliases to approved provider and model IDs before execution.

## Reference(s):

- [Model Router Usage Examples](references/USAGE_EXAMPLES.md)
- [Model Specifications Reference](references/model-specs.md)
- [Anthropic Documentation](https://docs.anthropic.com)
- [OpenAI Platform Documentation](https://platform.openai.com/docs)
- [Gemini API Documentation](https://ai.google.dev/docs)
- [Moonshot Platform Documentation](https://platform.moonshot.cn/docs)
- [Z.ai API Documentation](https://api.z.ai/docs)
- [GLM API Documentation](https://open.bigmodel.cn/dev/api)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown and terminal text with optional JSON classifier output and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May recommend sessions_spawn commands, model aliases, confidence scores, cost levels, and local configuration changes.]

## Skill Version(s):

1.1.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
