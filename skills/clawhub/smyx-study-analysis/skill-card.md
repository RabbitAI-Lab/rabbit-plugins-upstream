## Description:

Analyzes child or student study videos to identify learning behavior patterns, poor study habits, concentration and posture issues, then returns structured reports and family education suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Parents, guardians, educators, and agents use this skill to analyze child or student study-session videos or video URLs and receive structured learning behavior reports. It can also query cloud-hosted historical analysis reports associated with the configured internal identity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Child or student videos and video URLs are sent to a configured cloud service for analysis.

Mitigation: Use only recordings with appropriate consent and avoid regulated, school, medical, or highly private recordings unless retention and deletion assurances are acceptable.

Risk: The skill can create or reuse an internal account identity and store service tokens locally.

Mitigation: Review local workspace data and remote account history before deployment, and establish a process for deleting local identity data and cloud-hosted report history.

Risk: The analysis is educational guidance and may be inaccurate or incomplete for learning difficulties.

Mitigation: Treat reports as family education reference material and seek qualified teachers or professionals for serious concerns.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-study-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API interface documentation](artifact/references/api_doc.md)
- [SMYX analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown and structured JSON report text, with optional saved output file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include analysis status, behavior findings, risk notes, family education suggestions, historical report records, and report export links.]

## Skill Version(s):

1.0.12 (source: server release metadata; artifact frontmatter says 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
