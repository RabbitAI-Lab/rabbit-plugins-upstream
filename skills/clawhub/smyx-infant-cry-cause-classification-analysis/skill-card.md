## Description:

Analyzes supplied infant-cry audio to estimate possible causes from acoustic features and return a confidence-rated result with a supportive prompt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Parents and childcare staff use the skill to review an infant-cry audio clip and get an indicative classification of possible causes. Its suggestions are caregiving aids, not medical diagnoses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Infant recordings may be sent for cloud analysis, while the no-analysis option, workspace identity reuse, automatic account creation, token protection, and recording retention or deletion are not clearly explained.

Mitigation: Delay using real infant recordings until the no-analysis option is fixed and these identity, credential, and recording-handling practices are clearly explained.

Risk: The skill describes continuous monitoring and phone alerts, but the bundled code does not establish that these functions are available.

Mitigation: Treat the skill as an on-demand analysis aid and do not rely on it for continuous monitoring or alerts.

Risk: A suggested cry cause could be mistaken for a medical assessment.

Mitigation: Treat classifications as non-clinical guidance; seek pediatric care for persistent or concerning crying or symptoms.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-infant-cry-cause-classification-analysis)
- [API interface documentation](references/api_doc.md)
- [Analysis API error codes](skills/smyx_analysis/references/api_doc.md)
- [Skill usage demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, JSON, Markdown]

**Output Format:** [Structured analysis results or Markdown report text, with optional report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include a possible cause, confidence, acoustic summary, and directional soothing suggestion; results are advisory.]

## Skill Version(s):

1.0.15 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
