## Description:

Resolve Doc Bridge boundaries before changing code.

This skill is ready for commercial/non-commercial use.

## Publisher:

[emersonbraun](https://clawhub.ai/user/emersonbraun)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and coding agents use this skill before editing repositories with Doc Bridge configuration to resolve read-before-editing files, edit boundaries, and required checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fallback path may download and run the pinned Doc Bridge CLI through npx.

Mitigation: Use the skill only in repositories whose Doc Bridge configuration and package-resolution behavior are trusted.

Risk: The resolved handoff can instruct the agent to run project-defined check commands.

Mitigation: Review resolved checks before execution and run them only in the intended repository context.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/emersonbraun/skills/doc-bridge-handoff)
- [Synthetic Doc Bridge package guidance fixture](fixtures/synthetic-repo/docs/for-agents/packages/payments.md)
- [Synthetic Doc Bridge configuration fixture](fixtures/synthetic-repo/doc-bridge.config.json)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown guidance with optional JSON handoff output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Fails closed when the resolver returns incomplete, unsafe, or mismatched handoff data.]

## Skill Version(s):

1.0.0 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
