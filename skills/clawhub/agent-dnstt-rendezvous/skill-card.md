## Description:

Authorization-gated coordination skill for agents that need to plan, verify, and troubleshoot a DNSTT client/server link without sharing private keys, scanning resolvers, changing DNS/firewalls, or auto-executing tunnel commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT No Attribution

## Use Case:

Developers and operators use this skill to coordinate authorized DNSTT client/server handoffs, generate human-reviewed argv plans, verify cards and status reports, and troubleshoot bounded connection states without running tunnels automatically.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unauthorized DNSTT coordination could support activity on infrastructure the operator does not own or administer.

Mitigation: Use the skill only with explicit authorization for the domain, resolver, server, and service.

Risk: Generated argv plans may be unsafe if executed without review or against an unexpected DNSTT build.

Mitigation: Review every generated plan before execution and compare it with the installed DNSTT tool's help output.

Risk: HMAC secrets or private coordination details could be exposed through prompts, logs, or copied status text.

Mitigation: Keep HMAC secrets out of prompts and logs, and use the skill's secret-free card and status handoff patterns.

Risk: Running external DNSTT tools after planning can create observable DNS tunnel metadata.

Mitigation: Assume DNS resolvers and network operators can observe tunnel metadata and run plans only in approved environments.

## Reference(s):

- [Agent DNSTT Rendezvous on ClawHub](https://clawhub.ai/orionshaowswmw/skills/agent-dnstt-rendezvous)
- [Inspiration and License Boundaries](references/INSPIRATION.md)
- [Original DNSTT Documentation](https://www.bamsoftware.com/software/dnstt/)
- [anonvector/dnstt](https://github.com/anonvector/dnstt)
- [anonvector/SlipNet](https://github.com/anonvector/SlipNet)
- [anonvector/slipgate](https://github.com/anonvector/slipgate)
- [anonvector/DNS-Multiplexer](https://github.com/anonvector/DNS-Multiplexer)
- [WhiteDNS/WhiteDNS-Android](https://github.com/WhiteDNS/WhiteDNS-Android)
- [WhiteDNS/CottenDNS](https://github.com/WhiteDNS/CottenDNS)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON argv plans and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local planning and diagnostic artifacts for human review; it does not execute external DNSTT tools.]

## Skill Version(s):

1.1.2 (source: frontmatter, CHANGELOG, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
