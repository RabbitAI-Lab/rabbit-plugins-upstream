## Description:

ClawSecCheck runs a local OpenClaw security self-audit that inspects configuration, logs, installed skills, host posture, and related surfaces, then reports an A-F grade, findings, and optional machine-readable artifacts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gl0di](https://clawhub.ai/user/gl0di)

### License/Terms of Use:

MIT

## Use Case:

Developers, system administrators, and OpenClaw users use this skill to audit their local agent security, identify prompt-injection, misconfiguration, and supply-chain risks, and generate reports for review or CI gating.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The audit reads broad local OpenClaw, host-posture, installed-skill, log, and credential-store metadata that can reveal sensitive security posture.

Mitigation: Run it only when that scope is intended, treat reports as private, and use --no-host, --no-deptree, --no-sockets, or --no-native to narrow collection.

Risk: Generated reports and history can persist local security metadata on disk.

Mitigation: Use --no-history for ephemeral runs, choose explicit report paths carefully, and use --purge when local ClawSecCheck state should be removed.

Risk: The opt-in ignore-application path can modify the audited home's suppression file.

Mitigation: Use --apply-ignore-proposals only after reviewing the proposed suppressions and confirming the change.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gl0di/skills/clawseccheck)
- [User guide](docs/USAGE.md)
- [Security model](SECURITY_MODEL.md)
- [Output schema](docs/OUTPUT_SCHEMA.md)
- [Check catalog](docs/CHECKS.md)
- [CLI flags reference](references/cli-flags.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files, Shell commands, Guidance]

**Output Format:** [Plain text or Markdown reports, JSON envelopes, SARIF 2.1.0, PDF/HTML/SVG files, and inline shell commands when needed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include sensitive local security metadata; machine-readable JSON and SARIF schemas are documented for automation.]

## Skill Version(s):

3.61.0 (source: server release metadata, SKILL.md frontmatter, CHANGELOG.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
