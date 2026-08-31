## Description:

SurveyMethods helps an agent read SurveyMethods account and survey data and, with confirmation, create email lists or add contacts through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Users with an OOMOL-connected SurveyMethods account use this skill to inspect surveys, email lists, contacts, and account details, and to make reviewed email-list changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write actions can change SurveyMethods email lists or contacts.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions.

Risk: Unnecessary setup commands could install software, start login flows, or open account-connection steps when the account is already ready.

Mitigation: Run CLI install, login, or SurveyMethods connection setup only after a command fails with the matching setup or authentication error.

Risk: Actions operate against the user's OOMOL-connected SurveyMethods account.

Mitigation: Install this skill only when the agent should use that connected account, and review requested contact or email-list changes before approval.

## Reference(s):

- [ClawHub SurveyMethods skill page](https://clawhub.ai/oomol/skills/oo-surveymethods)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [SurveyMethods homepage](https://surveymethods.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON payload expectations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May execute oo CLI connector actions that return JSON data from SurveyMethods when authorized.]

## Skill Version(s):

1.0.0 (source: server evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
