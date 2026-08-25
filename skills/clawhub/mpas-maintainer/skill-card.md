## Description:

Allows authorized maintainers to review and approve MCP tool calls proposed through MPAS, helping prevent destructive or compliance-sensitive actions from executing without approval.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oma3](https://clawhub.ai/user/oma3)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and governance teams use this skill to configure an MPAS Maintainer agent that reviews pending actions, checks policy and context, and approves or rejects only the exact action under review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A maintainer approval can authorize immediate real-world changes, including destructive operations.

Mitigation: Require maintainers to review the exact action, hash, proposer, target resources, arguments, conditions, and expiration before approving.

Risk: Combining proposer and maintainer roles can weaken independent approval.

Mitigation: Install this skill only on a dedicated MPAS Maintainer agent and keep it separate from agents that propose governed actions.

Risk: Misconfigured signer or approval tooling can grant authority to the wrong actor.

Mitigation: Review signer configuration carefully and treat the configured signer or authorization step as the authoritative decision-maker.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oma3/skills/mpas-maintainer)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with approval-review procedures and configuration-oriented instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces maintainer guidance for reviewing MPAS actions and using configured signer or approval tools.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
