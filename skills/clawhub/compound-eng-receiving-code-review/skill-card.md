## Description: <br>
Helps agents process PR/MR review feedback critically by verifying correctness before acting, pushing back on incorrect suggestions, and avoiding performative agreement. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[iliaal](https://clawhub.ai/user/iliaal) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering agents use this skill to triage, respond to, and selectively implement PR/MR review feedback with evidence-based judgment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Incorrect reviewer suggestions can lead an agent to introduce bugs or unnecessary complexity. <br>
Mitigation: Verify each suggestion against the codebase, cite concrete evidence, and implement only feedback that is technically correct. <br>
Risk: Automated review handling can overreach when feedback is security-related, ambiguous, architectural, or user-visible. <br>
Mitigation: Escalate these cases instead of auto-fixing or auto-declining them, especially in headless mode. <br>
Risk: The skill may guide an agent to read and respond to PR review comments using existing GitHub access. <br>
Mitigation: Use it only in the intended review workflow with appropriate repository permissions and review proposed responses before posting when risk is unclear. <br>


## Reference(s): <br>
- [Skill specification](SPEC.md) <br>
- [Headless Mode](references/headless-mode.md) <br>
- [ClawHub skill page](https://clawhub.ai/iliaal/skills/compound-eng-receiving-code-review) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Text, Markdown, Code, Shell commands] <br>
**Output Format:** [Markdown responses with optional code, shell commands, and structured triage summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Headless mode may return grouped AUTO-FIX, AUTO-DECLINE, ESCALATE, and prior-feedback results.] <br>

## Skill Version(s): <br>
4.3.3 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
