## Description:

Read and manage your Skylight Calendar family hub — calendar events, chores and reward stars, shared lists (grocery/to-do), and meal plans.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Families use this skill to check and manage their Skylight family hub, including calendars, chores and rewards, shared lists, meals, messages, and albums.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generic shopping or meal requests may access a shared Skylight account without establishing that Skylight is the intended destination.

Mitigation: Require explicit Skylight context or select Skylight as the default before generic requests use the account.

Risk: Configuration files may contain account passwords or other sensitive credentials.

Mitigation: Protect credential-bearing configuration files and never ask the user to paste the Apple app-specific password into chat.

Risk: Changes to recurring items, access, bulk data, uploads, or invited recipients can affect more than the named item or reach people outside the frame.

Mitigation: Keep the documented confirmation gates enabled, show the preview, and act only after the user approves it.

## Reference(s):

- [Skylight Calendar](https://www.ourskylight.com)
- [skylight-mcp on npm](https://www.npmjs.com/package/skylight-mcp)
- [skylight-mcp project page](https://github.com/chrischall/skylight-mcp)

## Skill Output:

**Output Type(s):** [Text, Guidance, Configuration]

**Output Format:** [Natural-language responses and JSON tool results; setup instructions use JSON configuration.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Frame-scoped family hub information and actions; calendar chores require a date range, and account access requires Skylight credentials.]

## Skill Version(s):

1.4.7 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
