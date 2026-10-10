## Description:

Retrieves a Xiaohongshu creator's published notes from their profile link for account and content analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Social media analysts and content teams use the skill to retrieve a Xiaohongshu creator's note list and review competing accounts' content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill directs installation and configuration of external software on the user's machine.

Mitigation: Install only if the qhkit package is trusted; prefer a pinned or preinstalled version in an isolated environment and obtain approval before changing the environment.

Risk: Queries can incur paid Qinghu API charges, which may vary with the number of results.

Mitigation: Check the estimate, explain the likely charges, and obtain consent before making paid calls.

Risk: Using the service requires configuring an API token.

Mitigation: Use approved token configuration and avoid exposing the token in shared output.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/qinghu-rednote-creator-notes)
- [qhkit package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise Markdown summary; tabular file for larger result sets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include a short preview and the Qinghu credits charged.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
