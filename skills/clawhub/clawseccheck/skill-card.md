## Description:

ClawSecCheck is a local OpenClaw security self-audit that reads agent configuration, logs, session metadata, installed skills, and selected host artifacts to report risks, changes, and A-F grades when all five audit layers run.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gl0di](https://clawhub.ai/user/gl0di)

### License/Terms of Use:

MIT

## Use Case:

Developers and OpenClaw users use this skill to audit their own agent setup, review prompt-injection and misconfiguration risks, monitor drift, and receive local security findings without sending scan data off the machine.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The scanner can read broad local OpenClaw configuration, logs, session metadata, installed skill/plugin text, selected host-security artifacts, and OpenClaw environment files.

Mitigation: Install and run it only where that local read scope is acceptable; use containment flags such as --no-history, --no-host, --no-deptree, and --no-native when a narrower scan is needed.

Risk: Raw environment-file values may enter scanner process memory during scans.

Mitigation: Avoid running the skill in environments where that process-memory exposure is unacceptable, or run it only after reducing sensitive environment-file content.

Risk: Findings and scanned skill content may contain hostile or misleading text.

Mitigation: Treat audit output as untrusted evidence, summarize findings in your own words, and act only on the user's explicit instructions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/gl0di/skills/clawseccheck)
- [Security Model](SECURITY_MODEL.md)
- [User Guide](docs/USAGE.md)
- [Check Catalog Reference](docs/CHECKS.md)
- [Output Schema](docs/OUTPUT_SCHEMA.md)
- [CLI Flags Reference](references/cli-flags.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and text summaries with optional report files such as JSON, SARIF, HTML, PDF, and badges]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally; output may include security findings, coverage notes, grades when all audit layers run, drift events, and reviewed command proposals.]

## Skill Version(s):

4.0.1 (source: SKILL.md frontmatter, CHANGELOG, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
