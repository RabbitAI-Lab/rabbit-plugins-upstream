## Description:

詹明明·今天拍什么 is a short-video topic selection skill that helps a creator evaluate ideas with supply-demand checks, benchmark signals, real-data evidence, and topic mix constraints instead of producing one-click topic lists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External creators use this skill to decide what short-video topic to shoot next, diagnose whether an idea is worth making, or turn a broad topic into 3-5 evidence-backed candidate angles. It is intended for a solo knowledge creator who wants topic judgment, audience fit, hook direction, and concrete next steps before scripting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may automatically write conversation feedback into shared framework or memory files.

Mitigation: Review or disable automatic feedback write-back before broad use, and confirm changes before allowing feedback to affect future writing behavior.

Risk: The skill expects access to the user's ZMM vault, source materials, and topic pipeline files.

Mitigation: Install only in workspaces where reading those materials and saving topic decisions is expected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/zmm-topic)
- [Publisher profile: iamzifei](https://clawhub.ai/user/iamzifei)
- [常识缺口法](references/常识缺口法.md)
- [议程与合集](references/议程与合集.md)
- [选题三路](references/选题三路.md)
- [题感引擎](references/题感引擎.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance, files]

**Output Format:** [Markdown with structured candidate assessments, concise recommendations, and occasional shell commands or file-path references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save accepted topic decisions and feedback into the user's ZMM vault or shared framework files when the configured workspace paths are available.]

## Skill Version(s):

0.2.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
