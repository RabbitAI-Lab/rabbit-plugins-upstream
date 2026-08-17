## Description:

Search and book hotels with live room rates and real-time availability, including property comparison, room and policy review, reservation creation, order management, cancellation, and payment by Stripe, WeChat Pay, or Alipay.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tourmind](https://clawhub.ai/user/tourmind)

### License/Terms of Use:

MIT

## Use Case:

External users and travel-focused agents use this skill to search hotels, compare live room rates and cancellation terms, verify availability, create reservations, manage bookings, and start payment workflows through TourMind.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may store a TourMind user_key.txt credential locally for booking, order, cancellation, and payment operations.

Mitigation: Installers should protect the local credential file, avoid committing it, and remove or refresh it when authorization fails or access is no longer needed.

Risk: The security scan summary flags broad self-update authority from remote release sources.

Mitigation: Avoid the in-skill self-update path unless the release source is independently verified, and review file changes before replacing an installed skill.

Risk: Hotel rates, inventory, taxes, fees, and cancellation terms are time-sensitive and can change before booking.

Mitigation: Use the skill's final availability and price verification step before creating a booking, and show only terms returned by TourMind APIs.

Risk: Booking and payment actions can affect real reservations and charges.

Mitigation: Require explicit user confirmation, guest legal name, contact email, selected room, checked rate, order identifier, and payment method before order or payment API calls.

## Reference(s):

- [Hotel Booking AI on ClawHub](https://clawhub.ai/tourmind/skills/hotel-booking-ai)
- [TourMind publisher profile](https://clawhub.ai/user/tourmind)
- [Hotel Booking AI ToC API and Field Reference](references/parameter_guide.md)
- [TourMind Skill API](https://api.tourmind.com)
- [TourMind AgentAuth dashboard](https://aauth-170125614655.asia-northeast1.run.app/dashboard)

## Skill Output:

**Output Type(s):** [Text, Markdown, API calls, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown hotel recommendations, room details, booking status, payment links, and setup guidance with inline shell commands where needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include hotel and room images, live-price tables, cancellation summaries, read-only result links, order identifiers, and payment URLs.]

## Skill Version(s):

1.0.2 (source: server release metadata; artifact SKILL.md declares 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
