## Description: <br>
Generate a tailored code review checklist for any pull request based on the language, type of change, and risk level. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mohitagw15856](https://clawhub.ai/user/mohitagw15856) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering reviewers use this skill to turn pull request context into a focused review checklist with language-specific checks, risk-scaled depth, and approve or request-changes criteria. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Pull request descriptions or diffs can contain secrets, credentials, or proprietary code. <br>
Mitigation: Redact sensitive values and share only the code context needed to generate the checklist. <br>
Risk: A checklist can be incomplete or misleading when key review inputs are missing. <br>
Mitigation: Provide the language, framework, change type, risk level, pull request description, and relevant diff before relying on the recommendation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mohitagw15856/skills/code-review-checklist) <br>
- [Project skill page](https://mohitagw15856.github.io/pm-claude-skills/skill/code-review-checklist.html) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, guidance] <br>
**Output Format:** [Markdown checklist with review decision criteria] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Tailored to the supplied language, change type, risk level, pull request description, optional diff, and author context.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
