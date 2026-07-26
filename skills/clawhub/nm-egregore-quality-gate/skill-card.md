## Description: <br>
Orchestrates the QUALITY pipeline stage for egregore work items, running code review, unbloat, and test updates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to run egregore quality checks, self-review branch changes, update tests or docs, and prepare PR review outcomes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad triggers may invoke code-changing quality-gate behavior during ordinary review requests. <br>
Mitigation: Invoke it explicitly for egregore quality-gate work and review proposed commits before allowing changes to land. <br>
Risk: PR-review mode may guide agents toward posting GitHub review actions. <br>
Mitigation: Review any GitHub review action, approval, comment, or request-for-changes payload before it is submitted. <br>


## Reference(s): <br>
- [Egregore project homepage](https://github.com/athola/claude-night-market/tree/master/plugins/egregore) <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-egregore-quality-gate) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, code, markdown] <br>
**Output Format:** [Markdown guidance with command examples, JSON snippets, and review verdicts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide agents to inspect diffs, invoke mapped review or update skills, commit fixes, and prepare GitHub PR reviews.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
