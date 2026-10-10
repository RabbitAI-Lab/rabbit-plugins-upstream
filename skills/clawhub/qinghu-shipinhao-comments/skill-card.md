## Description:

Queries comments on a WeChat Channels video, with pagination and access to replies.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and analysts retrieve comments and replies for a specified WeChat Channels video to review audience feedback.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install external software or change persistent environment settings.

Mitigation: Preinstall a pinned qhkit version through a controlled process; require approval before environment changes and avoid shell startup-file edits.

Risk: Using the Qinghu service requires an API token and may incur paid credits.

Mitigation: Protect the token and obtain user confirmation of estimated charges before paid calls.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/qinghu-shipinhao-comments)
- [Qinghu qhkit package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise written summary with optional tabular export]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports the credits charged for paid queries; larger result sets may be delivered as a file.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
