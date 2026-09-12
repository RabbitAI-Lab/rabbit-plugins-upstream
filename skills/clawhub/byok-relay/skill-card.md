## Description:

BYOK Relay Builder helps developers integrate byok-relay, an OpenAI-compatible gateway for client-side applications that supports BYOK credentials, CORS-safe streaming, and routing to OpenAI, Anthropic, Gemini, Groq, Mistral, OpenRouter, and other models without a dedicated backend.

This skill is ready for commercial/non-commercial use.

## Publisher:

[avikalpg](https://clawhub.ai/user/avikalpg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to add OpenAI-compatible, client-side LLM access with bring-your-own-key workflows. It helps generate relay setup guidance, API key connection UI, streaming request code, self-hosting commands, and key lifecycle guidance for frontend, mobile, extension, and B2B applications.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Applications may send valuable provider API keys to a managed relay.

Mitigation: Use the managed relay only when that trust model is acceptable; for sensitive, regulated, or high-volume deployments, prefer self-hosting or a backend-controlled design.

Risk: Browser-readable relay tokens can expose access to keys stored under that token.

Mitigation: Scope relay tokens per user, app, tenant, and relay origin; avoid shared relay tokens in clients and route organization-managed key flows through a backend.

Risk: Incorrect relay origins or non-HTTPS key upload flows can increase credential exposure.

Mitigation: Validate the relay origin, require HTTPS outside localhost development, and pin reviewed releases before deployment.

Risk: Users may need to recover from compromised, revoked, or expired provider keys.

Mitigation: Document key rotation, provider-side revocation, relay token revocation, and account deletion flows in the product experience.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/avikalpg/skills/byok-relay)
- [Managed Relay Endpoint](https://relay.byokrelay.com)
- [OpenAI API Keys](https://platform.openai.com/api-keys)
- [Anthropic API Keys](https://console.anthropic.com/settings/keys)
- [Google AI Studio API Keys](https://aistudio.google.com/app/apikey)
- [Groq API Keys](https://console.groq.com/keys)
- [Mistral API Keys](https://console.mistral.ai/api-keys)
- [OpenRouter API Keys](https://openrouter.ai/settings/keys)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline JavaScript, HTML, and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes client-side integration patterns, key lifecycle UX states, self-hosting commands, and security guidance.]

## Skill Version(s):

1.0.7 (source: evidence.release.version and artifact/VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
