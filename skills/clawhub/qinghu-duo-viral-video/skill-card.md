## Description:

青虎AI 双人爆款视频模仿：上传一条双人参考视频和人物图，精准同步两个人物的动作与神态并优化画面画质，产出双人带货视频，适配童装、直播带货等多种创作场景。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and commerce teams use this skill to generate two-person product or social videos from an authorized reference video and optional character image. It is suited to double-host livestream commerce, parent-child, partner, and other two-person synchronized video scenes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may install and run an unpinned third-party CLI.

Mitigation: Use a pinned, reviewed qhkit version in a contained environment before running generation commands.

Risk: The workflow can use Qinghu service credentials and submit paid generation jobs.

Mitigation: Provide the token only when needed and confirm the returned credit estimate before generation.

Risk: Selected local images or videos are uploaded to an external Qinghu service.

Mitigation: Use only authorized media and confirm that external upload is acceptable for the content.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/qinghu-duo-viral-video)
- [Publisher profile](https://clawhub.ai/user/autoagc)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, markdown]

**Output Format:** [Markdown guidance with inline JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides an agent through qhkit workflow option lookup, estimate, generation, polling, and delivery of generated video URLs.]

## Skill Version(s):

0.1.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
