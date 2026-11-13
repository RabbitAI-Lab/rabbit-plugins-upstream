## Description:

Searches Google Hotels for hotel prices, ratings, amenities, and availability using browser automation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[skillhq-ai](https://clawhub.ai/user/skillhq-ai)

### License/Terms of Use:

MIT

## Use Case:

Travel planners, travelers, and agents use this skill to search Google Hotels, compare accommodation options, and present hotel results without completing bookings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The README install command depends on a mutable package resolution path.

Mitigation: Install from a pinned or otherwise trusted source when possible.

Risk: Hotel and chain websites may request sensitive booking or payment details during deal checks.

Mitigation: Use the skill only to compare availability, rates, and promotions; do not provide payment details or allow booking completion.

Risk: Hotel prices and availability are real-time and may become stale.

Mitigation: Present prices as indicative and verify final rates on the provider or hotel site before acting.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/skillhq-ai/skills/hotel-search)
- [agent-browser](https://github.com/nicobailey/agent-browser)
- [Google Hotels Interaction Patterns](references/interaction-patterns.md)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Guidance]

**Output Format:** [Markdown tables with concise notes and inline shell commands when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results are current, indicative hotel-search outputs; the skill does not complete bookings.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
