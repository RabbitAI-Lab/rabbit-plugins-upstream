## Description:

Guides agents using the relay-knowledge CLI to index repositories, manage knowledge maps, and retrieve code and business context for development work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[stevetdp](https://clawhub.ai/user/stevetdp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and coding agents use this skill to maintain repository knowledge maps, query indexed code and business relationships, and check context and impact after commits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Indexing may expose sensitive content in selected repositories or paths.

Mitigation: Choose narrow scopes for sensitive repositories and review what is indexed.

Risk: The CLI maintains local runtime state and may optionally install a service.

Mitigation: Review local state requirements and install a service only with explicit user or administrator authorization.

Risk: Installing an unverified binary or package can introduce untrusted code.

Mitigation: Verify the published binary or Cargo package source before installation.

Risk: Feedback auto-submit may publish information without per-report approval.

Mitigation: Enable auto-submit only with explicit user or administrator authorization.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/stevetdp/skills/relay-knowledge-cli)
- [Project homepage listed in skill metadata](https://github.com/coolplayagent/relay-knowledge)
- [CLI workflows](artifact/references/cli-workflows.md)
- [Knowledge map workflows](artifact/references/knowledge-map-workflows.md)
- [Feedback workflows](artifact/references/feedback-workflows.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with CLI command examples and JSON/YAML configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the selected repository scope and index freshness.]

## Skill Version(s):

1.1.20 (source: ClawHub release and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
