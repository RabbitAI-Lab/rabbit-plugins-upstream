## Description:

将以 sph 开头的视频号 ID 转换为后续接口所需的 finder username。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

视频号运营人员和开发者可将公开视频号短 ID 转换为后续接口所需的 finder username。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or update external qhkit and Node tooling.

Mitigation: Review installations first and prefer a preinstalled, pinned qhkit version.

Risk: A Qinghu API token may be exposed in logged commands.

Mitigation: Avoid entering tokens directly in command lines that are logged.

Risk: Lookup calls consume paid Qinghu credits, and failed calls may also incur charges.

Mitigation: Check the tool and expected credit use, then approve each paid lookup before calling it.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-shipinhao-id-convert)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Plain text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports the converted finder username and credits charged, if any.]

## Skill Version(s):

0.1.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
