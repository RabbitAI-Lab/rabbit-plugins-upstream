## Description:

Memory and defence for AI agents: semantic recall, knowledge graph and decay, plus a memory firewall that scans and enforces against prompt injection, credential leaks and poisoning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jarvis-drakon](https://clawhub.ai/user/jarvis-drakon)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use ShieldCortex to give AI agents persistent semantic memory and knowledge-graph recall, and to scan memory, agent instructions, and tool activity for security threats. It also provides setup and configuration guidance for supported agent integrations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The OpenClaw hook may resolve and run mcporter or ShieldCortex through npx when no local executable is available, allowing package downloads during hook operation.

Mitigation: Install reviewed ShieldCortex and mcporter versions where the gateway can find them before enabling the hook, so it does not need npx to fetch them.

Risk: The hook bootstrap self-heal can copy hook files and remove two named legacy hook directories without prompting.

Mitigation: Review the affected paths first; set SHIELDCORTEX_SKIP_SELF_HEAL=1 or configure self-heal off, then restart the gateway to make the hook warn without writing.

Risk: The integrations can read agent configuration and memory data, and enabled lifecycle handlers can capture conversation context into persistent local memory.

Mitigation: Review the capture and scan settings, disable automatic memory capture or lifecycle handlers when they are not wanted, and inspect stored memories periodically.

Risk: The scanner reports partial coverage because referenced paths were missing from the scanned artifact.

Mitigation: Treat the scan result as incomplete and review the missing paths and installed package before enabling automatic hooks.

## Reference(s):

- [ShieldCortex documentation](https://shieldcortex.ai/docs)
- [ShieldCortex npm package](https://www.npmjs.com/package/shieldcortex)
- [ShieldCortex ClawHub release](https://clawhub.ai/jarvis-drakon/skills/shieldcortex)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands, Configuration]

**Output Format:** [Structured MCP responses and plain-text guidance, with shell commands and configuration instructions when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Memory, scan results, and security guidance may reflect local agent and project data.]

## Skill Version(s):

5.20.3 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
