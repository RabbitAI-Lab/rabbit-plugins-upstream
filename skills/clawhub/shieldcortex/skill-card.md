## Description:

ShieldCortex gives AI agents persistent semantic memory and a memory firewall that scans for prompt injection, credential leaks, and poisoning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jarvis-drakon](https://clawhub.ai/user/jarvis-drakon)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users use ShieldCortex to retain and retrieve context across sessions, scan agent inputs and memories for threats, and review security findings. Protection and enforcement depend on the host integration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic memory capture or environment audits may retain sensitive agent or session data.

Mitigation: Review auto-memory and audit settings before use in sensitive projects, and establish retention and deletion practices.

Risk: Optional cloud sync and configured webhooks may transmit memory content or event data.

Mitigation: Leave integrations disabled unless needed; review their destinations, data scope, and credentials before enabling them.

Risk: The OpenClaw hook can repair its installation automatically at gateway startup.

Mitigation: Review self-heal settings and disable self-heal when managing hooks manually.

Risk: An OpenClaw fallback may download and run a mutable npm package when no local install is available.

Mitigation: Prefer a pinned local ShieldCortex installation and review fallback behavior before enabling the hook.

## Reference(s):

- [ClawHub release](https://clawhub.ai/jarvis-drakon/skills/shieldcortex)
- [ShieldCortex documentation](https://shieldcortex.ai/docs)
- [ShieldCortex homepage](https://shieldcortex.ai)
- [ShieldCortex npm package](https://www.npmjs.com/package/shieldcortex)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Memory recall, scan findings, and security guidance vary by host integration.]

## Skill Version(s):

5.8.0 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
