## Description:

Memory and defence for AI agents: semantic recall, knowledge graph and decay, plus a memory firewall that scans and enforces against prompt injection, credential leaks and poisoning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jarvis-drakon](https://clawhub.ai/user/jarvis-drakon)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use ShieldCortex to give AI agents persistent local memory, semantic recall, knowledge graph support, and security checks for prompt-injection, credential-leak, and poisoning risks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can persist conversation-derived content in local memory and audit storage.

Mitigation: Review or disable auto-memory, keyword triggers, and proactive recall before sensitive work, and delete local memory or audit data when it is no longer needed.

Risk: Cloud sync and webhook features can transmit selected data or metadata when the user enables them.

Mitigation: Keep cloud sync and webhooks disabled unless needed, configure only trusted endpoints, and review the data classes enabled for sync.

Risk: Self-heal behavior can maintain OpenClaw hook files across sessions.

Mitigation: Disable self-heal with the documented configuration or environment variable when persistent hook maintenance is not desired.

Risk: Some host integrations receive memory and scanner guidance without an enforceable tool gate.

Mitigation: Check the reported integration posture before relying on blocking behavior, and treat unbound integrations as advisory.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jarvis-drakon/skills/shieldcortex)
- [ClawHub publisher profile](https://clawhub.ai/user/jarvis-drakon)
- [ShieldCortex homepage](https://shieldcortex.ai)
- [ShieldCortex documentation](https://shieldcortex.ai/docs)
- [ShieldCortex npm package](https://www.npmjs.com/package/shieldcortex)
- [ShieldCortex changelog](https://shieldcortex.ai/changelog)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide local setup, memory operations, security review, and configuration; runtime behavior depends on the integrations and options the user enables.]

## Skill Version(s):

4.54.14 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
