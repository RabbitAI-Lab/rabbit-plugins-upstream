## Description:

Helps operators inspect Traefik, Caddy, and HAProxy routing, upstream health, certificates, and errors, and perform supported proxy changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Infrastructure operators and engineers use this skill to diagnose reverse-proxy routing, backend, certificate, and 5xx issues and to make supported Caddy or HAProxy changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write-capable sessions can change live routing or backend availability without an enforced approval boundary.

Mitigation: Use read-only or narrowly scoped proxy credentials first, and require external human review before production writes.

Risk: Stored proxy credentials or a master password exposed in shared configuration can grant unintended access.

Mitigation: Protect ~/.proxy-aiops and avoid storing the master password in plaintext MCP configuration on shared machines.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zw008/skills/proxy-aiops)
- [Project homepage (listed in skill metadata)](https://github.com/AIops-tools/Proxy-AIops)
- [Capabilities and platform support](artifact/references/capabilities.md)
- [CLI reference](artifact/references/cli-reference.md)
- [Setup guide](artifact/references/setup-guide.md)
- [Agent guardrails](artifact/references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include diagnostic findings, change previews, and rollback guidance.]

## Skill Version(s):

0.12.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
