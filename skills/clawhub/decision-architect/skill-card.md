## Description:

Decision Architect provides structured decision support for AI agents, including framework selection, cognitive bias checks, risk preference memory, and decision retrospectives.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and teams use this skill to structure product, technical, business, or personal tradeoff decisions, compare options, flag potential cognitive biases, and capture follow-up lessons.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence classifies the release as suspicious because permissions and documentation are inconsistent and broad.

Mitigation: Review the skill before installation, enable only the capabilities needed for decision support, and avoid granting exec unless separately justified.

Risk: The skill may store local decision memory and retrospective notes.

Mitigation: Use it only where local decision memory is acceptable, and avoid entering credentials, regulated data, or third-party sensitive information.

Risk: The artifact contains conflicting network and API-key guidance despite describing a mostly local Markdown-driven workflow.

Mitigation: Do not provide API keys or credentials unless the publisher clarifies the expected network behavior and credential requirements.

Risk: Structured decision output may be incomplete or misleading for high-stakes choices.

Mitigation: Treat outputs as decision-support guidance, keep final decisions with the user, and require professional review for medical, legal, financial, or similarly sensitive decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/decision-architect)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, guidance]

**Output Format:** [Markdown or JSON structured decision analysis]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include option comparisons, framework analysis, bias flags, confidence labels, and retrospective notes.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
