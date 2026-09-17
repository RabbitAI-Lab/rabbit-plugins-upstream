## Description:

Lob (lob.com) supports Lob address verification, standardization, and US address autocomplete through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Lob address verification and US address autocomplete through an OOMOL-connected Lob account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands for the oo CLI.

Mitigation: Install the oo CLI through a trusted, versioned, verifiable process instead of allowing an agent to run remote installer commands automatically.

Risk: Address verification sends user-provided address data to the connected Lob/OOMOL service.

Mitigation: Use only data that is appropriate to share with the connected service and confirm account, connection, and billing state before running verification actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-lob)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Lob Homepage](https://www.lob.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before execution and returns Lob connector results as JSON when actions are run.]

## Skill Version(s):

1.0.4 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
