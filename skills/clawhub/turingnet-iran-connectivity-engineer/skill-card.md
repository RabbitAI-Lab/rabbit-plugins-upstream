## Description:

TuringNet Iran Connectivity Engineer helps agents perform privacy-first, lawful troubleshooting for Iran-context connectivity outages, Wi-Fi and mobile-data failures, DNS/TLS issues, ISP escalation, redacted evidence, bilingual support tickets, and low-bandwidth reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

Support agents, help desks, incident leads, and authorized network operators use this skill to triage Iran-context connectivity issues, redact sensitive evidence, draft bilingual support materials, and prepare low-bandwidth reports. It is intended for lawful troubleshooting within user-owned or explicitly authorized scopes, not bypass, scanning, or credential collection.

### Deployment Geography for Use:

Iran

## Known Risks and Mitigations:

Risk: The skill handles sensitive troubleshooting evidence, and the server security summary says its privacy and guard guarantees are weakened by implementation issues.

Mitigation: Review before installing, review redacted output before sharing, avoid --collect on shared machines, and do not use --skip-guard.

Risk: Explicit networked commands can contact status pages or owned targets when invoked.

Mitigation: Only allowlist known public status-page hosts and run owned-scope diagnostics only with clear authorization.

Risk: The installation fallback using npx @latest can retrieve changing package contents.

Mitigation: Use a pinned or reviewed installation path instead of the npx @latest fallback until the issue is fixed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/orionshaowswmw/skills/turingnet-iran-connectivity-engineer)
- [Agent discovery](artifact/AGENT_DISCOVERY.md)
- [README](artifact/README.md)
- [Version history](artifact/references/history.md)
- [Verdict schema](artifact/schema/verdict.v1.schema.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command snippets, JSON verdicts, redacted text, support tickets, checklists, and low-bandwidth HTML reports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python3, bash, and curl; network use is off by default except explicit status-page requests and owned-scope diagnostics.]

## Skill Version(s):

2.3.2 (source: server release metadata; artifact frontmatter lists 2.3.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
