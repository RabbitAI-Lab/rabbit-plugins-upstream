## Description:

Deploy a self-hosted funnel builder, take a funnel from empty install to published - landing page, checkout, one-click upsell, thank-you - and drive it from an agent over MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autonnel](https://clawhub.ai/user/autonnel)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to self-host Autonnel funnels and guide an agent through deployment, configuration, publishing, and MCP-based funnel operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A write-enabled MCP API key can change production funnel content and tenant data.

Mitigation: Use read-only keys unless edits are required, create one key per agent, and revoke keys instead of sharing them.

Risk: Secrets, payment credentials, and tenant keys can be exposed or mishandled during deployment.

Mitigation: Keep secrets out of configuration files, use platform secret stores, and verify credential handling before exposing the service publicly.

Risk: Draft or page-reuse behavior can publish incorrect funnel steps or broken pages.

Mitigation: Verify drafts before publishing and confirm page-reuse, thank-you page, and error-page behavior against the current Autonnel version.

## Reference(s):

- [Self-Hosted Funnel Launch on ClawHub](https://clawhub.ai/autonnel/skills/self-hosted-funnel-launch)
- [Autonnel documentation](https://autonnel.com/docs)
- [Autonnel repository](https://github.com/autonnel/autonnel)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with inline JSON, YAML, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes operational checklists and MCP usage rules for deployment and funnel operations.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
