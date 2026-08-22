## Description:

Meituan Travel helps users plan and query hotels, flights, trains, attraction tickets, vacation options, discounts, prices, and itineraries through Meituan travel services.

This skill is ready for commercial/non-commercial use.

## Publisher:

[meituan-travel-ai](https://clawhub.ai/user/meituan-travel-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill as a travel assistant for Meituan hotel, flight, train, attraction ticket, vacation, discount, price comparison, and itinerary queries. The agent authenticates with Meituan Passport when needed and relays Meituan CLI results to the user.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a Meituan Passport login token and may silently reuse cached authorization for travel queries.

Mitigation: Install only when that credential use is acceptable, review cached authorization behavior before deployment, and prefer a version that asks before reusing cached credentials.

Risk: The skill sends the user's full original travel request to the Meituan CLI.

Mitigation: Avoid submitting sensitive personal details that are not needed for the travel query and disclose this data flow to users before use.

Risk: The skill runs or installs npm packages at runtime without tight pinning or user control.

Mitigation: Prefer a version that pins npm packages, avoids automatic global installs, and runs in an environment where npm execution is reviewed and controlled.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/meituan-travel-ai/skills/meituan-travel)
- [Meituan developer portal](https://developer.meituan.com)
- [Meituan Passport reference](artifact/meituan-passport-user-auth/reference.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown travel results and authentication prompts, with shell commands executed by the agent]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CLI output is expected to be passed through without deletion, including links, prices, ratings, and images when present.]

## Skill Version(s):

1.0.12 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
