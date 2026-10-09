## Description:

Memory and defence for AI agents: semantic recall, knowledge graph and decay, plus a memory firewall that scans and enforces against prompt injection, credential leaks and poisoning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jarvis-drakon](https://clawhub.ai/user/jarvis-drakon)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use ShieldCortex to retain and recall session knowledge, scan agent content for threats, and manage memory across supported integrations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic memory capture can retain sensitive session content locally.

Mitigation: Review auto-memory settings and disable capture for sensitive work.

Risk: Self-heal can modify an existing OpenClaw hook installation without prompting.

Mitigation: Review hook behavior and disable self-heal if automatic changes are unwanted.

Risk: Runtime npx fallback can execute an unpinned npm package in an agent context.

Mitigation: Prefer a reviewed, pinned local or global installation over runtime npx.

Risk: Optional cloud sync can transmit selected memory content and audit metadata.

Mitigation: Keep cloud sync off unless the data and sharing settings are appropriate.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/jarvis-drakon/skills/shieldcortex)
- [ShieldCortex website](https://shieldcortex.ai)
- [ShieldCortex npm package](https://www.npmjs.com/package/shieldcortex)
- [Publisher GitHub profile (listed in metadata)](https://github.com/Drakon-Systems-Ltd)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Text and structured tool responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Memory recall and security scan results depend on enabled integrations and settings.]

## Skill Version(s):

5.5.0 (source: server-resolved release and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
