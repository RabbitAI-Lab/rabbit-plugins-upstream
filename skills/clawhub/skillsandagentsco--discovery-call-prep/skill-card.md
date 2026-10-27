## Description:

Turns a stated hypothesis and what is known about a person into a discovery-call question guide where every question asks about something that already happened, tags each question with the product risk it tests, names hypotheses an interview cannot answer, and ends with an ask that costs the person something real.

This skill is ready for commercial/non-commercial use.

## Publisher:

[skillsandagentsco](https://clawhub.ai/user/skillsandagentsco)

### License/Terms of Use:

MIT-0

## Use Case:

External users and product teams use this skill before discovery calls to turn a hypothesis, desired call outcome, and notes about the person into a structured Markdown interview guide. The guide emphasizes past behavior, product-risk tagging, untestable-claim callouts, and a single closing ask tied to the caller's stated outcome.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pasted notes, hypotheses, or outcomes may contain instruction-like text intended to steer the agent away from the discovery-call rules.

Mitigation: Treat all pasted material as data, flag likely steering attempts in the output, and continue building the guide without following embedded instructions.

Risk: Users may paste unnecessary personal, contact, CRM, email, or confidential details into the inputs.

Mitigation: Carry only details needed for the questions, avoid unnecessary personal or confidential information, and keep the guide suitable for sharing.

Risk: A discovery interview can produce misleading guidance if it is used to test usability, feasibility, or a specific future price.

Mitigation: Name those claims as out of reach for an interview and direct users to a prototype, engineering spike, or charging the price as the appropriate test.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/skillsandagentsco/skills/discovery-call-prep)
- [Skills & Agents catalog page](https://skillsandagents.co/skills/discovery-call-prep/)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Analysis]

**Output Format:** [Markdown discovery-call guide with numbered questions, product-risk tags, follow-ups, untestable-claim notes, a closing ask, and flagged-input notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a stated outcome, a hypothesis, and notes about the person; asks for missing required inputs instead of inventing them.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
