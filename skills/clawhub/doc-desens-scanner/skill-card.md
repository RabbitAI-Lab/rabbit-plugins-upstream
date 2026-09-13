## Description:

Scans documents, code, and logs for PII, secrets, internal paths, and internal project codenames, then masks detected content and emits an audit-style desensitization report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers, security reviewers, and release owners use this skill before external sharing to identify and mask sensitive content in documents, code, and logs while retaining a record of what was redacted.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Report mode can expose sensitive prefixes in logs or captured console output.

Mitigation: Avoid report mode for real secrets or PII unless output handling is controlled and reviewed.

Risk: The current scanner behavior may not return the documented nonzero exit code when sensitive data is detected.

Mitigation: Do not rely on the exit code alone as a CI or publication gate until detection exit behavior is reviewed and fixed.

Risk: The release security verdict is suspicious and recommends review before deployment.

Mitigation: Install only from a pinned, reviewed commit or release and review the scanner before operational use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/doc-desens-scanner)
- [Publisher profile](https://clawhub.ai/user/zhaoxinghua09-cell)
- [LGD Hub](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell command examples; the scanner emits masked text and optional JSON report output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local processing; report mode may print sensitive plaintext prefixes and should be used carefully.]

## Skill Version(s):

1.0.0 (source: server release evidence; artifact frontmatter reports 1.2.0 and manifest reports 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
