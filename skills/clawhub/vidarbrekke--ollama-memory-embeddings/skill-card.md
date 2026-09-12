## Description:

Configure OpenClaw memory search to use Ollama as the embeddings server (OpenAI-compatible /v1/embeddings) instead of the built-in node-llama-cpp local GGUF loading.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vidarbrekke](https://clawhub.ai/user/vidarbrekke)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to configure OpenClaw memory-search embeddings to run through a local Ollama OpenAI-compatible embeddings endpoint. It supports interactive model selection, optional local GGUF import, verification, and drift enforcement for the memory embedding configuration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The installer and enforcement commands can change local OpenClaw memory configuration.

Mitigation: Review the planned configuration change first and keep a backup of ~/.openclaw/openclaw.json before installation or enforcement.

Risk: Preview or check modes may not be strictly read-only according to the security evidence.

Mitigation: Use the read-only audit command for inspection when possible, and run install or enforce commands only in an environment where configuration changes are acceptable.

Risk: The optional launchd watchdog can persistently heal drift by rewriting configuration.

Mitigation: Enable the watchdog only when ongoing automatic config healing is desired, and remove it with watchdog.sh --uninstall-launchd or uninstall.sh when no longer needed.

Risk: Passing real secrets through --api-key-value could expose credentials unnecessarily.

Mitigation: Use a non-secret local placeholder for Ollama and avoid providing real API keys for this local embeddings configuration.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/vidarbrekke/skills/ollama-memory-embeddings)
- [Publisher profile](https://clawhub.ai/user/vidarbrekke)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can guide installation, verification, audit, drift enforcement, watchdog setup, and local OpenClaw memory configuration changes.]

## Skill Version(s):

1.0.4 (source: frontmatter, VERSION.txt, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
