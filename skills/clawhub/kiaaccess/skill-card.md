## Description:

Kiaaccess helps an agent answer questions about a user's Kia vehicle and, when explicitly confirmed, use Kia Access / Kia Owners account capabilities such as status checks, location lookup, EV charge checks, door locks, climate, and charging commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect an agent to their own Kia Owners account for vehicle status, location, EV charging information, and confirm-gated remote commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Vehicle-affecting commands can unlock, lock, charge, or change climate on a real car.

Mitigation: Prefer read-only mode unless commands are needed, require explicit user confirmation before each command, and treat dry-run results as previews rather than completed actions.

Risk: Kia credentials and exported refresh tokens provide sensitive account and vehicle access.

Mitigation: Avoid storing credentials in project files, protect exported refresh tokens as MFA-bypass secrets, and never echo passwords, session IDs, or refresh tokens into conversation.

Risk: Running the MCP package through mutable npm resolution can execute package code that has changed since review.

Mitigation: Pin and review the MCP package version before running it in a trusted environment.

Risk: Cached vehicle status or command acceptance can be mistaken for confirmed current state.

Mitigation: Refresh and re-read vehicle status when freshness matters, and distinguish command acceptance from confirmed vehicle state.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/kiaaccess)
- [kiaaccess-mcp npm package](https://www.npmjs.com/package/kiaaccess-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON configuration examples and tool-use guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May describe dry-run previews, status reads, and confirmation requirements for vehicle-affecting commands.]

## Skill Version(s):

0.8.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
