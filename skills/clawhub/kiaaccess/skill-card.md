## Description:

This skill helps an agent answer questions about a user's Kia vehicle through a Kia Access / Kia Owners account and supports vehicle status, location, EV charge, and confirm-gated vehicle commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect an agent to their own Kia Access account for vehicle status checks, location lookup, EV charging information, and explicitly confirmed comfort or lock commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access Kia account data and vehicle location or status.

Mitigation: Install it only for agents intended to access the user's Kia account, and configure KIA_WRITE_MODE=none when read-only access is sufficient.

Risk: When write mode is enabled, the skill can send real vehicle commands, including climate, charging, and door lock or unlock actions.

Mitigation: Use KIA_WRITE_MODE=comfort for climate and charging only, reserve KIA_WRITE_MODE=all for cases where door lock or unlock authority is accepted, and require explicit confirmation before commands.

Risk: Exported refresh tokens can bypass MFA for the associated Kia session.

Mitigation: Protect KIA_RMTOKEN like a password and use it only when moving a locally bootstrapped session to an environment that cannot complete OTP bootstrap.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/kiaaccess)
- [npm package](https://www.npmjs.com/package/kiaaccess-mcp)

## Skill Output:

**Output Type(s):** [guidance, configuration, API Calls]

**Output Format:** [Markdown with inline JSON configuration and tool-call guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include vehicle status summaries, location links, dry-run previews, and confirmation-aware command results.]

## Skill Version(s):

0.6.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
