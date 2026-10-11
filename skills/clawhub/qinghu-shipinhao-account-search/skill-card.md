## Description:

Searches for videos matching a keyword within a specified WeChat Channels account using Qinghu's data service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents search a specified WeChat Channels account for videos by keyword and receive a concise summary or an exported results file.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or update qhkit and Node/npm tooling on the local machine.

Mitigation: Review and pre-install trusted tooling; avoid unpinned installs in sensitive environments.

Risk: Searching requires a Qinghu token and may consume paid credits.

Mitigation: Provide a token only when using the paid service, and confirm the estimated cost before calls.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-shipinhao-account-search)
- [qhkit package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Files]

**Output Format:** [Concise text summary; spreadsheet file for 10 or more results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports credits consumed for paid calls.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
