## Description:

Optional Space Duck add-on that signs a self-hosted runtime into Kimi locally and runs a protected localhost OpenAI-compatible proxy using the user's Kimi membership, with optional capped OpenRouter fallback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[askegor](https://clawhub.ai/user/askegor)

### License/Terms of Use:

MIT-0

## Use Case:

Developers running self-hosted Space Duck use this add-on to authenticate locally with Kimi membership and expose a localhost OpenAI-compatible proxy for inference. It helps keep Kimi credentials on the user's machine while optionally using a capped OpenRouter fallback.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Kimi access and refresh tokens are stored locally for the relay.

Mitigation: Install only when local Kimi token custody is acceptable; keep the default 0600 credential files and use logout or uninstall flows when the relay is no longer needed.

Risk: Inference is processed by Moonshot/Kimi infrastructure in China.

Mitigation: Do not route workloads through this lane when Western data residency or a different processing region is required.

Risk: Disabling localhost proxy authentication can allow other local processes to spend the user's Kimi quota.

Mitigation: Keep the auto-generated bearer secret enabled; use KIMI_RELAY_NO_AUTH=1 only on a single-user machine.

Risk: OPENROUTER_API_KEY or KIMI_* environment variables may be persisted when installing the relay service.

Mitigation: Review relevant environment variables before running install-service and keep the fallback daily cap configured for acceptable spend.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/askegor/skills/space-duck-kimi-relay)
- [Security Manifest](artifact/SECURITY-MANIFEST.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and configuration values]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide local commands that create credential files under ~/.kimi-code/credentials and start a localhost proxy.]

## Skill Version(s):

0.8.11 (source: server release evidence and artifact/_meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
