## Description:

ship-it audits a named feature, release, branch, or module for operational readiness across logging, error handling, telemetry, feature flags, migrations, rollback, secrets, local-first storage, auth, and update strategy before launch.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dennisrongo](https://clawhub.ai/user/dennisrongo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill before release to check whether a scoped change is operationally ready to ship and to receive a structured PASS, GAP, N/A, and final-verdict report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill inspects repository files and may search for secret-shaped values while gathering readiness evidence.

Mitigation: Run it only in trusted workspaces and review any security-related findings before sharing the report.

Risk: An underspecified release scope can lead to incomplete operational-readiness findings.

Mitigation: Name the PR, branch, release tag, feature flag, module, or directory before the audit and require PASS findings to include file:line evidence and a named probe.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown report with categorized findings, file:line evidence, named probes, and recommendation text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill reports findings first and avoids code edits unless the user explicitly approves follow-up fixes.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
