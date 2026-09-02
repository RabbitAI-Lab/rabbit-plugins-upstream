## Description:

Helps an agent read and write a Cargo workspace's git-backed GTM knowledge base, use its runtime sandbox, and inspect its typed knowledge graph.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

GTM operators, revenue teams, and their agents use this skill to inspect, author, update, and validate workspace context such as ICPs, personas, plays, proof points, objections, competitors, and buying signals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent writes or edits can update the wrong workspace context repository if the active workspace is not confirmed.

Mitigation: Run cargo-ai whoami and confirm the workspace name before using runtime write or runtime edit.

Risk: Generated or edited GTM knowledge may be misleading, stale, or over-weighted from limited sales-call evidence.

Mitigation: Review generated bootstrap content and keep human approval in the loop for call-derived edits before committing them.

Risk: runtime execute can run commands in the workspace sandbox and should not be treated as a place for arbitrary unreviewed commands.

Mitigation: Use runtime execute for inspection, builds, tests, or validation, and review commands before running them.

## Reference(s):

- [ClawHub cargo-context Skill Page](https://clawhub.ai/cargo-ai/skills/cargo-context)
- [Cargo Skills Homepage](https://github.com/getcargohq/cargo-skills)
- [Canonical Context Repository](https://github.com/getcargohq/cargo-workspaces)
- [Context repo conventions](references/conventions.md)
- [Response shapes](references/response-shapes.md)
- [Troubleshooting](references/troubleshooting.md)
- [Authoring examples](references/examples/authoring.md)
- [Bootstrap workspace context from a domain](references/examples/bootstrap-from-domain.md)
- [Knowledge-graph queries](references/examples/graph-queries.md)
- [Context repo lifecycle](references/examples/lifecycle.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON response shapes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce persistent context writes or edits when the Cargo CLI commands are run against an authenticated workspace.]

## Skill Version(s):

1.2.2 (source: SKILL.md frontmatter, skill-metadata.json, and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
