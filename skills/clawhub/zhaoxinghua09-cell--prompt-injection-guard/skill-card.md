## Description:

Scans selected text or files for patterns across eight threat categories and can produce a structured risk report and an SVG badge.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security reviewers can scan an explicitly selected prompt, document, or file for suspicious patterns and review the resulting findings before deciding what to do.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The scanner's SAFE badges can mislead users, and promised file protections and secret masking are missing.

Mitigation: Do not rely on the SAFE badge or use this release as a security gate; require fixes for path containment, overwrite protection, and secret masking before use.

Risk: Evaluation on unintended files could expose sensitive content or produce unsafe results.

Mitigation: Evaluate only in isolation with explicitly selected test files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/prompt-injection-guard)
- [LGD hub](https://zhaoxinghua09-cell.github.io/lgd-hub/)
- [LGD formal paper](https://doi.org/10.5281/zenodo.22456647)

## Skill Output:

**Output Type(s):** [JSON, SVG file]

**Output Format:** [Structured JSON scan report on stdout; optional SVG badge file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports pattern matches and a verdict; accepts text or a selected file.]

## Skill Version(s):

1.0.7 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
