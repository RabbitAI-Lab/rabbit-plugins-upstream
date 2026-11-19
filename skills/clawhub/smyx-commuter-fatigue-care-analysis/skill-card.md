## Description:

Analyzes the first 30 minutes of after-work living-room activity for possible fatigue and returns supportive care suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Smart-home users can use a short living-room video to review possible signs of after-work fatigue and receive a structured assessment with gentle self-care suggestions. The skill is intended for supportive wellbeing, not medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Security guidance raises concern about external processing of private home video.

Mitigation: Use the skill only if you are comfortable with that processing and can limit recordings to the intended living-room context.

Risk: Security evidence flags account registration, identity and token handling concerns, unexpected behavior, and a data-flow issue; scan coverage was partial.

Mitigation: Review the reported behavior and data flows before use, and resolve the missing-reference coverage before connecting personal accounts or video.

## Reference(s):

- [API reference](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Guidance]

**Output Format:** [Structured fatigue assessment and care suggestions in JSON; historical reports in Markdown tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include an estimated 0–100 fatigue index, observed cues, and suggested comfort actions. It does not provide a medical diagnosis.]

## Skill Version(s):

1.0.16 (source: server-resolved release metadata; bundled artifact frontmatter reports 1.0.24)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
