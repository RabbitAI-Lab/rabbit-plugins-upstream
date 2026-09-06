## Description:

This skill guides agents in using the local `baijimu` CLI to authenticate, inspect, and operate Baijimu platform workspaces, projects, bundles, modules, hosted services, runtime services, agents, platform apps, and local connectors.

This skill is ready for commercial/non-commercial use.

## Publisher:

[momoplan](https://clawhub.ai/user/momoplan)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and agent platforms use this skill to safely discover Baijimu CLI commands, consult official Baijimu documentation, resolve exact resource targets, and carry out platform operations with verification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can help an agent make authenticated Baijimu platform changes, including create, update, deploy, delete, cost-incurring, or externally visible actions.

Mitigation: Use only accounts and workspaces authorized for those changes, resolve exact targets before writes, and require explicit user authorization for destructive, cost-incurring, rollback, reset, release, remote overwrite, or external-message actions.

Risk: Incorrect or ambiguous resource selection could affect the wrong workspace, project, bundle, module, hosted service, runtime service, agent, platform app, or connector.

Mitigation: Read current state first, use CLI resource resolution or exact queries to convert names to stable IDs, and stop when a query returns zero or multiple matches.

Risk: Credentials, tokens, or authentication responses could be exposed during troubleshooting or platform operations.

Mitigation: Do not edit authentication files directly or output PATs, model keys, service tokens, cookies, complete authentication responses, or Capability Tokens; store Capability Tokens only in the target Hosted Service Environment Secret.

## Reference(s):

- [Baijimu documentation](https://docs.baijimu.com/)
- [Baijimu LLM documentation index](https://docs.baijimu.com/llms.txt)
- [Baijimu documentation manifest](https://docs.baijimu.com/docs-manifest.json)
- [Hosted Service Capability documentation](https://docs.baijimu.com/development/bundle-development/hosted-service-capability.md)
- [Skill homepage](https://github.com/momoplan/baijimu-platform-skill)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and CLI-derived findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include exact resource identifiers, status summaries, and verification results when produced by authoritative Baijimu CLI or documentation sources.]

## Skill Version(s):

2.0.1 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
