## Description:

Turn a written campaign and reward-tier plan into one gallery still per named slot. This crowdfunding gallery studio lays out each named reward-tier still and campaign scene as its own still. Use it for Indiegogo gallery stills, Kickstarter gallery frames, reward-tier tiles, and campaign gallery sets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to convert an already-written crowdfunding campaign and reward-tier plan into approved image-generation requests for gallery stills, reward-tier tiles, and campaign scenes. It emphasizes using confirmed campaign facts, one still per named slot, and billing-aware Beatra task recovery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary states that the package asks for broad Beatra account authority and can silently replace its installed files.

Mitigation: Install only where that account authority and update behavior are acceptable; disable automatic updates with the documented update command when post-review code replacement is not acceptable.

Risk: The package stores a shared Beatra Device Token under ~/.beatra and uses it for remote MCP calls.

Mitigation: Keep the credential files private to the local user, avoid exposing tokens in logs or chat, and do not use this package in environments where shared credential storage is prohibited.

Risk: Generation calls can spend wallet credits and may require recovery after transport failures.

Mitigation: Confirm the live price before billable work, use one client_request_id per still, and retry only identical uncertain requests with the original request identity.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/beatra-ai/skills/indiegogo-gallery-set)
- [Beatra Skill Homepage](https://beatra.ai/skills/indiegogo-gallery-set)
- [Crowdfunding Gallery Workflow](references/workflow.md)
- [Tasks and Results](references/tasks-and-results.md)
- [Billing, Errors, and Recovery](references/billing-errors-and-recovery.md)
- [Installation and Authentication](references/installation-and-auth.md)
- [MCP Connection](references/mcp-connection.md)
- [Automatic Updates and Safety](references/automatic-updates-and-safety.md)
- [Uninstall and Disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with JSON payload examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Plans one still per named slot, uses Beatra task IDs and billing fields, and may return generated image artifacts through remote tasks.]

## Skill Version(s):

0.1.1 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
