## Description: <br>
Scores pasted job postings on separate desirability and candidacy dimensions against a user's stored criteria, then returns a concrete action and logs the evaluation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bwancoding](https://clawhub.ai/user/bwancoding) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Job seekers use this skill to evaluate a posting or recruiter message against their own criteria, separating whether they want the role from whether they meet its stated requirements. It also supports criteria setup, history review, role comparison, trend analysis, and gap planning over accumulated evaluations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill keeps local job-search preferences, compensation preferences, skills, and evaluation history, and full raw-JD history can include recruiter messages or contact details. <br>
Mitigation: Use standard history unless raw posting text is needed, avoid full history in synced or shared workspaces, and review the local Markdown files before sharing them. <br>
Risk: Future recommendations depend on the user's stored criteria and skills inventory, so stale or malformed profile data can skew verdicts. <br>
Mitigation: Review and update jd_criteria.md when preferences or skills change, and answer the skill's clarification prompts instead of letting uncertain fields stand. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/bwancoding/skills/jd-triage) <br>
- [Criteria Template](assets/criteria-template.yaml) <br>
- [Bootstrap Reference](references/bootstrap.md) <br>
- [Scoring Reference](references/scoring.md) <br>
- [History Reference](references/history.md) <br>
- [Analyze and Plan Reference](references/analysis-commands.md) <br>
- [Intensity Signals Reference](references/intensity-signals.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown verdicts and local Markdown criteria/history files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs keep desirability and candidacy separate, preserve user-language free text, and may append evaluation history under ~/.openclaw/workspace.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
