## Description:

Karakeep (karakeep.app) enables an agent to read, create, update, and delete Karakeep data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate a connected Karakeep account from an agent, including bookmark workflows, tags, lists, highlights, feeds, backups, assets, and admin-only maintenance actions when the connected account has permission.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes direct execution of remote installer scripts for the oo CLI.

Mitigation: Install only after trusting OOMOL and manually reviewing the installer or using a verified oo CLI installation method.

Risk: Write, destructive, admin, backup download, asset upload, and signed URL actions can change or expose Karakeep data.

Mitigation: Require clear user confirmation of the target, payload, and expected effect before running those actions.

## Reference(s):

- [Karakeep homepage](https://karakeep.app)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub Karakeep skill page](https://clawhub.ai/oomol/skills/oo-karakeep)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects with data and meta.executionId; large downloads are returned as temporary connector file URLs.]

## Skill Version(s):

1.0.0 (source: evidence release version and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
