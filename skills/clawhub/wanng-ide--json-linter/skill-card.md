## Description:

Validates JSON syntax across workspace files and reports syntax errors in configuration files, memory files, or data assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wanng-ide](https://clawhub.ai/user/wanng-ide)

### License/Terms of Use:


## Use Case:

Developers and engineers use this skill to scan a workspace or selected directory for malformed JSON in configuration files, memory files, and data assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Recursive scanning can follow symlinks outside the chosen directory and may recurse through symlink cycles.

Mitigation: Run it only on trusted directories until the scanner skips symlinks, enforces a canonical scan-root boundary, and applies recursion limits.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wanng-ide/skills/json-linter)
- [ClawHub publisher profile](https://clawhub.ai/user/wanng-ide)

## Skill Output:

**Output Type(s):** [text, shell commands, guidance]

**Output Format:** [JSON report with file counts, scan timestamp, and invalid-file error details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports scanned, valid, and invalid JSON file counts and includes relative paths and parser messages for invalid files.]

## Skill Version(s):

1.0.0 (source: server release metadata and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
