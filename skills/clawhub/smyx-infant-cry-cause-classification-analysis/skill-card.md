## Description:

Analyzes infant crying in supplied audio or video and reports likely causes, confidence, and caregiving hints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Caregivers and childcare teams can submit infant cry recordings for a cloud-based cause classification and review linked past reports. Results are caregiving aids, not medical diagnoses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive infant audio or video and report history are sent to a cloud service.

Mitigation: Obtain guardian consent and confirm retention, access, and deletion controls with the publisher before submitting real recordings.

Risk: The skill creates or reuses local identity records and stores tokens without a visible identity prompt.

Mitigation: Review account binding and token storage before deployment, and protect local identity records from unauthorized access.

Risk: A probable cry-cause classification may be mistaken for a medical diagnosis.

Mitigation: Use results only as caregiving guidance; seek medical care for persistent or concerning symptoms.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/18072937735/skills/smyx-infant-cry-cause-classification-analysis)
- [Infant cry classification API reference](references/api_doc.md)
- [Analysis API error codes](skills/smyx_analysis/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Text or JSON analysis report; Markdown links for report history]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Likely cause and confidence, caregiving hints, report links, and optional saved output file.]

## Skill Version(s):

1.0.13 (source: server-resolved ClawHub release; bundled frontmatter says 1.0.17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
