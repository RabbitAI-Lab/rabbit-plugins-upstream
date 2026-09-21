## Description:

This skill helps agents create, upgrade, and evaluate logos and brand identity concepts, including brand analysis, refinement, transparent-background logo output, and multi-context previews.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to start or continue dLazy logo-design projects, attach reference files, and receive brand-mark concepts, evaluation, and delivery guidance through the dLazy CLI and hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached files are sent to dLazy hosted services.

Mitigation: Use only inputs approved for the dLazy service and avoid attaching sensitive files unless the service terms and data handling are acceptable.

Risk: The dLazy API key may be stored in local CLI configuration or supplied through an environment variable.

Mitigation: Restrict local config access and rotate or revoke the key from the dLazy dashboard when needed.

Risk: A global npm install persists the third-party CLI on the user's machine.

Mitigation: Use the pinned npx invocation for on-demand execution or review the external CLI package before installing it globally.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-logo-design)
- [Publisher Profile](https://clawhub.ai/user/dlazyai)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Files]

**Output Format:** [Markdown guidance with CLI commands and generated logo assets from the hosted dLazy service]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx and a dLazy API key; attached local files are uploaded to dLazy media storage when used.]

## Skill Version(s):

1.3.16 (source: server release metadata; artifact frontmatter reports 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
