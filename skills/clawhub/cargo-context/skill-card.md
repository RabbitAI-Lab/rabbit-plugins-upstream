## Description:

Read and write a workspace GTM knowledge base, including markdown context files, the Cargo runtime sandbox, and the derived knowledge graph.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

GTM, RevOps, and sales teams use this skill to let agents inspect, author, and maintain a Cargo workspace's context repository for ICPs, personas, plays, proof points, objections, competitors, and signals. Developers and operators also use it to query the typed knowledge graph and troubleshoot context repository workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Runtime write and edit commands can push changes directly to the workspace context repository.

Mitigation: Confirm the active Cargo workspace with cargo-ai whoami before writes, read back the workspace name, and review each proposed change before committing important GTM knowledge.

Risk: The advertised install uses @cargo-ai/cli@latest, which can change without review.

Mitigation: Prefer a pinned Cargo CLI version for production or repeatable workflows, and update only after reviewing release changes.

Risk: Runtime execute exposes a broad shell command surface inside the context sandbox.

Mitigation: Use execute for inspection and verification only, keep commands narrow and reviewable, and treat it as a high-trust operation.

## Reference(s):

- [Cargo Skills Repository](https://github.com/getcargohq/cargo-skills)
- [Cargo Workspace Context Example](https://github.com/getcargohq/cargo-workspaces)
- [ClawHub Skill Page](https://clawhub.ai/cargo-ai/skills/cargo-context)
- [Context repo conventions](references/conventions.md)
- [Response shapes](references/response-shapes.md)
- [Troubleshooting](references/troubleshooting.md)
- [Authoring examples](references/examples/authoring.md)
- [Bootstrap workspace context from a domain](references/examples/bootstrap-from-domain.md)
- [Knowledge-graph queries](references/examples/graph-queries.md)
- [Context repo lifecycle](references/examples/lifecycle.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON command shapes, and markdown file templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce persistent workspace context writes through Cargo CLI commands when the user authorizes or requests them.]

## Skill Version(s):

1.3.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
