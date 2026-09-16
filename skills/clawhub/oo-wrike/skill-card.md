## Description:

Wrike enables agents to read, create, and update Wrike data through an OOMOL-connected oo CLI account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage Wrike folders, tasks, and contacts through OOMOL's Wrike connector from an agent workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include internet-hosted installer scripts that could execute arbitrary code if run blindly.

Mitigation: Prefer verified or package-manager installation steps when available and review installer sources before execution.

Risk: Write actions can change Wrike folders or tasks.

Mitigation: Confirm the exact action payload and expected effect with the user before running write actions.

Risk: The skill depends on OOMOL as the Wrike connector with server-side credential handling.

Mitigation: Install only when OOMOL-connected Wrike access and the account permissions are acceptable for the deployment.

## Reference(s):

- [ClawHub Wrike skill page](https://clawhub.ai/oomol/skills/oo-wrike)
- [Wrike homepage](https://www.wrike.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions may return JSON from the oo CLI; write actions require user-confirmed payloads.]

## Skill Version(s):

1.0.2 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
