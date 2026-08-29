## Description:

Discovery Call Prep creates hypothesis-driven discovery-call question guides that ask about past behavior, tag each question by product risk, identify claims an interview cannot test, and end with one concrete ask.

This skill is ready for commercial/non-commercial use.

## Publisher:

[edakrong](https://clawhub.ai/user/edakrong)

### License/Terms of Use:

MIT-0

## Use Case:

Product teams, founders, and customer-facing operators use this skill before discovery calls to turn a stated outcome, hypothesis, and person notes into a risk-tagged question guide grounded in past behavior.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may process business and person-specific notes pasted by the user.

Mitigation: Avoid including unnecessary private contact details or sensitive CRM content, especially in guides that will be shared.

Risk: Pasted outcome, hypothesis, or person notes may contain instruction-shaped text.

Mitigation: Treat pasted content as data, flag likely injection attempts, and continue without following embedded directions.

Risk: Discovery interviews can produce misleading confidence for usability, feasibility, or specific pricing claims.

Mitigation: Name those claims as untestable in an interview and route them to a prototype, engineering spike, or actual charge as appropriate.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/edakrong/skills/discovery-call-prep)
- [Skills & Agents catalog entry](https://skillsandagents.co/skills/discovery-call-prep/)

## Skill Output:

**Output Type(s):** [markdown, guidance]

**Output Format:** [Markdown discovery-call guide with numbered questions, risk tags, untestable-claims section, closing ask, and flagged input section.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a user-provided outcome, hypothesis, and person notes; does not use MCP tools or external data access.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
