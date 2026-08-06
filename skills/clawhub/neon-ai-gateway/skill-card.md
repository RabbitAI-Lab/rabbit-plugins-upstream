## Description: <br>
One API and one credential for frontier and open-source LLMs, built into your Neon branch and powered by Databricks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[andrelandgraf](https://clawhub.ai/user/andrelandgraf) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to configure Neon AI Gateway, send LLM requests through a branch-scoped Neon endpoint, and adapt OpenAI, Anthropic, Gemini, Vercel AI SDK, or Mastra integrations with minimal code changes. <br>

### Deployment Geography for Use: <br>
United States (AWS us-east-2 for AI Gateway availability) <br>

## Known Risks and Mitigations: <br>
Risk: Suggested Neon CLI commands can provision AI Gateway infrastructure and write branch-scoped credentials to local environment files. <br>
Mitigation: Review commands before execution and do not commit local environment files containing NEON_AI_GATEWAY_TOKEN or related credentials. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/andrelandgraf/skills/neon-ai-gateway) <br>
- [Neon parent skill](https://neon.com/docs/ai/skills/neon/SKILL.md) <br>
- [Neon AI Gateway overview](https://neon.com/docs/ai-gateway/overview.md) <br>
- [Neon AI Gateway get started](https://neon.com/docs/ai-gateway/get-started.md) <br>
- [Neon AI Gateway models](https://neon.com/docs/ai-gateway/models.md) <br>
- [Neon AI Gateway chat completions](https://neon.com/docs/ai-gateway/chat-completions.md) <br>
- [Neon AI Gateway Anthropic messages](https://neon.com/docs/ai-gateway/anthropic-messages.md) <br>
- [Neon AI Gateway OpenAI responses](https://neon.com/docs/ai-gateway/openai-responses.md) <br>
- [Neon AI Gateway Gemini](https://neon.com/docs/ai-gateway/gemini.md) <br>
- [Neon AI Gateway authentication](https://neon.com/docs/ai-gateway/authentication.md) <br>
- [Neon AI Gateway troubleshooting](https://neon.com/docs/ai-gateway/troubleshooting.md) <br>
- [Neon provider model catalog](https://models.dev/providers/neon) <br>
- [models.dev API catalog](https://models.dev/api.json) <br>
- [Vercel AI SDK](https://ai-sdk.dev) <br>
- [Mastra](https://mastra.ai) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline code, code blocks, and shell command blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include Neon CLI commands and environment-variable configuration for branch-scoped AI Gateway credentials.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
