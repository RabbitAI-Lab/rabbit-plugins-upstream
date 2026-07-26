## Description: <br>
Scans OpenClaw agent memory files and workspace configuration files for malicious instructions, prompt injection, credential leakage, and related security threats. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dgriffin831](https://clawhub.ai/user/dgriffin831) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to scan OpenClaw memory, daily logs, and workspace configuration files for stored prompt attacks, exposed credentials, and other security threats before continuing agent work. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The scanner can read OpenClaw memory and workspace configuration files that may contain sensitive content. <br>
Mitigation: Install and run it only when memory and configuration scanning is intended, and review findings before sharing or acting on them. <br>
Risk: Remote analysis can send redacted memory content to OpenAI or Anthropic when explicitly enabled. <br>
Mitigation: Keep remote scanning disabled unless external LLM analysis is intended; use --allow-remote only after confirming the data-sharing posture. <br>
Risk: Quarantine actions modify memory files by redacting lines or replacing files. <br>
Mitigation: Use quarantine only after reviewing findings; the artifact creates backups before modification so original content can be inspected or restored. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dgriffin831/skills/memory-scan) <br>
- [README](artifact/README.md) <br>
- [Detection prompt](artifact/docs/detection-prompt.md) <br>
- [Testing](artifact/TESTING.md) <br>
- [Changelog](artifact/CHANGELOG.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Human-readable scan summaries, optional JSON reports, quiet severity-score output, and shell commands for scanning, scheduling, or quarantine.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Severity levels are SAFE, LOW, MEDIUM, HIGH, and CRITICAL; MEDIUM or higher findings are intended for review and optional alerting.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and changelog, released 2026-02-01) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
