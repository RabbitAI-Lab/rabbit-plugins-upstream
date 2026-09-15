## Description:

Operate Pipedrive CRM through an OOMOL-connected account, supporting read, create, update, and delete workflows for deals, people, organizations, activities, pipelines, and stages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Sales and operations users can ask an agent to retrieve and manage Pipedrive CRM records through the OOMOL connector. The skill is suited to account, contact, activity, pipeline, and deal workflows where write or delete actions require confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that can execute local code.

Mitigation: Prefer a verified official package or inspect and verify installer contents before running pipe-to-shell commands.

Risk: Create, update, and delete actions can change or remove Pipedrive data.

Mitigation: Require explicit user confirmation of the target, payload, and expected effect before running write or destructive actions.

Risk: Connector credentials are held and injected by OOMOL.

Mitigation: Install only when OOMOL processing Pipedrive requests and managing connector credentials is acceptable for the user's environment.

## Reference(s):

- [Pipedrive Homepage](https://www.pipedrive.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-pipedrive)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution; successful CLI runs return JSON with data and meta.executionId.]

## Skill Version(s):

1.0.3 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
