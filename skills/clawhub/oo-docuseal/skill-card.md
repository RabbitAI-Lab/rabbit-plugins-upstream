## Description:

DocuSeal skill for reading, creating, and updating DocuSeal data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage DocuSeal templates and create signature submissions through the oo CLI after inspecting live connector schemas.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer scripts executed directly in a shell.

Mitigation: Use a signed, version-pinned package where available, or manually download and verify the installer before execution.

Risk: The create_submission action changes DocuSeal state by creating signature requests.

Mitigation: Inspect the live connector schema and confirm the exact payload and intended effect with the user before running write actions.

## Reference(s):

- [ClawHub DocuSeal skill page](https://clawhub.ai/oomol/skills/oo-docuseal)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [DocuSeal homepage](https://www.docuseal.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include connector schema checks, action commands, and confirmation guidance for state-changing DocuSeal actions.]

## Skill Version(s):

1.0.4 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
