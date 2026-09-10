## Description:

NanoClaw runtime traffic monitoring baseline for host-side proxy inspection with container-safe MCP and IPC status surfaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[davida-ps](https://clawhub.ai/user/davida-ps)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security engineers use this skill as a NanoClaw baseline for designing opt-in host-side traffic monitoring, redacted findings, and bounded container-safe MCP status surfaces.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Short installer commands can bypass stronger artifact verification.

Mitigation: Prefer the signed release verification workflow before installing or extracting release artifacts.

Risk: Future traffic monitoring could expose secrets in logs or MCP responses.

Mitigation: Redact snippets before persistence or responses, bound scanned bytes, and keep findings limited to redacted status data.

Risk: HTTPS inspection could expose CA private key material or mutate system trust unexpectedly.

Mitigation: Keep CA private keys host-side, require explicit per-runtime trust configuration, and never install a system-wide CA automatically.

Risk: The reviewed artifact is a specification scaffold rather than an active runtime monitor.

Mitigation: Treat it as implementation guidance and review future proxy, detector, IPC, and MCP code before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/davida-ps/skills/clawsec-nanoclaw-traffic-guardian)
- [ClawSec homepage](https://clawsec.prompt.security)
- [NanoClaw Traffic Guardian README](artifact/README.md)
- [NanoClaw Traffic Guardian Specification](artifact/SPEC.md)
- [NanoClaw Traffic Guardian Changelog](artifact/CHANGELOG.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, configuration details, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Current release is a specification scaffold; active proxy, detector, and MCP runtime behavior must be implemented and reviewed separately.]

## Skill Version(s):

0.0.2 (source: evidence.json release, SKILL.md frontmatter, skill.json, CHANGELOG released 2026-09-07)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
