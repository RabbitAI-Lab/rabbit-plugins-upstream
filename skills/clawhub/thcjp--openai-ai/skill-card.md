## Description:

llm-provider AI工具 helps agents call OpenAI-compatible provider tools to manage model calls, files, assistants, vector stores, batch jobs, fine-tuning jobs, images, and model resources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, automation teams, and agent users use this skill to automate OpenAI-compatible provider workflows such as chat completions, assistant and vector-store setup, file handling, batch jobs, fine-tuning jobs, image generation, and model-resource checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can initiate broad provider actions, including uploads, assistant or vector-store changes, batch jobs, fine-tuning jobs, deletes, and other account-changing operations.

Mitigation: Require preview and explicit user confirmation before uploads, assistant or vector-store changes, batch jobs, fine-tuning jobs, deletes, or other write actions.

Risk: Prompts and files may be processed by the provider and may be subject to provider-side handling or retention.

Mitigation: Do not provide sensitive prompts or files unless the user is comfortable with provider-side processing.

Risk: The security verdict is suspicious because the skill combines broad command and file authority with provider account automation.

Mitigation: Review the skill before installing and use it only when the user explicitly wants ClawLink to call the provider on their behalf.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/openai-ai)
- [llm-provider connection dashboard](https://claw-link.dev/dashboard?add=llm-provider)
- [Skill homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with bash command examples and JSON result patterns]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a configured provider connection and API credentials; write actions should be previewed and explicitly confirmed.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
