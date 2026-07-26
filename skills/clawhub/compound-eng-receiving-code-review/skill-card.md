## Description: <br>
Guides agents through critical triage of PR/MR review feedback, including verifying suggestions, pushing back with evidence when needed, and implementing only confirmed fixes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[iliaal](https://clawhub.ai/user/iliaal) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering agents use this skill to respond to PR/MR review comments, triage automated or human suggestions, and decide whether to fix, clarify, or push back with evidence. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may use an existing GitHub CLI session to read PR comments or draft and post review-thread replies when asked. <br>
Mitigation: Review the target repository, comments, and reply text before allowing commands that read or post PR review content. <br>
Risk: Incorrect triage could accept bad review feedback or dismiss valid feedback. <br>
Mitigation: Require evidence-backed verification, escalate ambiguous or security-related suggestions, and test each implemented fix individually. <br>


## Reference(s): <br>
- [Headless Mode](references/headless-mode.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Text, Markdown, Shell commands] <br>
**Output Format:** [Markdown guidance with optional structured triage summaries and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Headless mode returns AUTO-FIX, AUTO-DECLINE, ESCALATE, and PRIOR FEEDBACK sections.] <br>

## Skill Version(s): <br>
4.2.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
