## Description:

Detects AI-generated writing patterns in prose.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, documentation maintainers, and reviewers use this skill to inspect prose, documentation, and code comments for AI-writing markers, identity leaks, unsupported claims, hallucinated references, and stub or deferral language before publication or merge.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill's behavior can extend beyond read-only prose detection into broad repository cleanup, security sweeps, code-change recommendations, CI or pre-commit setup, and local scan-history writes.

Mitigation: Install only when a broad documentation and repository cleanup assistant is intended; run it with explicit targets and review proposed security, configuration, CI, and pre-commit changes before accepting them.

Risk: Automated remediation can remove useful context or make incorrect edits when findings are low confidence or when generated, vendored, historical, safety-critical, or contract-bearing files are involved.

Mitigation: Keep unattended runs report-only, avoid auto-applying low-confidence findings, and require human review before remediation or changes to protected file classes.

Risk: Using tracking mode stores scan history in the repository.

Mitigation: Use tracking only when repository-local history is acceptable and review generated history files before committing.

## Reference(s):

- [Clawdis homepage](https://github.com/athola/claude-night-market/tree/master/plugins/scribe)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown reports, JSON or JSON Lines for CI, and inline shell/configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can include per-finding severity, confidence, evidence, rationale, fixes, diffs, scan summaries, CI exit codes, and optional local scan-history files.]

## Skill Version(s):

1.9.19 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
