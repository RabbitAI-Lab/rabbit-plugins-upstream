## Description:

Hosts a couple compatibility quiz, records answers, and provides private surprise or gift suggestions when the initiator asks afterward.

This skill is ready for commercial/non-commercial use.

## Publisher:

[padepa](https://clawhub.ai/user/padepa)

### License/Terms of Use:

MIT

## Use Case:

External users use this skill to run a lightweight couple quiz and later generate evidence-linked surprise or gift ideas from the participant's answers. It is intended for relationship-content and personal gift-planning workflows where the initiator can manage participant consent and privacy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can collect a partner's quiz answers under a game framing and later reuse them for private gift analysis.

Mitigation: Use it only with clear upfront consent from everyone answering, or revise the prompts to disclose answer recording, retention, and later recommendation use before the quiz begins.

Risk: Gift suggestions may overstate inferred preferences from limited relationship answers.

Mitigation: Keep each recommendation tied to cited answers, label uncertainty, ask for missing constraints such as budget or occasion, and verify purchases before acting.

## Reference(s):

- [Couple content prompt](references/couple-content-prompt.md)
- [ClawHub skill page](https://clawhub.ai/padepa/skills/couple-content)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Conversational text, structured JSON, and Markdown-ready question or gift recommendation content]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Gift recommendations should cite the participant answers they rely on, distinguish stated preferences from inferences, and avoid claims about real-time price or availability.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
