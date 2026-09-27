## Description:

Reads Workday org charts, worker profiles, compensation, benefits, performance, and other accessible pages through your signed-in browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and authorized developers use this skill to read Workday people, team, pay, benefits, and performance information available to their signed-in account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reads may expose sensitive Workday HR information about the user or coworkers.

Mitigation: Review requests and returned data; limit queries to information needed for the task and avoid broad compensation, benefits, or performance requests.

Risk: The skill accesses Workday using a live signed-in browser session and includes broad raw-read tools.

Mitigation: Confirm employer permission for browser-session access before installing and use raw reads only for specific authorized pages.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/workday-mcp)
- [workday-mcp npm package](https://www.npmjs.com/package/workday-mcp)
- [fetchproxy browser extension setup](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [JSON, Guidance]

**Output Format:** [Structured JSON responses and text guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only; some responses are partial or require further navigation.]

## Skill Version(s):

1.1.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
