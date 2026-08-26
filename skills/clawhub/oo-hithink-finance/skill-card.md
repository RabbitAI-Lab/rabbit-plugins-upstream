## Description:

Tonghuashun Financial Data helps an agent search, read, and export Tonghuashun financial datasets through the OOMOL hithink_finance connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to retrieve Tonghuashun A-share market data, company financial statements, public-fund information, index data, and export datasets from an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connector actions send requests through OOMOL and require a connected Tonghuashun Financial Data account.

Mitigation: Install and use the skill only when OOMOL's oo CLI and the Tonghuashun connection are intended for the task.

Risk: Export actions can upload full or recent market datasets to transit storage.

Mitigation: Review the selected export action and payload before execution, especially for large or sensitive datasets.

Risk: Future actions marked write or destructive could change or remove data if added to the connector.

Mitigation: Require explicit user approval for any action tagged write or destructive before running it.

## Reference(s):

- [Tonghuashun Financial Data homepage](https://fuyao.aicubes.cn/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown with inline shell commands and JSON payloads; connector responses may include JSON data or exported Parquet datasets uploaded to transit storage.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The agent should inspect the live connector schema before constructing action payloads.]

## Skill Version(s):

1.0.0 (source: evidence release version and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
