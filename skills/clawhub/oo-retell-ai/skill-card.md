## Description:

Retell AI (retellai.com). Use this skill for searching and reading Retell AI data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Retell AI calls, phone numbers, voices, and voice agents through the OOMOL oo CLI without calling the Retell AI API directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: OOMOL acts as an intermediary for Retell AI data.

Mitigation: Use the skill only when OOMOL-mediated access is acceptable for the workspace data and account scopes involved.

Risk: First-time setup includes remote installer commands for the oo CLI.

Mitigation: Install the oo CLI through a verified, user-controlled process before allowing an agent to run Retell AI actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-retell-ai)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Retell AI Homepage](https://www.retellai.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Action responses are returned as JSON data with execution metadata when run through the oo CLI.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
