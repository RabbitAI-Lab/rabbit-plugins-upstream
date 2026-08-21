## Description:

Classifies the likely cause of an infant cry from audio or audio-bearing video, returning a structured result with confidence, secondary causes, acoustic feature summary, suggested soothing guidance, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Parents, caregivers, and operators of baby-monitoring workflows can use this skill to submit infant cry audio or audio-bearing video for non-diagnostic cause classification and directional soothing guidance. The skill also supports querying cloud-hosted history for prior infant cry analysis reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill processes sensitive infant audio or video in a cloud-backed workflow.

Mitigation: Use only with clear guardian consent, avoid unnecessary sensitive recordings, and verify backend endpoints before deployment.

Risk: The security review states that the skill silently creates or reuses identity state, stores tokens locally, and retrieves account-linked cloud history without clear user-facing control.

Mitigation: Review local workspace data handling, token storage, and history-query behavior before installation or operational use.

Risk: Infant cry classification can be mistaken for medical certainty.

Mitigation: Present outputs as non-diagnostic acoustic classifications and direct caregivers to professional care for persistent abnormal crying or symptoms.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-infant-cry-cause-classification-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)
- [API error reference](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-style structured analysis reports with result summaries, confidence values, suggestions, and report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May query cloud APIs for analysis results and account-linked report history.]

## Skill Version(s):

1.0.9 (source: server release metadata; SKILL.md frontmatter lists 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
