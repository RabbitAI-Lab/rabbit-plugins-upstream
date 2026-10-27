## Description:

Scan Python code for security vulnerabilities with the open-source Frame CLI, triage the findings, generate and verify fixes, and re-scan.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sandeep85das](https://clawhub.ai/user/sandeep85das)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to scan Python repositories or files for security issues, triage findings, and review proposed fixes and verification scans.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional AI-assisted scanning may send code snippets to a hosted endpoint.

Mitigation: Obtain approval before sending code externally and review which repository files the endpoint can access.

Risk: Suggested fixes may be incorrect or change project behavior.

Mitigation: Review the proposed diff, approve changes before applying them, and keep a backup.

Risk: A clean scan may miss vulnerabilities and does not establish that code is secure.

Mitigation: Treat scan results as one input to security review rather than proof of safety.

## Reference(s):

- [Frame CLI project](https://github.com/lambdasec/frame)
- [Findings triage checklist](references/triage-checklist.md)
- [ClawHub skill release](https://clawhub.ai/sandeep85das/skills/frame-security-scan)

## Skill Output:

**Output Type(s):** [Guidance, Analysis, Shell commands, Code]

**Output Format:** [Markdown guidance, shell commands, scan findings, and unified diffs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings and fixes depend on the scanned Python code and selected scan options.]

## Skill Version(s):

1.0.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
