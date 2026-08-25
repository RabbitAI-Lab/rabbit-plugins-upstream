## Description:

KoboToolbox lets an agent read, create, update, export, validate, deploy, and delete KoboToolbox data through the OOMOL `oo` CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, employees, and developers use this skill to operate a connected KoboToolbox account from an agent workflow, including project, asset, submission, validation, and export tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent can read KoboToolbox project and submission data from the connected account.

Mitigation: Limit requests to the needed project, asset, submission, or export and avoid exposing unnecessary returned data.

Risk: Write and destructive actions can create, deploy, validate, export, or delete KoboToolbox data.

Mitigation: Require exact target and payload confirmation before write actions, and explicit approval before deletion.

## Reference(s):

- [KoboToolbox homepage](https://www.kobotoolbox.org)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-kobotoolbox)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands use the live connector schema before running actions.]

## Skill Version(s):

1.0.0 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
