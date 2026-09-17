## Description:

This skill lets an agent operate Geckoboard through an OOMOL-connected account to inspect connector schemas and append, replace, find or create, and delete dataset data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage Geckoboard dataset workflows through the OOMOL connector, including schema inspection, appending or replacing records, finding or creating datasets, and deleting datasets with explicit confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include direct execution of remote installer scripts without verification.

Mitigation: Prefer a verified, pinned installer or package manager instead of curl-to-bash or irm-to-iex installation.

Risk: Write and destructive actions can replace or delete Geckoboard dataset data.

Mitigation: Confirm the exact payload, target dataset, and expected effect with the user before running write or delete actions.

Risk: Connector actions route through OOMOL's connected account and service connector.

Mitigation: Use the skill only when the publisher and OOMOL connector are trusted for the target Geckoboard workspace.

## Reference(s):

- [ClawHub Geckoboard skill page](https://clawhub.ai/oomol/skills/oo-geckoboard)
- [Geckoboard homepage](https://www.geckoboard.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill instructs the agent to inspect live connector schemas before running actions and to request confirmation for write or destructive dataset changes.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
