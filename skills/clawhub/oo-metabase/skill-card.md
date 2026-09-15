## Description:

Metabase helps agents read, create, update, search, and manage Metabase content through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and business users use this skill to inspect schemas and operate Metabase assets such as databases, collections, dashboards, cards, questions, metrics, MBQL queries, and native SQL through the oo CLI. It supports both read workflows and confirmed state-changing Metabase actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup references internet installer scripts for the oo CLI.

Mitigation: Review or verify the oo installer through an official release channel before running it.

Risk: Native SQL and state-changing Metabase actions can expose or modify content according to the connected account's permissions.

Mitigation: Require explicit approval before native SQL execution or any action that changes Metabase content.

## Reference(s):

- [ClawHub Metabase skill page](https://clawhub.ai/oomol/skills/oo-metabase)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Metabase homepage](https://www.metabase.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses may include JSON data and an execution id when actions are run.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
