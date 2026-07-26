## Description: <br>
A comprehensive AI model routing system that automatically selects the optimal model for any task. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[digitaladaption](https://clawhub.ai/user/digitaladaption) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use this skill to choose and configure model routing across multiple AI providers based on task type, complexity, quality needs, and cost preference. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores AI provider API keys locally. <br>
Mitigation: Use only approved provider keys, keep the generated files restricted to the local user, prefer environment variables for production use, and rotate keys regularly. <br>
Risk: Routed tasks may send private, regulated, or business-sensitive data to third-party model providers. <br>
Mitigation: Confirm organizational approval for each configured provider, redact sensitive inputs before routing, and verify which provider and model each alias uses before delegation. <br>
Risk: Automatic or heuristic model selection can choose an unsuitable model for quality, privacy, or cost needs. <br>
Mitigation: Review classifier recommendations, honor explicit user model requests, and adjust task mappings or cost optimization settings for high-impact work. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/digitaladaption/skills/model-router) <br>
- [Usage examples](references/USAGE_EXAMPLES.md) <br>
- [Model specifications reference](references/model-specs.md) <br>
- [Anthropic documentation](https://docs.anthropic.com) <br>
- [OpenAI platform documentation](https://platform.openai.com/docs) <br>
- [Gemini documentation](https://ai.google.dev/docs) <br>
- [Moonshot documentation](https://platform.moonshot.cn/docs) <br>
- [Z.ai documentation](https://api.z.ai/docs) <br>
- [GLM API documentation](https://open.bigmodel.cn/dev/api) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance, terminal text, optional JSON classifier output, and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create local model-router configuration and API key files when the setup wizard is run.] <br>

## Skill Version(s): <br>
1.1.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
