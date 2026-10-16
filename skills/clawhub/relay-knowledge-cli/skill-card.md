## Description:

Guides agents through local CLI workflows for repository knowledge maps, code and business graph queries, and commit-driven indexing and impact analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[stevetdp](https://clawhub.ai/user/stevetdp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this skill to index repositories, navigate versioned knowledge maps, query code and business relationships, and refresh impact and context after commits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Repository indexing and optional service or watcher operation can persist local repository information and run background work.

Mitigation: Confirm repository scope and storage location before indexing; enable a service or watcher only when intended.

Risk: Opt-in feedback publication can expose private source snippets, logs, credentials, or repository details.

Mitigation: Keep sensitive details out of public narratives and enable feedback auto-submit only with explicit authorization.

## Reference(s):

- [Relay Knowledge project homepage (skill metadata)](https://github.com/coolplayagent/relay-knowledge)
- [ClawHub skill release](https://clawhub.ai/stevetdp/skills/relay-knowledge-cli)
- [CLI workflows](references/cli-workflows.md)
- [Knowledge Map workflows](references/knowledge-map-workflows.md)
- [Feedback workflows](references/feedback-workflows.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown guidance with CLI commands and JSON/YAML examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Repository answers should be tied to an indexed, pinned snapshot.]

## Skill Version(s):

1.1.21 (source: server release metadata, skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
