## Description:

This skill helps create, upgrade, and evaluate logos and brand marks, producing transparent-background logos with multi-context previews.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, designers, and brand teams use this skill to run a dLazy-hosted logo design assistant for brand identity concepts, refinement, evaluation, and delivery previews.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow sends prompts and attached files to dLazy hosted services.

Mitigation: Attach only files that are acceptable to upload to dLazy storage and review service terms before use.

Risk: Using a global CLI install can persist a local binary and API key configuration.

Mitigation: Use the pinned on-demand command `npx @dlazy/cli@1.2.3` when less local persistence is preferred, and rotate or revoke API keys from the dLazy dashboard when needed.

Risk: The skill depends on a pinned third-party CLI and hosted service for the design workflow.

Mitigation: Review the pinned dLazy CLI before installing and keep use aligned with the security guidance in the release evidence.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-logo-design)
- [dLazy CLI repository](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, files, guidance]

**Output Format:** [Markdown and plain-text chat responses with CLI commands and generated logo or preview files from the dLazy service]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project-scoped multi-turn output; attached local files may be uploaded to dLazy storage before use.]

## Skill Version(s):

1.3.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
