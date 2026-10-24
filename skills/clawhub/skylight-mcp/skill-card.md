## Description:

Connects an authenticated Skylight Calendar account to read and manage family events, chores and rewards, shared lists, and meal plans.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and families can ask an agent to check or update their Skylight family hub, including calendars, chores, rewards, shared lists, meals, and related frame settings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The connector can access private family information and make changes to the selected Skylight frame.

Mitigation: Protect credential configuration, choose the intended frame, and review confirmation previews before approving sensitive changes.

Risk: Recurrence-wide, access, bulk-delete, external-invite, and sharing actions can affect other occurrences, people, or data.

Mitigation: Keep user approval in the loop, verify each preview and its scope, and pin a reviewed package version.

## Reference(s):

- [Skylight Calendar](https://www.ourskylight.com)
- [skylight-mcp project documentation](https://github.com/chrischall/skylight-mcp)
- [skylight-mcp npm package](https://www.npmjs.com/package/skylight-mcp)

## Skill Output:

**Output Type(s):** [Text, Structured data, API calls]

**Output Format:** [Structured Skylight data and requested updates, summarized in text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read and write operations depend on the selected tool; some higher-impact changes require confirmation.]

## Skill Version(s):

1.4.6 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
