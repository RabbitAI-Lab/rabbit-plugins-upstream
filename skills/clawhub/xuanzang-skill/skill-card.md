## Description:

xuanzang-skill activates a Chinese-language motivational coaching and governance mode for agents when users request it or when an agent shows repeated failure, passivity, unverified completion claims, or similar low-confidence behavior.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ebandao777-oss](https://clawhub.ai/user/ebandao777-oss)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agent users can use this skill to add a persona-driven coaching layer that pushes agents toward verification, task closure, and structured escalation after repeated failures. It also includes local governance protocols for role routing, sub-agent coordination, persistent progress state, shell-based verification, and teardown workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence rates the release as suspicious because it presents as motivational coaching while also directing broad local governance and orchestration behavior.

Mitigation: Install only when that broader local governance and orchestration behavior is intended, and review the skill behavior before enabling it in an agent runtime.

Risk: The security evidence calls out persistence under ~/.xuanzang.

Mitigation: Review what local state will be stored, use an isolated environment where appropriate, and remove or constrain persistence if it is not needed.

Risk: The security evidence calls out shell-based verification, contract verify_commands, and teardown actions.

Mitigation: Require explicit human review before allowing generated verification commands, contract commands, or teardown actions to run.

Risk: The security evidence calls out automatic hooks and sub-agent orchestration as under-disclosed for a motivational style mode.

Mitigation: Disable or constrain automatic hooks and sub-agent orchestration unless the operator has reviewed and accepted those workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ebandao777-oss/skills/xuanzang-skill)
- [Server-resolved GitHub import](https://github.com/ebandao777-oss/xuanzang-skill)
- [README](README.md)
- [Methodology router](references/methodology-router.md)
- [Display protocol](references/display-protocol.md)
- [Flavors](references/flavors.md)
- [Harness governance](references/harness-governance.md)
- [De-escalation protocol](references/de-escalation-protocol.md)
- [Evolution protocol](references/evolution-protocol.md)
- [Platform local instruction system](references/platform.md)
- [Teardown protocol](references/teardown-protocol.md)
- [Agent team integration](references/agent-team.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown-style agent responses with inline commands, configuration snippets, task contracts, status panels, and guidance text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update local ~/.xuanzang state files and may propose verification or teardown commands when its governance workflows are used.]

## Skill Version(s):

1.0.2 (source: ClawHub release evidence; artifact frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
