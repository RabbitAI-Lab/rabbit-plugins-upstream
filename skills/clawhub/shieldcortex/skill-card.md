## Description:

Memory and defence for AI agents: semantic recall, knowledge graph and decay, plus a memory firewall that scans and enforces against prompt injection, credential leaks and poisoning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jarvis-drakon](https://clawhub.ai/user/jarvis-drakon)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use ShieldCortex to retain and recall agent knowledge, scan for security threats, and configure memory protections across supported agent hosts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad access to agent configuration, rules, credentials scans, and transcripts may expose sensitive local context.

Mitigation: Review requested access and disable auto-memory on sensitive projects.

Risk: Automatic hook self-heal may write to agent hook directories without prompting.

Mitigation: Disable self-heal if automatic hook changes are not acceptable.

Risk: Optional cloud sync and webhooks may transmit memory or event data off-device.

Mitigation: Leave cloud sync and webhooks disabled unless needed and review their configuration before enabling.

Risk: An on-demand npx fallback may fetch and run an unpinned package.

Mitigation: Use a reviewed, locally installed and pinned ShieldCortex binary.

## Reference(s):

- [ShieldCortex documentation](https://shieldcortex.ai/docs)
- [ShieldCortex homepage](https://shieldcortex.ai)
- [ShieldCortex npm package](https://www.npmjs.com/package/shieldcortex)
- [ClawHub skill listing](https://clawhub.ai/jarvis-drakon/skills/shieldcortex)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Plain text and Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include recalled memories, scan findings, and setup guidance.]

## Skill Version(s):

5.10.5 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
