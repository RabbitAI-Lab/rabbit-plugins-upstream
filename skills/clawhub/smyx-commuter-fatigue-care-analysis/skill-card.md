## Description:

Analyzes home-arrival video and optional audio for signs of after-work fatigue and offers supportive care suggestions and report history.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Home users and smart-home developers can analyze living-room video after work to review fatigue indicators, receive gentle care suggestions, and consult historical reports. Results are not medical diagnoses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cloud processing of home video or audio may expose sensitive household activity.

Mitigation: Require explicit opt-in, restrict permitted media sources, and set clear retention limits before enabling monitoring.

Risk: Reports tied to an internal identity and locally stored tokens or history may remain accessible longer than intended.

Mitigation: Protect local credentials and history, limit access, and provide an easy way to delete history or disable monitoring.

Risk: Fatigue indicators can be mistaken for a medical assessment.

Mitigation: Present results as non-diagnostic observations and encourage professional advice for persistent concerns.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-commuter-fatigue-care-analysis)
- [Skill API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis summaries, Markdown report tables, or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include fatigue indicators, care suggestions, and report links.]

## Skill Version(s):

1.0.10 (source: ClawHub release; bundled SKILL.md lists 1.0.16)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
