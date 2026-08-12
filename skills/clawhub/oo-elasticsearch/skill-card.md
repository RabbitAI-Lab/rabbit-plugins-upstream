## Description:

Operate Elasticsearch through OOMOL's oo CLI for read, write, search, index, and cluster-management workflows without handling raw credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect and manage Elasticsearch clusters, indices, documents, mappings, aliases, shards, and reindexing workflows through an OOMOL-connected account. It supports read workflows as well as confirmed write and destructive actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Approved write and destructive actions can change or remove Elasticsearch data.

Mitigation: Review the exact payload and target before approving write or delete actions, and scope the connected Elasticsearch account to only the data the agent should access.

Risk: Setup commands such as CLI installation and login can affect the local environment if run unnecessarily.

Mitigation: Treat CLI install and login as one-time setup steps, and run them only after an auth, connection, or missing-CLI failure.

## Reference(s):

- [Elasticsearch homepage](https://www.elastic.co/elasticsearch)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-elasticsearch)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the live connector schema before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
