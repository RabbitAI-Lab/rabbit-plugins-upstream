## Description:

Scans OpenClaw agent memory files and workspace configuration files for malicious content, credential leaks, prompt injections, and related security threats.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dgriffin831](https://clawhub.ai/user/dgriffin831)

### License/Terms of Use:


## Use Case:

Developers and agent operators use this skill to scan stored OpenClaw memory and workspace configuration files for injected instructions, leaked credentials, prompt stealing attempts, and other security-relevant content before the agent acts on it.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional remote analysis can send memory and configuration content to an external LLM provider after best-effort redaction.

Mitigation: Use the default local scan mode unless remote review is explicitly acceptable, and review redaction expectations before running with --allow-remote.

Risk: The quarantine script modifies target files and can overwrite content outside the intended memory area if pointed at the wrong path.

Mitigation: Run quarantine only on intended memory files after reviewing findings; rely on the backup created under .memory-scan/quarantine/ before restoring or deleting content.

Risk: Scheduled scanning creates persistent daily automation.

Mitigation: Review the cron job after setup and disable it if daily background scans or alert delivery are not wanted.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dgriffin831/skills/memory-scan)
- [README](artifact/README.md)
- [Testing](artifact/TESTING.md)
- [Detection Prompt](artifact/docs/detection-prompt.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Human-readable terminal report, JSON scan results, quiet severity/score line, and concise agent-facing recommendations.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can scan a specific file or recent memory logs; remote LLM analysis is disabled by default and enabled only with --allow-remote.]

## Skill Version(s):

1.0.0 (source: server release metadata and CHANGELOG, released 2026-02-01)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
