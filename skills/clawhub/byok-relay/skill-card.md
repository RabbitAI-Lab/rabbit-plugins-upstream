## Description: <br>
BYOK Relay Builder helps agents add an OpenAI-compatible relay to client-side apps so users can connect their own provider API keys across OpenAI, Anthropic, Gemini, Groq, Mistral, OpenRouter, and compatible models. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[avikalpg](https://clawhub.ai/user/avikalpg) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to add BYOK LLM access to browser, mobile, extension, Electron, and other client-side apps. It guides relay configuration, API-key collection UI, provider calls, self-hosting commands, and smoke tests. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Apps built from this skill may send and store provider API keys with a third-party relay without clear user disclosure or consent. <br>
Mitigation: Clearly disclose the relay domain before key entry, explain that the provider key is sent to and stored by the relay service, require user consent, and provide a key removal path. <br>
Risk: Sensitive or production workloads may depend on a managed relay outside the app owner's direct control. <br>
Mitigation: Prefer self-hosting for production or sensitive use, and use restricted provider keys with the minimum required permissions and spend limits. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/avikalpg/skills/byok-relay) <br>
- [Managed relay endpoint](https://relay.byokrelay.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline code examples, shell commands, and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include frontend UI snippets, relay API calls, optional self-hosting steps, and smoke-test instructions.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata and artifact/VERSION) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
