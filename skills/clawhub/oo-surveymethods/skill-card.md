## Description:

Use this skill for SurveyMethods requests that read, create, or update account, survey, email list, and contact data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate SurveyMethods from an agent session, including reading account and survey data, listing email lists and contacts, creating email lists, and adding contacts after user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer commands for the oo CLI could execute mutable code on the user's machine.

Mitigation: Review the installation path, use the official source, verify integrity if available, and install with normal user privileges.

Risk: SurveyMethods write actions can create email lists or add contacts.

Mitigation: Inspect the live action schema and confirm the exact payload and expected effect with the user before running write actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-surveymethods)
- [Publisher Profile](https://clawhub.ai/user/oomol)
- [SurveyMethods Homepage](https://surveymethods.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce live SurveyMethods connector calls through the oo CLI; write actions require payload confirmation.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
