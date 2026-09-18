## Description:

Helps an agent clarify ambiguous user requests through a one-question-at-a-time interview until intent, constraints, success criteria, and out-of-scope work are explicitly confirmed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bogdantanchuk](https://clawhub.ai/user/bogdantanchuk)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill before planning or implementation when a request is underspecified, conventional, or ambiguous. It guides the agent to form hypotheses, ask focused clarifying questions, and obtain explicit confirmation of the user's real intent before downstream work begins.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can slow down ambiguous requests by requiring explicit confirmation of intent before implementation or planning.

Mitigation: Use it when clarification is valuable, and skip it for unambiguous mechanical or purely informational requests.

Risk: An intent document may persist project notes if the user asks to save the confirmed intent.

Mitigation: Only allow the agent to save an intent document after explicit user confirmation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bogdantanchuk/skills/interview)
- [ClawHub publisher profile](https://clawhub.ai/user/bogdantanchuk)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown conversation text and optional Markdown intent document]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a confirmed statement of intent; only saves an intent document when the user explicitly confirms persistence.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
