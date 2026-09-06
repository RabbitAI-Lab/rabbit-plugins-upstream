## Description:

Turingnet helps agents diagnose lawful Iran-context connectivity, Wi-Fi, mobile data, DNS/TLS, ISP, and outage-resilience issues while producing privacy-preserving evidence, support tickets, reports, and operator checklists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

External users, support teams, and authorized network operators use this skill to troubleshoot connectivity and service-reachability problems, collect redacted evidence, draft bilingual support materials, and plan safe incident or outage responses.

### Deployment Geography for Use:

Iran

## Known Risks and Mitigations:

Risk: Local scripts read and write evidence files and can perform explicit network checks.

Mitigation: Review the scripts before installing, run diagnostics only on owned or authorized scope, and allowlist only known public status-page domains.

Risk: The security guidance identifies guard-bypass behavior and shared-system temporary-file concerns.

Mitigation: Do not use --skip-guard for reports, and avoid --collect on shared systems until temporary-file handling is fixed.

## Reference(s):

- [Turingnet ClawHub Skill Page](https://clawhub.ai/orionshaowswmw/skills/turingnet-iran-connectivity-engineer)
- [Version History](references/history.md)
- [Quality Gate and Compatibility Notes](README.md)
- [Machine Verdict Schema](schema/verdict.v1.schema.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance, shell commands, JSON verdicts, redacted evidence files, HTML reports, and reusable templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes guard-gated redaction and reporting workflows; low-bandwidth reports are capped at 100 KB.]

## Skill Version(s):

2.3.1 (source: server evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
