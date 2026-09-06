## Description:

Creates, upgrades, and evaluates logo and brand identity concepts through a dLazy hosted logo-design agent, including brand-gene analysis, strategy, refinement, multi-context previews, and transparent-background logo delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, designers, brand teams, and developers use this skill to start or continue logo-design projects through the dLazy CLI, optionally attaching reference files for hosted processing and iterative feedback.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, options, and attached files are sent to dLazy hosted services.

Mitigation: Avoid sending private or regulated content unless dLazy processing is approved for the use case.

Risk: A dLazy API key may be saved in the local CLI configuration.

Mitigation: Use OS account protections, rotate or revoke keys when needed, or provide the key per invocation with DLAZY_API_KEY when persistence is not desired.

Risk: Installing a third-party CLI globally adds an executable dependency to the user's environment.

Mitigation: Use the pinned npx invocation for on-demand use, or review the published package and source before global installation.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-logo-design)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and service-generated design guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference project-scoped dLazy sessions and uploaded file URLs when users attach local assets.]

## Skill Version(s):

1.3.11 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
