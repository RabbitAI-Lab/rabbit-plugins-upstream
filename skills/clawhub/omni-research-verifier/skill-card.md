## Description:

Autonomous verification engine that deconstructs claims, evaluates source credibility, and identifies contradictions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mustafa-cuda-dev](https://clawhub.ai/user/mustafa-cuda-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agent users use this skill to check factual claims against live web evidence, compare source credibility, identify contradictions, and return a structured verification report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted claims are sent to DuckDuckGo search during verification.

Mitigation: Do not submit confidential, regulated, or private material unless the skill adds redaction or an explicit opt-in flow.

Risk: The security review notes an unused requests dependency that should be removed or upgraded before broader deployment.

Mitigation: Remove the dependency if it remains unused, or keep it upgraded and scanned as part of release review.

Risk: Web-search evidence and heuristic credibility scores can produce incomplete or misleading conclusions.

Mitigation: Review the returned evidence table, contradictions, and citations before relying on the report for material decisions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/mustafa-cuda-dev/skills/omni-research-verifier)

## Skill Output:

**Output Type(s):** [analysis, text, markdown, code, configuration, guidance]

**Output Format:** [JSON report with executive summary, evidence table, contradictions, citations, confidence score, and processing metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live web access for DuckDuckGo search and should not be used with confidential, regulated, or private claims unless redaction or explicit opt-in handling is added.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
