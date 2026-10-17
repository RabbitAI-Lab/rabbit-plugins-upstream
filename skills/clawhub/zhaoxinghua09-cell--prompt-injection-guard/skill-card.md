## Description:

Provides static pattern-based checks for prompt injection, hardcoded secrets, destructive commands, and exfiltration in text or files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents can screen text or files for suspicious instruction and security patterns before deciding whether to use them. Treat the results as review signals, not a trusted safety decision.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The command-line scanner fails to start because of a missing import.

Mitigation: Require a working CLI and test it on representative inputs before relying on scan results.

Risk: Declared filesystem permissions do not match the file-reading and badge-writing behavior.

Mitigation: Review and restrict filesystem access to the input and optional output paths before running it.

Risk: Verification claims and badges may imply safety even when risks are present.

Mitigation: Do not treat verification claims or badges as proof of safety; require honest FAIL/UNSAFE labeling and human review.

## Reference(s):

- [Prompt Injection Guard on ClawHub](https://clawhub.ai/zhaoxinghua09-cell/skills/prompt-injection-guard)

## Skill Output:

**Output Type(s):** [Text, JSON, SVG badge]

**Output Format:** [Plain text or JSON risk report; optional SVG badge]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes matched threat categories, snippets, scores, and a verdict when the command runs successfully.]

## Skill Version(s):

1.0.1 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
