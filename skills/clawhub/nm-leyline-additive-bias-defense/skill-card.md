## Description: <br>
Inverts burden of proof for code additions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and code reviewers use this guidance skill to challenge proposed code, file, abstraction, error-handling, and configuration additions before accepting them. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may activate during common PR review or refactor-planning conversations because of broad trigger wording. <br>
Mitigation: Review the trigger wording and invoke the skill explicitly when tighter control is needed. <br>
Risk: Guidance-oriented outputs may introduce incorrect or misleading review conclusions if accepted without review. <br>
Mitigation: Review and scan the skill before deployment, and treat its verdicts as review guidance rather than automatic enforcement. <br>


## Reference(s): <br>
- [Leyline plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/leyline) <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-leyline-additive-bias-defense) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, text] <br>
**Output Format:** [Markdown guidance with scrutiny questions, anti-pattern checks, and burden-of-proof verdicts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Broad trigger wording may activate during common PR review or refactor-planning conversations.] <br>

## Skill Version(s): <br>
1.9.16 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
