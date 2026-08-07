## Description:

Detects and repairs partially wiped agent workspaces, verifies files, blobs, trees, and execute bits, and can sync signed recovery manifests off-box with redaction or encryption.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to detect sandbox snapshot loss, repair damaged workspace artifacts, and rebuild missing dependencies or models from signed restore recipes. It is suited to environments where build outputs, virtual environments, large downloads, credentials, or execute bits may disappear between turns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Restore manifests contain shell recipes and bundled recovery utilities can modify files, credentials, dependencies, and workspace state.

Mitigation: Review manifests as executable code, run dry-run checks first, require valid signatures before restore, and grant only the workspace permissions needed for the selected workflow.

Risk: Off-box manifest sync can expose recovery commands, credential placeholders, payload metadata, and endpoint information.

Mitigation: Keep redaction or encryption enabled, verify peer fingerprints out of band, confirm paste hashes on pull, and avoid publishing manifests that have not been reviewed.

Risk: The packaged debugger and auto-recovery helpers have broader process, package, cleanup, diagnostic, and logging behavior than workspace integrity checking alone.

Mitigation: Avoid invoking debugger or recovery helpers unless their behavior is acceptable, inspect logs for sensitive data, and keep diagnostic runs scoped to disposable or backed-up workspaces.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/orionshaowswmw/skills/snapshot-wipe-resilience)
- [README](artifact/README.md)
- [Skill Definition](artifact/SKILL.md)
- [Reference Manifest Example](artifact/reference/manifest.example.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON manifest examples, and command-line status output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent-facing output may include restore plans, diagnostics, JSON status, hashes, signatures, and command exit codes.]

## Skill Version(s):

1.4.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
