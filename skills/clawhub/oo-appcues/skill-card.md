## Description:

Appcues helps agents retrieve and manage Appcues flows and content tags through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve Appcues Flow 2.0 experiences and content tags, and to publish or unpublish flows through an OOMOL-connected Appcues account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary reports unsafe pipe-to-shell installer commands.

Mitigation: Review and independently verify installer commands before running first-time setup.

Risk: The security summary reports that unpublish_flow is not clearly classified as requiring confirmation.

Mitigation: Treat unpublish_flow as a state-changing action and confirm the exact Appcues flow and account before execution.

## Reference(s):

- [Appcues homepage](https://www.appcues.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-appcues)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live action schemas before constructing Appcues connector payloads.]

## Skill Version(s):

1.0.2 (source: frontmatter and server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
