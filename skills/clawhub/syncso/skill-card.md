## Description:

Finds New York City events and activities with dates, prices, images, booking links, and personalized recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liangstl](https://clawhub.ai/user/liangstl)

### License/Terms of Use:

MIT-0

## Use Case:

People and their assistants use SyncSo to discover and plan New York City outings suited to their dates, budgets, locations, and accessibility needs.

### Deployment Geography for Use:

New York City, United States (activity coverage)

## Known Risks and Mitigations:

Risk: An account-linked bearer code does not expire on its own and may expose the user's allowance if disclosed.

Mitigation: Prefer OAuth with scoped, expiring access tokens where available; protect the code and replace it if exposed.

Risk: Planning requests can disclose location, budget, accessibility needs, allergies, and other personal context to SyncSo.

Mitigation: Share only relevant details with the user's awareness; avoid card details and unrelated sensitive information.

## Reference(s):

- [SyncSo ClawHub release](https://clawhub.ai/liangstl/skills/syncso)
- [SyncSo account connection](https://syncso.com/connect)
- [SyncSo MCP endpoint](https://rtdb.syncso.com/partner/mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown event recommendations with dates, venues, prices, images, and booking links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results are ordered for the user's request; available activities are limited to New York City.]

## Skill Version(s):

2.0.1 (source: server-resolved ClawHub release; artifact frontmatter says 2.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
