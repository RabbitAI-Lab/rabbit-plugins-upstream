## Description:

Use Ringover through the OOMOL oo CLI connector to search and read calls, users, groups, IVRs, numbers, tags, and team details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and support or operations teams use this skill to retrieve Ringover telephony records and directory data from a connected OOMOL account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote installer commands for the oo CLI.

Mitigation: Review the installer path before installation, prefer official signed or package-manager installation methods, verify downloads where possible, and do not let an agent run a remote installer automatically.

Risk: The skill accesses Ringover data through a connected account and may expose data according to granted scopes.

Mitigation: Ensure the Ringover connection has only the intended scopes and review returned data before sharing it outside the authorized workflow.

Risk: Future connector actions could change Ringover state if write or destructive actions are added.

Mitigation: Require user confirmation for any state-changing connector action, including the exact target, payload, and expected effect.

## Reference(s):

- [ClawHub Ringover Skill](https://clawhub.ai/oomol/skills/oo-ringover)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Ringover Homepage](https://www.ringover.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector action responses are JSON objects returned by the oo CLI.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
