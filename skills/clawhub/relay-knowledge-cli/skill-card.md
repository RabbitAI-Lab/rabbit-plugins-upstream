## Description:

Guides agents in indexing repositories, maintaining CodeSpec and Knowledge Maps, and querying code and business knowledge with the relay-knowledge CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[stevetdp](https://clawhub.ai/user/stevetdp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to index repositories, maintain knowledge maps and business terminology, answer code and dependency questions, and assess changes after commits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Indexing a repository creates persistent local state and may update knowledge-map files.

Mitigation: Index only intended repositories and review map and glossary changes like normal source changes.

Risk: Feedback auto-submit may publish information to a GitHub target.

Mitigation: Enable auto-submit only with an explicitly approved GitHub target and token.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/stevetdp/skills/relay-knowledge-cli)
- [Project homepage (listed in skill metadata)](https://github.com/coolplayagent/relay-knowledge)
- [CLI workflows](references/cli-workflows.md)
- [Knowledge Map workflows](references/knowledge-map-workflows.md)
- [Feedback workflows](references/feedback-workflows.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Running suggested commands may create local indexes and update knowledge-map files.]

## Skill Version(s):

1.1.19 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
