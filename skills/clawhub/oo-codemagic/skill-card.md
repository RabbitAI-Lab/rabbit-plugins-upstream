## Description:

Helps agents operate Codemagic through an OOMOL-connected account by inspecting live connector schemas and running Codemagic actions with the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and DevOps engineers use this skill to inspect Codemagic users, teams, apps, and builds, and to start or cancel builds after confirming write actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that can execute changing code on the user's machine.

Mitigation: Review installer steps before use and prefer a trusted, versioned package or verified download for the oo CLI.

Risk: Build creation and cancellation actions change Codemagic state.

Mitigation: Confirm the exact payload, target build or workflow, and expected effect with the user before running write actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-codemagic)
- [Codemagic homepage](https://codemagic.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Codemagic actions may return JSON from the oo CLI; write actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
