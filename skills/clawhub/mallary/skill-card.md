## Description:

Guides an agent through Mallary CLI, API, MCP, and workflow tasks with read-only discovery by default, OAuth setup when requested, and state-changing Mallary actions only after clear user authorization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sammydigits](https://clawhub.ai/user/sammydigits)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and operators use this skill when they want an agent to inspect, configure, or operate Mallary accounts through the Mallary CLI or related Mallary workflows. It supports safe discovery, setup, and user-authorized publishing or account operations while preserving credential and profile-data boundaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An agent using this skill may operate Mallary accounts and create public or scheduled social-media posts after a clear user request.

Mitigation: Install only where that authority is acceptable, keep discovery read-only by default, and treat a clear current action request as the authorization boundary.

Risk: OAuth or API-key access can grant broad Mallary account authority.

Mitigation: Keep credentials in trusted environments, use masked secret storage for API keys, and never ask users to paste or print passwords, tokens, or API keys in chat or logs.

Risk: Read-only discovery can expose sensitive profile, account, post, analytics, settings, webhook, or customer metadata.

Mitigation: Request only the data needed for the user's Mallary task and redact identifiers, account labels, post metadata, webhook details, and customer data before sharing output.

Risk: Repeating an uncertain state-changing command can duplicate posts, replies, uploads, settings changes, or account-access changes.

Mitigation: Run requested state-changing actions once, verify the result with a read-only command, and report uncertainty instead of retrying automatically.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/sammydigits/skills/mallary)
- [Mallary Website](https://mallary.ai/)
- [Mallary Documentation](https://docs.mallary.ai)
- [Mallary CLI npm Package](https://www.npmjs.com/package/@mallary/cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and configuration notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the mallary binary; OAuth or MALLARY_API_KEY access should be limited to environments where Mallary account authority is acceptable.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
