## Description:

Classifies security incidents, vulnerabilities, and threat reports by their causal weaknesses using the TLCTC v2.6 taxonomy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[barnes70](https://clawhub.ai/user/barnes70)

### License/Terms of Use:

MIT-0

## Use Case:

Security analysts and incident responders use this skill to classify cyber incidents, CVEs, and threat reports, and to explain attack paths, uncertainty, and defensive controls using TLCTC v2.6.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad activation wording may steer general security analysis toward TLCTC even when another framework is preferred.

Mitigation: Explicitly request another framework or a comparison when TLCTC is not the intended lens.

## Reference(s):

- [TLCTC framework](https://www.tlctc.net)
- [TLCTC v2.6 core paper](https://doi.org/10.5281/zenodo.20633176)
- [ClawHub skill release](https://clawhub.ai/barnes70/skills/tlctc-classify)

## Skill Output:

**Output Type(s):** [Markdown, JSON]

**Output Format:** [Structured Markdown analysis report with optional JSON export]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes cluster assignments, attack paths, confidence, and control recommendations; timing and boundary annotations when supported by evidence.]

## Skill Version(s):

2.6.0 (source: skill frontmatter and release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
