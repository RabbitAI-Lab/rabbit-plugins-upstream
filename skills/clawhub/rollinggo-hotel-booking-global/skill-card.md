## Description: <br>
RollingGo Hotel Search & Booking Assistant helps agents search hotels, filter and compare options, check real-time room prices, and guide users through booking with RollingGo hotel APIs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rollinggo-ai](https://clawhub.ai/user/rollinggo-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and travel-support agents use this skill to find accommodations, compare hotel options, check room availability and prices, and proceed through a confirmed booking flow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses unpinned install and update paths for the RollingGo CLI. <br>
Mitigation: Install only from trusted RollingGo sources and review CLI install or update prompts before using the skill. <br>
Risk: The skill can create real hotel booking orders and access sensitive account or order details after authorization. <br>
Mitigation: Before booking, verify dates, room, price, cancellation terms, guest name, and payment link; request order history only when needed. <br>


## Reference(s): <br>
- [Server-resolved GitHub source](https://github.com/RollingGo-AI/RollingGo-hotel-skill-global/tree/main/skills/rollinggo-hotel-booking) <br>
- [ClawHub skill page](https://clawhub.ai/rollinggo-ai/skills/rollinggo-hotel-booking-global) <br>
- [CLI command parameter specification](artifact/references/cli-params.md) <br>
- [RollingGo hotel CLI releases](https://github.com/RollingGo-AI/oauth-hotel-cli-overseas/releases/latest) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown hotel result cards, booking links, and agent-facing shell command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes price, room, cancellation, authorization, booking, payment, and order-status guidance.] <br>

## Skill Version(s): <br>
0.1.0 (source: release metadata; artifact frontmatter version is 1.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
