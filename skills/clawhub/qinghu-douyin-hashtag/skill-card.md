## Description:

Retrieves Douyin hashtag details by topic ID, including playback and participation metrics, through Qinghu AI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Social media analysts and marketers use this skill to look up Douyin hashtag activity and assess topic popularity from playback and participation metrics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install a local Node.js and qhkit toolchain.

Mitigation: Use a preinstalled or pinned qhkit version in managed environments and review installation before proceeding.

Risk: Queries require a Qinghu API token.

Mitigation: Provide the token only through the intended credential configuration and keep it out of shared outputs.

Risk: Hashtag lookups are paid and charges may rise with result size.

Mitigation: Check estimated credits and obtain user approval before paid calls, especially bulk queries.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-douyin-hashtag)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise Markdown response; tabular file for larger result sets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports Qinghu credits consumed after paid calls.]

## Skill Version(s):

0.1.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
