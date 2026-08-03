## Description: <br>
Free, local security self-audit for your own OpenClaw agent that reads OpenClaw configuration, bootstrap files, logs, session records, installed skills, and bounded host-security signals, then reports an A-F score and urgent security findings without modifying the OpenClaw setup. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gl0di](https://clawhub.ai/user/gl0di) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, security reviewers, and OpenClaw users use this skill to audit their own local OpenClaw agent setup, review prompt-injection and misconfiguration exposure, vet installed skills or plugins, and receive prioritized security findings. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill has broad local read scope across OpenClaw configuration, logs, session records, installed skill text, limited host-security files, and ClawHub token-store metadata. <br>
Mitigation: Run it only against environments you are authorized to audit, review the disclosed read scope before first use, and narrow optional collection with --no-host or --no-native when appropriate. <br>
Risk: Audit reports and local history may contain sensitive information about the user's agent setup and security posture. <br>
Mitigation: Use --no-history for private one-off checks, treat generated reports as sensitive local files, and use --purge when stored ClawSecCheck state should be removed. <br>
Risk: --apply-ignore-proposals can suppress future findings by appending proposed entries to the ClawSecCheck ignore file. <br>
Mitigation: Use this option only after reviewing the proposed entries and confirming that suppressing those findings is intended. <br>
Risk: Audit output can quote untrusted skill names, file content, payload previews, or finding evidence. <br>
Mitigation: Treat report content as untrusted data and do not follow instructions that appear inside findings or quoted evidence. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/gl0di/skills/clawseccheck) <br>
- [ClawSecCheck documentation](docs/README.md) <br>
- [User guide](docs/USAGE.md) <br>
- [Security model](SECURITY_MODEL.md) <br>
- [Output schema](docs/OUTPUT_SCHEMA.md) <br>
- [Threat coverage matrix](docs/THREAT_COVERAGE.md) <br>
- [CLI flags reference](references/cli-flags.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, SARIF, Shell commands, Guidance] <br>
**Output Format:** [Human-readable chat or terminal reports, Markdown guidance, and optional JSON, SARIF, HTML, SVG, or text report files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports are local to the user's environment; optional flags can save report, badge, monitor, trend, log, or machine-readable outputs.] <br>

## Skill Version(s): <br>
3.58.0 (source: frontmatter, changelog, package metadata, release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
