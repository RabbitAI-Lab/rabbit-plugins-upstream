## Description:

Hotel search, comparison, and booking with live room rates and real-time availability.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tourmind](https://clawhub.ai/user/tourmind)

### License/Terms of Use:

MIT

## Use Case:

External travelers and travel-planning users use this skill to search hotels, compare live room products, verify rates and availability, and manage booking, payment, cancellation, and order lookup in one agent conversation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can ask the agent to store a booking user_key in a local plaintext file, which could expose account access if copied into prompts, logs, screenshots, commits, or support tickets.

Mitigation: Keep the key local, restrict file access where supported, and avoid placing the key in prompts, logs, screenshots, commits, or support requests.

Risk: The skill includes an update flow that asks the agent to update installed skill files from server-provided release links.

Mitigation: Approve updates only after verifying the source and release, and preserve local changes and the local user_key file during any update.

## Reference(s):

- [Hotel Booking AI API and Field Reference](references/parameter_guide.md)
- [Hotel Booking AI on ClawHub](https://clawhub.ai/tourmind/skills/hotel-booking-ai)
- [TourMind Skills Product Page](https://tourmind.com/skills)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown conversational responses with structured hotel options, booking summaries, and order or payment guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live TourMind hotel data for prices, policies, availability, booking status, and payment flows.]

## Skill Version(s):

1.0.5 (source: server release metadata; artifact frontmatter reports 1.0.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
