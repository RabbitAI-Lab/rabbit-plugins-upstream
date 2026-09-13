## Description:

BYOK Relay Builder helps developers integrate an OpenAI-compatible client-side LLM relay across multiple providers while supporting user-supplied API keys.

This skill is ready for commercial/non-commercial use.

## Publisher:

[avikalpg](https://clawhub.ai/user/avikalpg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to add LLM features to browser, mobile, extension, Electron, and similar client-side applications without building a dedicated provider proxy. It guides setup of managed or self-hosted relay access, user API key connection flows, streaming requests, key lifecycle handling, and integration verification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Managed relay use sends reusable provider API keys to a third-party relay.

Mitigation: Use the managed relay only when that storage model is acceptable; for production, regulated, high-spend, or team use, self-host or route requests through a backend-for-frontend.

Risk: Long-lived relay bearer tokens in browser storage can grant access to saved provider keys if exposed.

Mitigation: Scope tokens by relay, app, user, and tenant; avoid browser storage for administrative or organization-wide access, and revoke then re-register tokens after compromise.

Risk: Shared team relay tokens expose all saved keys to every holder.

Mitigation: Issue one relay token per member and proxy organization-managed requests server-side instead of distributing a shared relay token to clients.

Risk: A license conflict exists between server evidence and artifact text.

Mitigation: Confirm the authoritative license before public release and update the card context if MIT-0 is not the governing license.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/avikalpg/skills/byok-relay)
- [Publisher profile](https://clawhub.ai/user/avikalpg)
- [Managed BYOK relay endpoint](https://relay.byokrelay.com)
- [OpenAI API keys](https://platform.openai.com/api-keys)
- [Anthropic API keys](https://console.anthropic.com/settings/keys)
- [Google AI Studio API keys](https://aistudio.google.com/app/apikey)
- [Groq API keys](https://console.groq.com/keys)
- [Mistral API keys](https://console.mistral.ai/api-keys)
- [OpenRouter API keys](https://openrouter.ai/settings/keys)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JavaScript, HTML, and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes integration, key lifecycle, UX state, and verification guidance.]

## Skill Version(s):

1.0.8 (source: server release metadata and artifact/VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
