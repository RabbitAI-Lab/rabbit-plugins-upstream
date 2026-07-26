## Description: <br>
Review a pull request or diff with prioritized, kind feedback focused on correctness, security, design, tests, readability, and a clear verdict. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mohitagw15856](https://clawhub.ai/user/mohitagw15856) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to review pull requests, diffs, or code changes and produce structured feedback ranked by severity with concrete suggestions and a final approve, request-changes, or comment verdict. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Users may provide sensitive code or context for review. <br>
Mitigation: Provide only code and context intended for the agent to review, and follow internal handling rules for confidential code. <br>
Risk: Review feedback may miss an issue, overstate severity, or suggest a change that does not fit the project. <br>
Mitigation: Treat the output as review assistance and have maintainers verify findings, severity, and suggested changes before merging. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mohitagw15856/skills/code-review-guide) <br>
- [Skill homepage](https://mohitagw15856.github.io/pm-claude-skills/skill/code-review-guide.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance, Analysis] <br>
**Output Format:** [Markdown review with summary, prioritized review passes, severity-ranked comments, strengths, and verdict] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [No scripts or runtime side effects; output is code review feedback for the provided change.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
