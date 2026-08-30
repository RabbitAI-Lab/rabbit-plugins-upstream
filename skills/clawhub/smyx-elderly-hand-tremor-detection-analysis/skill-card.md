## Description:

Analyzes elderly hand-at-rest video or video URLs through a configured health-analysis service to estimate tremor frequency, amplitude, affected side, risk level, and report links for screening support, not medical diagnosis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users such as caregivers, elder-care staff, and community health workers use this skill to submit elderly hand-at-rest videos for tremor screening indicators and report retrieval. The outputs can help decide when to seek qualified clinical review, but they do not replace neurological diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive health-related videos or video URLs may be sent to the configured analysis service.

Mitigation: Use only with consent from the recorded person or their authorized representative, and confirm that the configured endpoint is appropriate for the deployment environment.

Risk: The skill can create or reuse a local identity and store report history, profile data, or tokens in the workspace data directory and SQLite database.

Mitigation: Treat the workspace data directory as sensitive, restrict access to it, and remove local state when the skill is no longer needed.

Risk: Outputs describe tremor risk indicators and report links, which could be mistaken for a medical diagnosis.

Mitigation: Present results as screening support only and route concerning findings to qualified clinical review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-elderly-hand-tremor-detection-analysis)
- [API interface documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown text with structured JSON analysis content and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write the rendered analysis response to a user-specified output file.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact frontmatter reports 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
