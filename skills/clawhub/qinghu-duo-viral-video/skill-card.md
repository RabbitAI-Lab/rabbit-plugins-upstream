## Description:

青虎AI 双人爆款视频模仿 helps an agent use the qhkit workflow to generate a two-person imitation video from a two-person reference video and optional person image, with guidance for estimating cost, submitting jobs, polling status, and delivering generated media.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and agent users use this skill to produce two-person product or social video imitations, such as parent-child, partner, or livestream-commerce scenes. The skill is intended for workflows where two people are visible in the reference video and their actions and expressions need to be synchronized in the generated output.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary flags local npm/Node setup changes and reliance on the Qinghu qhkit tool.

Mitigation: Install only when the user trusts qhkit, keep setup changes visible, and verify qhkit authentication before running workflow actions.

Risk: The skill can trigger paid qhkit generation jobs that consume Qinghu credits.

Mitigation: Run estimate first, report the expected charge, and require explicit user approval before any generate command.

Risk: The security guidance warns against sharing API keys in chat.

Mitigation: Have users configure QHKIT_TOKEN or qhkit credentials outside the agent session and only verify that authentication works.

Risk: The artifact behavior involves creating imitation videos from reference media, which can raise content authorization concerns.

Mitigation: Use only owned or authorized source materials, and require appropriate consent for likenesses, especially when minors are depicted.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-duo-viral-video)
- [Qinghu qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [AutoAGC publisher profile](https://clawhub.ai/user/autoagc)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, markdown, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON workflow parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The agent may return generated media URLs after qhkit status polling completes.]

## Skill Version(s):

0.1.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
