## Description: <br>
WorkBuddy Gift Claimer helps users plan, automate, verify, and learn daily reward, check-in, and credit claiming flows for WorkBuddy and other supported Windows scenarios. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users on Windows use this skill to automate daily WorkBuddy credit and reward claiming, check for missed claims, learn new check-in scenes from screenshots or videos, and manage optional scheduled claiming tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can automate Windows desktop clicks through apps, which may trigger unintended reward-claiming actions if invoked accidentally. <br>
Mitigation: Install only in sessions where this automation is expected, review prompts before execution, and avoid broad triggers in contexts where accidental claiming would be disruptive. <br>
Risk: The skill can store local claim history and learning data for scenes and rewards. <br>
Mitigation: Use a local data directory appropriate for the account, periodically review stored state, and remove learned scenes or history that should no longer be retained. <br>
Risk: The skill can download an OCR model and set up scheduled tasks for recurring automation. <br>
Mitigation: Confirm network and scheduled-task setup during installation, review task timing and startup behavior, and disable scheduled tasks when automatic claiming is no longer desired. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/workbuddy-gift-claimer) <br>
- [Flow Immersion related skill](https://skillhub.cn/skills/user_11064e10/flow-immersion) <br>
- [WorkBuddy Tuner related skill](https://skillhub.cn/skills/user_11064e10/workbuddy-tuner) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and structured status text with task, claim, scene, and learning summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include claim status, rewards, failure reasons, learned keywords, generated scene configuration summaries, scheduled-task status, and next-step guidance.] <br>

## Skill Version(s): <br>
2.3.2 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
