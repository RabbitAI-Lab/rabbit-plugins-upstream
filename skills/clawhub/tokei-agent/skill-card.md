## Description:

Helps agents manage Tokei launch, waitlist, and giveaway campaigns through a CLI, including publishing, media, analytics, and webhooks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gilesdawe](https://clawhub.ai/user/gilesdawe)

### License/Terms of Use:

MIT

## Use Case:

Developers and campaign managers use this skill to direct an agent to configure and monitor Tokei launch, waitlist, and giveaway campaigns, including deliberate updates to public pages and webhooks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A write-capable key permits public campaign changes and webhook management without enforced human approval.

Mitigation: Require explicit human approval before publishing or unpublishing pages, creating entries, uploading media, or creating or deleting webhooks.

Risk: Broad API access and an unpinned npm dependency increase the impact of a compromised account or package.

Mitigation: Trust the package and account context, use a read-only API key for monitoring, and pin the npm version in MCP configurations.

## Reference(s):

- [Tokei agent documentation](https://tokei.io/agent)
- [Tokei API reference](https://tokei.io/docs/api)
- [tokei-agent release on ClawHub](https://clawhub.ai/gilesdawe/skills/tokei-agent)
- [tokei-agent npm package](https://www.npmjs.com/package/tokei-agent)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Configuration instructions]

**Output Format:** [Markdown guidance with CLI examples; CLI results are JSON when piped or used by agents]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Tokei API key; write operations require a read+write key.]

## Skill Version(s):

0.3.7 (source: server release, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
