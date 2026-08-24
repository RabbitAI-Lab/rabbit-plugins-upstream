## Description:

Collects coffee chat signup details, checks duplicate WeChat IDs, and writes new or updated records to a Feishu Bitable through a relay server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[moljay](https://clawhub.ai/user/moljay)

### License/Terms of Use:

MIT-0

## Use Case:

Event organizers and operators use this skill with an AI assistant to collect participant name, job, WeChat ID, and entrepreneurship experience, then de-duplicate and submit records to a self-managed Feishu Bitable relay.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may start a local Node relay process without making that startup visible to the user.

Mitigation: Require explicit user consent before starting the relay, or run the relay manually under operator control.

Risk: The release includes a shared relay API key in its configuration examples and defaults.

Mitigation: Remove or rotate the bundled key before use and configure a unique API key for each controlled relay server.

Risk: Submitted names, jobs, WeChat IDs, and entrepreneurship experience are stored in the configured Feishu table.

Mitigation: Obtain clear consent before collection, restrict table access, and define retention rules for submitted personal information.

Risk: The ping shortcut returns a deployment-style confirmation that can obscure the actual signup result.

Mitigation: Replace the deployment-style response with a truthful signup confirmation before using the skill with participants.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/moljay/skills/fork-latte-skill)
- [Feishu Open Platform](https://open.feishu.cn)
- [Feishu tenant access token API](https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal)
- [Feishu Bitable records API](https://open.feishu.cn/open-apis/bitable/v1/apps/{BASE_TOKEN}/tables/{TABLE_ID}/records)

## Skill Output:

**Output Type(s):** [Text, Markdown, API calls, Shell commands, Configuration]

**Output Format:** [Natural-language prompts and status messages with JSON REST payloads and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Collects personal signup data and may update or create records in a configured Feishu Bitable relay.]

## Skill Version(s):

1.0.4 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
