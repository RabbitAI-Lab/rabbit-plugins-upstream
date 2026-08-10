## Description:

Find Hotel helps agents use the RollingGo CLI to search hotels by destination, dates, star rating, budget, tags, and distance, then retrieve hotel details, room prices, and hotel tag catalogs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[longcreat](https://clawhub.ai/user/longcreat)

### License/Terms of Use:

MIT-0

## Use Case:

Travel-planning agents and users use this skill to find candidate hotels, compare structured search results, retrieve current room pricing, and prepare booking links through RollingGo. It is intended for hotel search and hotel-detail workflows, not other travel booking categories such as flights or car rentals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Hotel search details are sent to RollingGo.

Mitigation: Confirm the user is comfortable sharing destination, date, occupancy, budget, and preference details with RollingGo before running searches.

Risk: The RollingGo API key could be exposed if passed directly on a command line.

Mitigation: Configure the key through a protected environment variable or secret manager rather than using --api-key in shell history.

Risk: The documentation uses both ROLLINGGO_API_KEY and RollingGo_API_KEY.

Mitigation: Use RollingGo_API_KEY where host metadata and references require it, and verify the runtime environment before invoking CLI commands.

## Reference(s):

- [RollingGo website](https://rollinggo.store)
- [RollingGo API key application](https://rollinggo.store/apply)
- [Find Hotel on ClawHub](https://clawhub.ai/longcreat/skills/find-hotel)
- [RollingGo NPX reference](references/rollinggo-npx.md)
- [RollingGo UV reference](references/rollinggo-uv.md)
- [Claw host environment reference](references/claw-host-env.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON result expectations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide RollingGo CLI calls that return JSON hotel search results, hotel details, room prices, hotel tags, booking URLs, and hotel detail links.]

## Skill Version(s):

1.0.1 (source: server release evidence; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
