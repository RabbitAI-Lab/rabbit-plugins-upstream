## Description: <br>
Presents adaptive codebase challenge questions with multiple-choice and trace exercises. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and contributors use this skill to test and reinforce knowledge of a codebase through adaptive challenge questions, trace exercises, answer evaluation, scoring, and progress tracking. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads and updates local .gauntlet challenge state and may write a pre-commit pass token after a successful challenge. <br>
Mitigation: Before installing, confirm this local state behavior is expected for the current project and review or scan the skill before deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-gauntlet-challenge) <br>
- [claude-night-market gauntlet homepage](https://github.com/athola/claude-night-market/tree/master/plugins/gauntlet) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown challenge prompts, answer feedback, explanations, scores, and progress updates.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May read and update local .gauntlet challenge state and may write a pre-commit pass token after a successful gated challenge.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
