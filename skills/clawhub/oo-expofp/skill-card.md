## Description:

ExpoFP (expofp.com). Use this skill for ANY ExpoFP request -- reading, creating, updating, and deleting data. Whenever a task involves ExpoFP, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate ExpoFP through an OOMOL-connected account, including listing expos and exhibitors, retrieving exhibitor details, and creating, updating, or deleting exhibitors with confirmation for state-changing actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes direct execution of remote installer scripts.

Mitigation: Review the oo CLI installation path first and prefer an official package or manually downloaded, verified installer.

Risk: Write and delete actions can change or remove ExpoFP exhibitor data.

Mitigation: Confirm exact payloads, targets, and expected effects before running write actions, and require explicit approval before destructive actions.

## Reference(s):

- [ExpoFP homepage](https://expofp.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub ExpoFP skill page](https://clawhub.ai/oomol/skills/oo-expofp)

## Skill Output:

**Output Type(s):** [Shell commands, API calls, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
