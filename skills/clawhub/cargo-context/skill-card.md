## Description:

Helps agents read and maintain a workspace's git-backed go-to-market knowledge base and inspect its knowledge graph.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales, marketing, and operations teams use this skill to document and retrieve workspace knowledge such as customer profiles, personas, positioning, plays, and objections. Agents can also inspect cross-references in the knowledge graph.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated context edits and commands can push persistent changes to the default branch.

Mitigation: Confirm the workspace before writing; keep command execution read-only unless a maintenance change is explicitly reviewed.

Risk: The required CLI has authenticated access to the workspace context repository.

Mitigation: Install only when that access is appropriate and pin the CLI version.

Risk: Enrichment or scraping workflows may contact third-party services.

Mitigation: Get consent before running workflows that contact external services.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/cargo-ai/skills/cargo-context)
- [Cargo skills homepage (publisher metadata)](https://github.com/getcargohq/cargo-skills)
- [Context repository conventions](references/conventions.md)
- [Command response shapes](references/response-shapes.md)
- [Context authoring examples](references/examples/authoring.md)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Guidance]

**Output Format:** [Markdown guidance and workspace knowledge-base files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Context changes can be committed and pushed to the workspace repository.]

## Skill Version(s):

1.4.0 (source: skill frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
