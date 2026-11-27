## Description:

Scan an AI-agent skill or MCP server folder for malicious or risky behaviour before installing it — credential and SSH key reads, data exfiltration, network sends, hidden instructions, obfuscation, and install-time tricks in code, scripts and manifests. Use when asked to scan, vet, audit or check a skill, plugin or MCP server before installing it, when a skill looks suspicious, or when reviewing a SKILL.md someone shared. Not for general security review of ordinary code projects, for checking CI workflow files (use ci-command-truth), or for checking package dependencies in a pull request (use phantomdep-pr-gate).

This skill is ready for commercial/non-commercial use.

## Publisher:

[raktikoo](https://clawhub.ai/user/raktikoo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security reviewers use SkillScan to inspect an AI-agent skill or MCP server folder before installing it. It reports a verdict with file- and line-linked findings and can produce machine-readable or review-friendly reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing the scanner from a GitHub URL carries supply-chain risk even when this skill's scan verdict is benign.

Mitigation: Review the installation source and use a virtual environment for the install; treat a clean verdict as limited to the files scanned.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/raktikoo/skills/skillscan)
- [SkillScan GitHub repository](https://github.com/RakTikoo/skillscan)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown, JSON, SARIF]

**Output Format:** [Plain-text verdict and findings, or JSON, Markdown, or SARIF reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings identify the rule, file, and line; incomplete scans cannot receive a clean PASS.]

## Skill Version(s):

0.10.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
