## Description: <br>
OpenBotAuth helps AI agents create a cryptographic identity, register a public JWKS endpoint, and sign HTTP requests with Ed25519/RFC 9421 headers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hammadtq](https://clawhub.ai/user/hammadtq) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and AI-agent operators use OpenBotAuth to register an agent identity, generate and store local Ed25519 keys, and produce signed request headers for CLI or browser-based sessions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores a local private key and briefly stores a registration bearer token. <br>
Mitigation: Use the token only for registration, keep files permission-restricted, delete the token after setup, and never attach bearer tokens to browser sessions or global headers. <br>
Risk: The optional browser mode runs a local HTTPS interception proxy with a persistent CA key. <br>
Mitigation: Prefer core signing mode when possible, avoid routing unrelated browsing through the proxy, and trust or install the generated CA only after reviewing the TLS interception implications. <br>
Risk: The security verdict is suspicious because browser-mode signing changes local network and certificate handling. <br>
Mitigation: Review the skill before deployment, keep proxy use scoped to intended browsing tasks, and confirm the registration token is removed after setup. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/hammadtq/skills/openbotauth) <br>
- [OpenBotAuth Website](https://openbotauth.org) <br>
- [OpenBotAuth API](https://api.openbotauth.org) <br>
- [OpenBotAuth Spec](https://github.com/OpenBotAuth/openbotauth) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, JavaScript snippets, and JSON configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands may create local key, token, configuration, and optional proxy CA files when executed by the agent.] <br>

## Skill Version(s): <br>
0.1.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
