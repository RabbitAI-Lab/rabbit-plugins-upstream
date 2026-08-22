## Description:

Analyzes public-place camera images or videos to produce anonymous group-level emotion distributions, a 0-100 group emotion index, operating suggestions, safety-warning guidance, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External operators, developers, and venue analytics teams use this skill to analyze fixed-camera footage from malls, exhibitions, scenic areas, airports, museums, and similar public places. It supports aggregate customer-satisfaction monitoring, service-layout optimization, and human-reviewed public-safety triage.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Public-place footage and account-related identifiers are sent to the provider's cloud service.

Mitigation: Use only in deployments with clear public notice, consent or other lawful basis, documented retention limits, and approval for cloud processing of camera footage.

Risk: The skill creates or reuses local identity state and stores token/profile data.

Mitigation: Before deployment, identify the local data directory, restrict file permissions, define token/profile rotation and deletion procedures, and periodically review generated account records.

Risk: Group emotion and safety-warning outputs can be misused as deterministic judgments about individuals or automatic interventions.

Mitigation: Keep outputs at aggregate venue or region level, prohibit individual pricing or service discrimination, and require human review before operational or safety actions.

## Reference(s):

- [Public Place Group Emotion Index API Documentation](artifact/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-public-place-group-emotion-index-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown or JSON-style structured report text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include emotion distributions, group emotion index, regional breakdowns, operational suggestions, safety suggestions, heatmap/report links, historical report tables, and optional local output files.]

## Skill Version(s):

1.0.10 (source: SKILL.md frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
