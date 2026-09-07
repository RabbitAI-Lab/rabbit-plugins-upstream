## Description:

Idempotent Rebuild Verification helps agents verify pinned workspace rebuilds with an offline deterministic CLI that classifies benign versus damaging hash drift, checks manifests, extracts runbook pins and steps, and routes post-wipe recovery actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill when a hash-pinned runbook rebuild or snapshot wipe leaves files missing or mismatched. It helps classify drift, validate pinned files, extract runbook steps safely, and decide which writer, download, compile, or shim steps should be rerun.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The CLI can read selected files and inspect selected directories during verification and wipe audits.

Mitigation: Run it only against intended project paths and avoid broad roots that may expose unrelated project structure.

Risk: Commands such as extract-steps with --write-steps and gen-fixtures write to user-specified output directories.

Mitigation: Use private, newly created output directories rather than shared paths such as /tmp/steps or /tmp/fix.

Risk: Security evidence marks the release as requiring review because some write and audit behavior may affect more local files than expected.

Mitigation: Review the skill and scanner summary before deployment, and keep usage limited to explicitly chosen verification workspaces.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/orionshaowswmw/skills/idempotent-rebuild-verification)
- [Drift Classes](references/drift_classes.md)
- [Runbook Extraction](references/runbook_extraction.md)
- [Snapshot Semantics](references/snapshot_semantics.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON-producing CLI examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The bundled CLI emits machine-readable JSON and uses exit codes 0, 2, and 3 for success, input errors, and detected drift or missing files.]

## Skill Version(s):

2.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
