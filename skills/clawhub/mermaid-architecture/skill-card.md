## Description:

Generates, documents, and updates Mermaid architecture diagrams, flowcharts, sequence diagrams, ER diagrams, class diagrams, and state diagrams under docs/architecture/.

This skill is ready for commercial/non-commercial use.

## Publisher:

[afonsoft](https://clawhub.ai/user/afonsoft)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to create and maintain readable Mermaid diagrams and architecture design documents for application, service, workflow, deployment, and data-model documentation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Image rendering can automatically use npx -y @mermaid-js/mermaid-cli when mmdc is unavailable, which may download and execute an unpinned npm package.

Mitigation: Install and pin a trusted Mermaid CLI in advance, prefer the global mmdc path, and run rendering in a workspace without broad credentials or secrets.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/afonsoft/skills/mermaid-architecture)
- [Publisher profile](https://clawhub.ai/user/afonsoft)
- [Metadata URL](https://github.com/afonsoft/skills)
- [Metadata homepage](https://github.com/SpillwaveSolutions/design-doc-mermaid)
- [Metadata sources](https://github.com/SpillwaveSolutions/design-doc-mermaid)
- [Mermaid Diagram Guide](references/mermaid-diagram-guide.md)
- [Architecture Diagrams Guide](references/guides/diagrams/architecture-diagrams.md)
- [Sequence Diagrams Guide](references/guides/diagrams/sequence-diagrams.md)
- [Activity Diagrams Guide](references/guides/diagrams/activity-diagrams.md)
- [Deployment Diagrams Guide](references/guides/diagrams/deployment-diagrams.md)
- [Unicode Symbols Guide](references/guides/unicode-symbols/guide.md)
- [Troubleshooting Guide](references/guides/troubleshooting.md)
- [Resilient Workflow Guide](references/guides/resilient-workflow.md)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with Mermaid code blocks and optional shell commands for validation or image export]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can produce Mermaid source files, embedded Markdown diagrams, design-document templates, and optional PNG/SVG exports when Mermaid CLI is available.]

## Skill Version(s):

1.0.0 (source: server evidence release.version and artifact metadata.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
