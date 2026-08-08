## Description:

AigoHotel MCP helps agents search, compare, and book hotels through RollingGo hotel services, including location-based search, filtering, room-price lookup, and booking guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dreamtzlong](https://clawhub.ai/user/dreamtzlong)

### License/Terms of Use:

MIT-0

## Use Case:

External users and travel-focused agents use this skill to find hotels by destination, amenities, price, or brand, compare available rooms and prices, and proceed through booking with user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs and runs external RollingGo hotel-booking software that can handle hotel searches, login authorization, order history, and unpaid order creation.

Mitigation: Install only when the publisher and RollingGo tooling are trusted; review the npm package or release source and prefer a pinned, verified installer before use.

Risk: The skill performs silent daily version checks and may require persistent local or global installation behavior.

Mitigation: Monitor update prompts and installation paths, and review upgrade behavior before allowing the agent to continue booking workflows.

Risk: Hotel booking can create real unpaid orders and expose payment links.

Mitigation: Require explicit user confirmation for room selection, traveler contact details, price locking, and order creation before submitting booking commands.

## Reference(s):

- [CLI command parameter reference](references/cli-params.md)
- [ClawHub skill page](https://clawhub.ai/dreamtzlong/skills/aigohotel-mcp)
- [ClawHub publisher profile](https://clawhub.ai/user/dreamtzlong)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Guidance]

**Output Format:** [Markdown hotel result cards, booking prompts, payment-link guidance, and command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include hotel names, star ratings, prices, distances, amenities, room details, cancellation terms, order identifiers, and payment links.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
