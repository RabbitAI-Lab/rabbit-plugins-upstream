## Description: <br>
Enforces token quota management at session start with conservation and compression checks for large context loads. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to keep long sessions within token and context budgets. It guides quota checks, read budgeting, delegation decisions, compression review, and concise next actions before large analyses or context-heavy work. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow can add process overhead to short or low-context tasks. <br>
Mitigation: Skip or disable the skill for short tasks where token planning overhead is not useful. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-conserve-token-conservation) <br>
- [Clawdis homepage](https://github.com/athola/claude-night-market/tree/master/plugins/conserve) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown checklist and concise procedural guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include token budget notes, compression recommendations, and next-action lists.] <br>

## Skill Version(s): <br>
1.9.16 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
