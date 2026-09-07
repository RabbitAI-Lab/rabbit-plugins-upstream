## Description:

Authorization-gated coordination skill for agents that need to plan, verify, and troubleshoot a DNSTT client/server link without sharing private keys, scanning resolvers, changing DNS/firewalls, or auto-executing tunnel commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, and authorized operators use this skill to coordinate DNSTT client/server handoffs, generate reviewable command plans, verify rendezvous cards and status chains, and troubleshoot connection state without automatically executing tunnels or sharing private keys.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unauthorized DNSTT use or policy evasion.

Mitigation: Use only for domains, resolvers, servers, and services the operator owns or is explicitly authorized to administer.

Risk: Incorrect or unsafe tunnel command execution.

Mitigation: Review generated command_argv values before running them; the skill produces plans and does not execute tunnel commands.

Risk: Key substitution or unsigned handoff.

Mitigation: Use HMAC-authenticated cards when possible and verify the server public-key fingerprint through an independent channel.

Risk: Private-key or coordination-secret exposure.

Mitigation: Keep private keys server-side with strict permissions and avoid placing secrets in cards, logs, status messages, prompts, or issue reports.

Risk: Open-proxy or unintended LAN exposure.

Mitigation: Keep upstream services and client listeners loopback-bound unless broader access is explicitly reviewed and authorized.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/orionshaowswmw/skills/agent-dnstt-rendezvous)
- [Inspiration, License Boundaries, and Originality](references/INSPIRATION.md)
- [Original DNSTT Documentation](https://www.bamsoftware.com/software/dnstt/)
- [anonvector/dnstt](https://github.com/anonvector/dnstt)
- [anonvector/SlipNet](https://github.com/anonvector/SlipNet)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance and local JSON artifacts, including deterministic argv arrays, rendezvous cards, status reports, diagnostic summaries, and compact JSON envelopes when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The helper emits reviewable plans and local files only when the operator supplies an output path; it does not execute tunnel commands.]

## Skill Version(s):

1.2.0 (source: server release metadata, SKILL.md frontmatter, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
