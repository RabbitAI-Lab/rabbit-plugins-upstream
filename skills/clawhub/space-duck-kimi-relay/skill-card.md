## Description:

Optional add-on for Space Duck that runs a local Kimi device sign-in and relay so a Remote-Hosted (Lane A / BYOB) duck can use the owner's Kimi membership for inference.

This skill is ready for commercial/non-commercial use.

## Publisher:

[askegor](https://clawhub.ai/user/askegor)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to sign in to Kimi locally, refresh membership tokens, and expose an OpenAI-compatible local relay for Space Duck runtimes they operate on their own infrastructure.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores and refreshes Kimi tokens on the local machine.

Mitigation: Install only on infrastructure you control, protect the local credential file, and treat token command output as secret.

Risk: The optional background proxy can persist API keys or KIMI_* environment variables in service files.

Mitigation: Review environment variables before running install-service and use the background service only when a persistent local relay is intended.

Risk: Optional OpenRouter fallback can switch failed membership calls to pay-per-token usage.

Mitigation: Set OPENROUTER_API_KEY only when fallback billing is acceptable and keep the documented daily fallback cap enabled.

Risk: Release metadata includes an unrelated ClawHub credential-location note.

Mitigation: Publisher should remove credential-location metadata before publication or downstream redistribution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/askegor/skills/space-duck-kimi-relay)
- [Kimi authentication endpoint](https://auth.kimi.com)
- [Kimi coding API endpoint](https://api.kimi.com/coding/v1)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code]

**Output Format:** [Markdown with command examples and Python script behavior]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local login, token refresh, probe, proxy, service installation, status, and logout workflows for agents.]

## Skill Version(s):

0.4.0 (source: server release evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
