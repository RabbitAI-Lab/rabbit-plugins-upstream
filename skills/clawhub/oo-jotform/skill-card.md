## Description:

Jotform helps agents read, create, and update Jotform data through OOMOL's oo CLI and a connected Jotform account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Jotform from an agent through an OOMOL-connected account, including listing forms, retrieving forms and submissions, inspecting questions, and creating submissions after confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unverified remote installer commands that could execute arbitrary code if the external installer is compromised.

Mitigation: Review the setup path before installing; prefer a verified, version-pinned, checksum- or signature-checked oo CLI installation method.

Risk: The create_submission action changes Jotform state and can submit incorrect form data if IDs or payload values are wrong.

Mitigation: Fetch the live action schema, confirm form IDs and payloads with the user, and only then run write actions.

## Reference(s):

- [ClawHub Jotform Skill](https://clawhub.ai/oomol/skills/oo-jotform)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Jotform Homepage](https://www.jotform.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the oo CLI Jotform connector; write actions require user confirmation before execution.]

## Skill Version(s):

1.0.3 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
