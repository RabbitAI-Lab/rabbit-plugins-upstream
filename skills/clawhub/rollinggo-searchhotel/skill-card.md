## Description:

RollingGo SearchHotel helps an agent search, compare, price-check, and book hotels through RollingGo hotel service flows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dreamtzlong](https://clawhub.ai/user/dreamtzlong)

### License/Terms of Use:

MIT-0

## Use Case:

External users and travel-support agents use this skill to find hotels by location or amenities, compare room options and prices, and continue into confirmed booking and order lookup flows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can install or update executable booking tools from npm or release binaries.

Mitigation: Install only in a trusted environment, review the referenced package and binaries before use, and pin or approve tool updates where operational policy requires it.

Risk: The skill can create real hotel orders and payment links.

Mitigation: Require explicit user selection and confirmation before price locking or booking, and verify guest name, email, dates, room, cancellation policy, and total price before order creation.

Risk: The skill runs local CLI wrappers with broad execution authority.

Mitigation: Run it with least-privilege local permissions and avoid exposing unrelated credentials or sensitive files in the execution environment.

Risk: Silent update checks and dynamic command discovery may change behavior during use.

Mitigation: Review update prompts and command help before high-impact booking actions, and re-run price confirmation if a locked price expires.

## Reference(s):

- [CLI parameter reference](references/cli-params.md)
- [ClawHub skill page](https://clawhub.ai/dreamtzlong/skills/rollinggo-searchhotel)
- [RollingGo hotel npm package](https://www.npmjs.com/package/@rollinggo/hotel)
- [RollingGo hotel CLI releases](https://github.com/RollingGo-AI/oauth-hotel-cli/releases/latest)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown hotel result cards, room and order summaries, and agent-executed shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses real-time hotel search, price confirmation, booking, and order lookup flows; payment links are produced only after user confirmation.]

## Skill Version(s):

1.0.5 (source: ClawHub release metadata; artifact frontmatter lists 1.1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
