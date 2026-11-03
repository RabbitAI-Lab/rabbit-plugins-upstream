## Description:

Memory and defence for AI agents: semantic recall, knowledge graph and decay, plus a memory firewall that scans and enforces against prompt injection, credential leaks and poisoning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jarvis-drakon](https://clawhub.ai/user/jarvis-drakon)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use ShieldCortex to give AI agents persistent memory and scan for or enforce against prompt injection, credential leaks, and memory poisoning across supported integrations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: OpenClaw hooks may download executable packages at runtime and can automatically copy or remove hook files during self-heal.

Mitigation: Review hooks before enabling them, prefer reviewed and pinned local executables with runtime package downloads blocked, and disable self-heal and back up legacy hooks if automatic migration is not wanted.

Risk: Captured memories may contain conversation content, and cloud sync or configured webhooks can transmit data.

Mitigation: Review captured memories and leave cloud sync and webhooks disabled unless you intend to share their payloads.

## Reference(s):

- [ShieldCortex documentation](https://shieldcortex.ai/docs)
- [ShieldCortex npm package](https://www.npmjs.com/package/shieldcortex)
- [ShieldCortex homepage](https://shieldcortex.ai)
- [Publisher GitHub profile](https://github.com/Drakon-Systems-Ltd)
- [ClawHub release page](https://clawhub.ai/jarvis-drakon/skills/shieldcortex)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Setup steps and enforcement capabilities depend on the agent host.]

## Skill Version(s):

5.17.3 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
