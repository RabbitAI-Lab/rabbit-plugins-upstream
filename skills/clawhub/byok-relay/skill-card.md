## Description:

OpenAI-compatible LLM gateway for any client-side application (browser, mobile, React Native, Flutter, VS Code extensions, browser extensions, Electron, smart TV, and more). Routes requests to OpenAI, Anthropic, Gemini, Groq, Mistral, and 200+ models, handling CORS, key encryption, and streaming without a dedicated backend. Uniquely supports BYOK (bring your own key): users connect their own provider API keys so the developer pays nothing for inference. Use for multi-provider LLM access, client-safe AI API calls, or any product where users supply their own API credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[avikalpg](https://clawhub.ai/user/avikalpg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and product teams use this skill to add multi-provider LLM access to client-side apps without building a dedicated backend. It focuses on BYOK flows where users or organizations connect their own provider API keys, plus optional self-hosting for teams that need more control.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The managed relay receives users' paid provider API keys.

Mitigation: Use the managed relay only with clear user consent; for sensitive, organizational, or high-volume deployments, self-host so the operator controls the relay and encryption secret.

Risk: Provider API keys can incur user or organization costs if misused.

Mitigation: Use dedicated restricted provider keys, spending limits, visible billing ownership copy, and clear deletion and revocation guidance.

Risk: A privileged relay token stored in browser localStorage can expose access to keys saved under that token.

Mitigation: For real users or organizations, prefer a backend-managed session or HttpOnly cookie, avoid sharing relay tokens across team members, and revoke compromised relay tokens.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/avikalpg/skills/byok-relay)
- [Publisher profile](https://clawhub.ai/user/avikalpg)
- [Managed relay endpoint](https://relay.byokrelay.com)
- [BYOK Relay GitHub project](https://github.com/avikalpg/byok-relay)
- [OpenAI API keys](https://platform.openai.com/api-keys)
- [Anthropic API keys](https://console.anthropic.com/settings/keys)
- [Google AI Studio API keys](https://aistudio.google.com/app/apikey)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with JavaScript, HTML, shell command, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes client integration patterns, provider key UI guidance, self-hosting commands, response-state handling, and smoke-test steps.]

## Skill Version(s):

1.0.6 (source: server release evidence and artifact/VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
