## Description: <br>
AI Hotel Booking helps agents use TourMind APIs for live hotel discovery, room-rate comparison, availability checks, booking, order lookup, cancellation, and payment workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kaduzhu-ai](https://clawhub.ai/user/kaduzhu-ai) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and travel-support agents use this skill to search hotels, compare verified room rates, inspect policies and images, create bookings, manage orders, and start payment flows through TourMind. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: TourMind handles live hotel searches, bookings, cancellations, and payment-link workflows. <br>
Mitigation: Install only when that data handling is acceptable for the deployment and disclose live API errors truthfully. <br>
Risk: The skill stores a reusable booking key in a local user_key.txt file for order operations. <br>
Mitigation: Treat the key like a password, restrict file permissions, and remove or rotate it if authorization fails. <br>
Risk: The skill includes an in-chat update flow that can modify installed skill files from remote release sources. <br>
Mitigation: Use the update flow only after independently verifying the release source and installed changes. <br>


## Reference(s): <br>
- [Parameter Guide](references/parameter_guide.md) <br>
- [ClawHub Skill Listing](https://clawhub.ai/kaduzhu-ai/skills/hotel-booking-journione) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, API calls, configuration, guidance] <br>
**Output Format:** [Markdown responses with structured hotel cards, links, tables, and concise booking guidance.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use a local user_key.txt credential for order operations and may surface live API errors as returned.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md frontmatter and ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
