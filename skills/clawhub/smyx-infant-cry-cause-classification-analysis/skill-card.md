## Description:

Analyzes infant cry audio or audio-video input through a remote service to classify likely cry causes such as hunger, sleepiness, pain or discomfort, need for attention, fear, colic, or unknown, with confidence and care-oriented guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, parents, caregivers, childcare operators, and developers use this skill to submit infant cry audio or audio-video media for structured cry-cause classification and report retrieval. Results are care-supporting reference information and should not be treated as pediatric diagnosis or emergency guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Infant cry media and report queries may be sent to configured remote services.

Mitigation: Use only with guardian consent, endpoint allowlisting, clear retention and deletion controls, and tenant/account separation.

Risk: The skill may create or reuse persistent local identity or token records.

Mitigation: Store identity and token records in encrypted storage, limit access, and review account separation before use with real family or childcare data.

Risk: Cry-cause classification may be incorrect or overinterpreted as medical advice.

Mitigation: Present results as non-diagnostic guidance and direct users to professional pediatric care for persistent abnormal crying or concerning symptoms.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-infant-cry-cause-classification-analysis)
- [API documentation](references/api_doc.md)
- [smyx analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or JSON-style structured analysis report with cause labels, confidence, secondary causes, feature summary, suggestion hints, and report links when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May query remote services for analysis and historical reports; outputs are advisory and not medical diagnosis.]

## Skill Version(s):

1.0.12 (source: server release evidence and target metadata; artifact frontmatter states 1.0.15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
