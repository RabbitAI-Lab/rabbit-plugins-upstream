## Description:

Book Hotels helps agents use the RollingGo CLI to search hotels by destination, dates, ratings, budget, tags, and distance, then retrieve hotel details, room availability, prices, and booking links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[longcreat](https://clawhub.ai/user/longcreat)

### License/Terms of Use:

MIT-0

## Use Case:

External users and travel-planning agents use this skill to find candidate hotels, compare hotel details and current room pricing, inspect hotel tags, and guide booking through returned hotel or booking URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs the RollingGo CLI from npm or PyPI at the latest available version and uses a RollingGo API key.

Mitigation: Verify that the user is comfortable with the current RollingGo CLI package before execution, and provide the API key through host-scoped environment injection.

Risk: The artifact and metadata use both RollingGo_API_KEY and ROLLINGGO_API_KEY naming.

Mitigation: Confirm the exact environment variable expected by the installed CLI before use and configure that variable in the execution environment.

Risk: Passing an API key on the command line can expose it through shell history, process listings, or logs.

Mitigation: Prefer environment-variable injection over command-line --api-key usage.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/longcreat/skills/book-hotels)
- [RollingGo](https://rollinggo.store)
- [RollingGo API Key Application](https://rollinggo.store/apply)
- [Claw Host Environment Reference](references/claw-host-env.md)
- [RollingGo NPX Reference](references/rollinggo-npx.md)
- [RollingGo UV Reference](references/rollinggo-uv.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with bash commands and JSON CLI results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a RollingGo API key and a RollingGo CLI runtime through rollinggo, npx, npm, uvx, or uv.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
