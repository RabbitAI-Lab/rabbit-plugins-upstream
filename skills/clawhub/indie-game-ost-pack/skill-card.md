## Description:

Build an original indie game OST pack of 8 to 15 instrumental tracks for title, explore, battle, shop, and victory.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and indie game teams use this skill to plan and generate a labeled pack of original instrumental game background music for common game slots such as title, exploration, battle, shop, and victory.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad Beatra account permissions and uses a shared local Beatra device authorization.

Mitigation: Install only if that authorization is acceptable, keep the token only in the protected Beatra credential file, and revoke or uninstall the connection when it is no longer needed.

Risk: Credentials are stored under ~/.beatra and are shared by Beatra skill packages on the same device.

Mitigation: Protect the local account, do not copy tokens into chat, logs, command arguments, environment variables, backups, or diffs, and use the bundled uninstall workflow to clean up shared state.

Risk: Silent package updates are enabled by default.

Mitigation: Disable automatic updates before use when reviewed, stable code is required, and run explicit update checks during controlled maintenance.

Risk: Each music generation call is paid and transport uncertainty can otherwise create duplicate work.

Mitigation: Confirm the live pack estimate before the first paid call, use one stable client_request_id per slot, and recover uncertain requests with the same frozen payload instead of submitting replacements.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/beatra-ai/skills/indie-game-ost-pack)
- [Beatra Skill Homepage](https://beatra.ai/skills/indie-game-ost-pack)
- [Indie game OST workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with labeled soundtrack details, inline JSON payloads, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports slot order, actual duration, MIME type, size, URL or artifact ID, resolved model, and billing.net_charged_credits when generation tasks complete.]

## Skill Version(s):

0.1.1 (source: server release evidence and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
