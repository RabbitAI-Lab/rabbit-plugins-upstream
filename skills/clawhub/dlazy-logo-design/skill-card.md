## Description:

Logo 设计 Logo Design helps agents create, upgrade, and evaluate logos and brand marks through dLazy's hosted logo-design assistant, including brand analysis, concepts, refinement, multi-context preview, and transparent-background logo delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and brand teams use this skill to route logo creation, refresh, and evaluation tasks to dLazy's hosted logo-design template. It supports project-scoped follow-up work and optional reference-file attachments for logo and visual-identity workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and explicitly attached files are sent to dLazy's hosted service and file-storage endpoint.

Mitigation: Confirm brand material and reference files are approved for third-party processing before invoking the skill.

Risk: The dLazy API key is stored in local CLI configuration or supplied through an environment variable.

Mitigation: Protect the local user account, avoid sharing shell environments that expose the key, and rotate or revoke the key from the dLazy dashboard when access changes.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-logo-design)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, files, guidance]

**Output Format:** [Markdown and streamed CLI text with optional file references and generated logo assets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx, a dLazy API key, and network access to dLazy API and file-storage endpoints.]

## Skill Version(s):

1.3.17 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
