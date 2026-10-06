## Description:

Scans prompts before sharing for exposed credentials, internal paths, personal information, custom sensitive terms, and instructions that could leak a system prompt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (Python code); all rights reserved (documentation and theory)

## Use Case:

Developers and other people preparing prompts for publication or sharing use this skill to identify possible leaks and embedded prompt-disclosure instructions before release.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scanned prompts and finding samples may contain sensitive material.

Mitigation: Scan only intended local files, keep findings private, and review any samples before sharing.

Risk: The declared file-writing and web-access tools exceed what the local scanner needs.

Mitigation: Invoke the scanner locally on explicit inputs instead of granting broad autonomous access.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/zhaoxinghua09-cell/skills/prompt-leak-scanner)
- [Publisher project homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Plain-text findings or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings include category, severity, position, and a sample; high-risk findings return exit code 1, while medium-risk findings require review.]

## Skill Version(s):

1.0.3 (source: ClawHub release metadata; bundled version labels differ)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
