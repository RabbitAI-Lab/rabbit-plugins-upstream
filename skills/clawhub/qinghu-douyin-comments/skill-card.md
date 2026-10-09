## Description:

Collects comments from a Douyin video link through the Qinghu data service, with results retrieved in pages of 10 comments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and analysts collect comments on a specified Douyin video to review audience feedback and summarize discussion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid Qinghu calls can incur variable charges when collecting multiple pages of comments.

Mitigation: Check the current estimate and obtain explicit user approval before paid calls or bulk collection.

Risk: Setup may install or update Node and qhkit tooling on the user's machine.

Mitigation: Approve setup steps explicitly and prefer an isolated environment.

Risk: Service access requires a qhkit API token on the user's machine.

Mitigation: Approve credential configuration explicitly and keep the token out of shared output.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-douyin-comments)
- [Qinghu qhkit package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise summary and comment previews; tabular file for larger results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports charged Qinghu credits after paid calls; up to 10 comments per page.]

## Skill Version(s):

0.1.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
