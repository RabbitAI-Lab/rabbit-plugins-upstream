## Description: <br>
Orchestrates the QUALITY pipeline stage for egregore work items, running code review, unbloat, and test updates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to run quality checks on egregore work items, perform self-review before pull requests, and review another agent's pull request in PR-review mode. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad review-related triggers can accidentally activate workflows that commit fixes or post GitHub pull request reviews. <br>
Mitigation: Narrow or override triggers before use, and require explicit user confirmation before auto-fix commits or GitHub pull request review posting. <br>


## Reference(s): <br>
- [claude-night-market egregore plugin](https://github.com/athola/claude-night-market/tree/master/plugins/egregore) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and structured JSON snippets with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce quality findings, verdicts, manifest decision records, auto-fix changes, commits, and GitHub pull request review comments depending on mode and user confirmation.] <br>

## Skill Version(s): <br>
1.9.17 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
