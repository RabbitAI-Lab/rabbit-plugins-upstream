## Description:

Tuskr helps agents operate Tuskr through an OOMOL-connected account to read, create, and update project, test case, test run, and result data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and QA teams use this skill to let an agent operate Tuskr through OOMOL for project, test case, test run, and bulk result workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include curl and PowerShell pipe-to-shell installer commands that can run remote scripts on a user's machine.

Mitigation: Review the setup path before installing, prefer safer official installation options where possible, and avoid running remote installer commands blindly.

Risk: Tuskr write actions can change project, test case, test run, or result data.

Mitigation: Confirm the exact payload and intended effect with the user before allowing write actions to run.

## Reference(s):

- [ClawHub Tuskr skill page](https://clawhub.ai/oomol/skills/oo-tuskr)
- [Tuskr homepage](https://tuskr.app)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live oo connector schemas before constructing JSON payloads.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
