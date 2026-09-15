## Description:

Logo 设计 Logo Design helps agents create, upgrade, or evaluate logos and brand marks through brand-gene analysis, strategy, concept refinement, multi-context delivery, and evaluation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and brand teams use this skill to start or continue dLazy logo-design projects, attach reference files, and receive logo or visual-identity guidance and deliverables from the hosted dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected attachments are sent to dLazy hosted endpoints for processing.

Mitigation: Use the skill only for data appropriate for dLazy's hosted service, and attach only files intentionally selected with --files.

Risk: The dLazy API key is stored in local CLI configuration or supplied through an environment variable.

Mitigation: Protect the local config and environment, and rotate or revoke the organization API key when needed.

Risk: A global npm install persists the dLazy CLI on the local system.

Mitigation: Use npx or an isolated environment when a non-persistent CLI invocation is preferred.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-logo-design)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Files, Guidance]

**Output Format:** [Markdown guidance with CLI command examples and hosted-service logo or preview deliverables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the dLazy CLI and may return project-scoped, multi-turn design results.]

## Skill Version(s):

1.3.14 (source: server release metadata; artifact frontmatter says 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
