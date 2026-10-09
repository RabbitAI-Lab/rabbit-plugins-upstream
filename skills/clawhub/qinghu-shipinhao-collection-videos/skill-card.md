## Description:

Retrieves videos from a WeChat Channels collection by topic ID, with cursor-based pagination through Qinghu's qhkit tool.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Users and analysts retrieve and review the video list for a specified WeChat Channels collection, including additional pages when available.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing qhkit adds an npm dependency to the environment.

Mitigation: Use a reviewed or pinned qhkit version in managed environments.

Risk: Qinghu API access requires a token and paid queries may consume credits.

Mitigation: Configure the token securely, estimate charges, and obtain user approval before paid calls.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-shipinhao-collection-videos)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Text, Files, Shell commands]

**Output Format:** [Markdown summary with optional tabular export file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes key previews and reports Qinghu credits spent on paid calls.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
