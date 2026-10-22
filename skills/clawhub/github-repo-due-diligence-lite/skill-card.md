## Description:

Checks public GitHub repository metadata to summarize maintenance signals, license status, and a simple health heuristic.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nenadzivotic](https://clawhub.ai/user/nenadzivotic)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users assessing a public GitHub dependency can check stars, recent activity, license, and archived status before deciding whether to adopt or monitor it. The metadata-based health label is not a security audit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing an unreviewed source may introduce supply-chain risk.

Mitigation: Verify the repository and use a pinned or reviewed source before installation.

Risk: A repository name supplied for a check is disclosed to GitHub through an API request.

Mitigation: Use public repository names only when that disclosure is acceptable.

Risk: Repository metadata and activity heuristics can be mistaken for a full trust or security assessment.

Mitigation: Review the repository's code, maintainers, and dependencies separately before adoption.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/nenadzivotic/skills/github-repo-due-diligence-lite)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Plain-text summary and recommendation based on JSON repository metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports stars, days since last push, SPDX license identifier when available, archived status, and a heuristic health label.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
