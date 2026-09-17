## Description:

Enables agents to read, create, update, search, and list Atlassian Confluence content through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users can use this skill to operate Confluence from an agent session, including page creation, retrieval, updates, content search, and space listing through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes direct execution of remote installer scripts.

Mitigation: Install the oo CLI through a verified package or reviewed installer before using the skill.

Risk: Confluence activity is routed through OOMOL, which may be sensitive for workspaces containing confidential data.

Mitigation: Review the integration before installation and use a least-privilege Confluence connection.

Risk: Write actions can change Confluence pages.

Mitigation: Confirm the exact payload and expected effect with the user before running create or update actions.

## Reference(s):

- [ClawHub Confluence Skill](https://clawhub.ai/oomol/skills/oo-confluence)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Atlassian Confluence](https://www.atlassian.com/software/confluence)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action payloads; connector responses are JSON objects containing data and meta.executionId.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
