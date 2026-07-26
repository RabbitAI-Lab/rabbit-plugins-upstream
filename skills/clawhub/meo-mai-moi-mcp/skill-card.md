## Description: <br>
Connect, authorize, and safely use Meo Mai Moi through its OAuth MCP gateway for pet profiles, care and health records, habits, microchips, sharing, rehoming or placement, helper profiles, messages, groups, pet finances, notifications, and account workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[troioi-vn](https://clawhub.ai/user/troioi-vn) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to connect OAuth-capable agents such as Codex, Cursor, or OpenClaw to Meo Mai Moi, choose appropriate OAuth scopes, and safely perform pet-care workflows through the MCP gateway. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Authorizing broad OAuth scopes can allow reads or writes to sensitive pet records, including finances, messages, sharing, placement, groups, profile data, and invitations. <br>
Mitigation: Use the Everyday care preset or narrower task-specific scopes by default, and choose Full management only after explicit user selection and a sensitivity warning. <br>
Risk: Consequential writes may affect health history, finances, access, messages, invitations, or real-world pet handoffs. <br>
Mitigation: Read the target state before writing, use stable IDs and versions, apply a fresh idempotency key for each intended write, and verify the result with a follow-up read. <br>
Risk: OAuth credentials, authorization codes, invitation material, personal records, health data, or financial values could be exposed in chat or logs. <br>
Mitigation: Never request or repeat tokens or secrets; handle short-lived OAuth callback codes only in a private one-to-one flow, exchange them immediately, and keep sensitive records out of chat unless needed for the user's decision. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/troioi-vn/skills/meo-mai-moi-mcp) <br>
- [Connection and scope selection](references/connection.md) <br>
- [OpenClaw native MCP onboarding](references/openclaw.md) <br>
- [Safety and error handling](references/safety.md) <br>
- [Meo MCP clients documentation](https://github.com/troioi-vn/meo-mcp/blob/main/docs/clients.md) <br>
- [Meo MCP tools documentation](https://github.com/troioi-vn/meo-mcp/blob/main/docs/tools.md) <br>
- [Meo MCP OAuth documentation](https://github.com/troioi-vn/meo-mcp/blob/main/docs/oauth.md) <br>
- [Meo MCP errors documentation](https://github.com/troioi-vn/meo-mcp/blob/main/docs/errors.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline shell commands and scope strings] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces OAuth MCP connection guidance, scope selection advice, safe operation steps, and recovery guidance.] <br>

## Skill Version(s): <br>
0.3.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
