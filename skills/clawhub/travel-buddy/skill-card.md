## Description:

Helps travelers discover and compare destinations, build day-by-day trip plans, and revise plans when requirements change.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dong845](https://clawhub.ai/user/dong845)

### License/Terms of Use:

MIT-0

## Use Case:

Travelers use this skill to explore destinations, compare options against their needs, and create or revise itineraries with booking links and verification notes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Locally saved trip plans and preferences may contain personal travel details.

Mitigation: Use profiles only with consent; do not enter passport numbers, payment details, credentials, or exact addresses, and protect or delete local files when no longer needed.

Risk: Explicitly starting a separate planner can create an unattended agent run.

Mitigation: Keep automatic planner spawning off unless intentionally selecting --assistant codex or --assistant claude.

Risk: Travel prices, availability, entry requirements, and opening hours can change.

Mitigation: Check time-sensitive claims against current sources before making reservations or travel decisions.

## Reference(s):

- [Initial intake](references/initial-intake.md)
- [Profile and storage](references/profile-and-storage.md)
- [Verification](references/verification.md)
- [Booking-ready HTML output](references/booking-html-output.md)

## Skill Output:

**Output Type(s):** [Guidance, HTML, JSON]

**Output Format:** [Travel recommendations and saved day-by-day HTML/JSON plans]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional locally saved traveler profile and verification report]

## Skill Version(s):

2.8.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
