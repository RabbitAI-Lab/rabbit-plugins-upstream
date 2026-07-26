## Description: <br>
Run asynchronous decisions by producing a decision memo and a bounded process wrapper with named roles, response windows, comment rules, escalation, kickoff, and closing note. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mohitagw15856](https://clawhub.ai/user/mohitagw15856) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Teams, managers, and operators use this skill to replace stalled decision meetings or open-ended comment threads with a time-bound written decision process. It helps an agent draft the memo, kickoff message, role assignments, comment protocol, and closing note. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated decision records may contain internal strategy, named stakeholders, deadlines, dissent, and reopen conditions. <br>
Mitigation: Store the memo and closing note only in the team's approved decision-log location with appropriate access controls. <br>
Risk: The skill can shape decision process guidance, which may be misleading if the underlying decision facts or roles are incomplete. <br>
Mitigation: Confirm the decider, consulted stakeholders, decision deadline, stakes, and reopen condition before using the generated memo to close a decision. <br>


## Reference(s): <br>
- [Async Decision Memo homepage](https://mohitagw15856.github.io/pm-claude-skills/skill/async-decision-memo.html) <br>
- [ClawHub skill page](https://clawhub.ai/mohitagw15856/skills/async-decision-memo) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown decision memo with kickoff and closing-note templates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes named roles, decision deadline, comment-resolution rules, escalation path, dissent record, reopen condition, and filing guidance.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
