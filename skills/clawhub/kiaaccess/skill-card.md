## Description:

Helps an agent use a user's Kia Access or Kia Owners account to check vehicle status, location, EV charge, and run confirm-gated lock, climate, and charging commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and their agents use this skill to read Kia account vehicle information and perform explicit, confirm-gated vehicle commands for the user's own enrolled Kia vehicle.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access sensitive Kia account and vehicle data and can run commands that affect a real vehicle.

Mitigation: Install only when this access is intended; use KIA_WRITE_MODE=none for read-only use, keep the default or stricter mode unless commands are needed, and use all only when confirm-gated door lock and unlock authority is acceptable.

Risk: The Kia password and exported refresh token can provide broad account access or bypass MFA.

Mitigation: Treat KIA_PASSWORD, KIA_RMTOKEN, and session identifiers as full account credentials and do not echo them into conversations or logs.

Risk: Vehicle commands may be accepted by Kia without the vehicle state being confirmed immediately.

Mitigation: Require confirm: true for command execution, distinguish dry runs from real commands, and verify important state changes with a follow-up vehicle status read.

Risk: Vehicle status and location can be stale or privacy-sensitive.

Mitigation: Describe location as last reported rather than live, and refresh then re-read status when freshness matters.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/kiaaccess)
- [kiaaccess-mcp npm package](https://www.npmjs.com/package/kiaaccess-mcp)
- [kiaaccess-mcp repository](https://github.com/chrischall/kiaaccess-mcp)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with JSON configuration snippets and tool-use guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Kia account credentials; command tools are controlled by KIA_WRITE_MODE and explicit confirmation.]

## Skill Version(s):

0.6.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
