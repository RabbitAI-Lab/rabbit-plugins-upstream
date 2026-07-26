## Description: <br>
RollingGo Hotel Booking helps agents search, compare, price-confirm, book, and check hotel orders through RollingGo hotel services. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rollinggo-ai](https://clawhub.ai/user/rollinggo-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Travelers and agent users use this skill to find hotels by destination, dates, budget, amenities, or brand, compare live room options and prices, and proceed to booking with explicit confirmation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill connects an OAuth-enabled hotel CLI to real transaction flows, including price locking, payable order creation, and order history access. <br>
Mitigation: Before booking, require the agent to summarize the hotel, dates, room, total price, cancellation policy, and contact email, then wait for explicit user confirmation. <br>
Risk: The release evidence flags broad activation, automatic update checking, and latest-version installs or downloads as supply-chain concerns. <br>
Mitigation: Install only if the user trusts RollingGo, and do not allow automatic updates or downloads unless the user accepts that supply-chain risk. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/rollinggo-ai/skills/rollinggo-hotel-skill-cn-new) <br>
- [CLI parameter reference](references/cli-params.md) <br>
- [RollingGo hotel CLI releases](https://github.com/RollingGo-AI/oauth-hotel-cli/releases/latest) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown hotel cards, booking and order summaries, and shell commands for the rgh CLI.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include hotel images, booking links, OAuth authorization links, and payment URLs; requires explicit user confirmation before price lock or booking.] <br>

## Skill Version(s): <br>
1.1.1 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
