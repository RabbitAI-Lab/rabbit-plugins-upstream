## Description:

Hotel search, comparison, and booking with live room rates and real-time availability for hotel and accommodation requests, including recommendations, room details, prices, amenities, cancellation policies, rate verification, reservations, order management, and payment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tourmind](https://clawhub.ai/user/tourmind)

### License/Terms of Use:

MIT

## Use Case:

External travelers and agent users use this skill to search hotels worldwide, compare live room rates, inspect room details and cancellation terms, and complete booking, payment, cancellation, or order lookup after explicit confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Order operations use a local user_key for booking, payment, lookup, and cancellation actions.

Mitigation: Keep the key out of chats, logs, screenshots, and commits; restrict local file permissions and provide it only when an order operation requires it.

Risk: The release includes a self-update flow that can change installed skill instructions from remote release sources.

Mitigation: Use the update flow only after independently verifying the release source and integrity, and avoid overwriting local changes or the local user_key file.

## Reference(s):

- [Hotel Booking AI ToC API and Field Reference](references/parameter_guide.md)
- [ClawHub Skill Page](https://clawhub.ai/tourmind/skills/hotel-booking-ai)
- [TourMind Skills Product Page](https://tourmind.com/skills)

## Skill Output:

**Output Type(s):** [Text, Markdown, API calls, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown responses with tables, links, images when available, and concise operational guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live TourMind hotel, room-rate, availability, booking, payment, order, and cancellation data; public search does not require sign-in, while order operations use a local user_key.]

## Skill Version(s):

1.0.4 (source: ClawHub release metadata; artifact frontmatter declares 1.0.7)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
