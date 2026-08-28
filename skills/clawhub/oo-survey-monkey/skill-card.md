## Description:

Enables an agent to operate SurveyMonkey through an OOMOL-connected account for reading, creating, and updating survey, collector, contact, and response data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent inspect SurveyMonkey schemas, retrieve account, survey, collector, contact, and response data, and create contacts, contact lists, surveys, and public weblink collectors through an OOMOL-connected SurveyMonkey account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Read actions can expose contacts, survey responses, collectors, and account details from the connected SurveyMonkey workspace.

Mitigation: Install only for intended SurveyMonkey workspaces and review returned data handling before sharing or storing outputs.

Risk: Write actions can create contacts, contact lists, surveys, and public weblink collectors in the connected account.

Mitigation: Confirm the exact payload and expected effect with the user before approving write actions.

Risk: First-time setup or expired connections can block connector actions.

Mitigation: Use the documented setup flow only after an authentication, scope, credential, app, or billing error occurs.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-survey-monkey)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [SurveyMonkey Homepage](https://www.surveymonkey.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live action schema inspection before building connector payloads.]

## Skill Version(s):

1.0.0 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
