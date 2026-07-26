## Description: <br>
MBTI helps an agent diagnose its MBTI-style behavior profile, compare it with user expectations, and generate configuration adjustment suggestions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[torchesfrms](https://clawhub.ai/user/torchesfrms) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use this skill to run a staged personality-style diagnosis, compare measured agent behavior with desired behavior, and review proposed SOUL.md configuration changes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may lead agents to make persistent SOUL.md behavior changes without clear confirmation, rollback, or tight scoping. <br>
Mitigation: Require a diff or preview, make a backup first, and apply changes only after explicit approval. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/torchesfrms/skills/mbti) <br>
- [Publisher profile](https://clawhub.ai/user/torchesfrms) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and shell command output with proposed configuration changes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose SOUL.md changes; review diffs before applying.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
