## Description: <br>
Code Review orchestrates multi-agent pull request review by combining GitHub Copilot with adversarial, operational, and reference-comparison subagents for scoped triage. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[conorbronsdon](https://clawhub.ai/user/conorbronsdon) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to review pull requests by sizing the change, coordinating Copilot and targeted subagent review passes, and triaging findings into fix-now, stale, or deferred work. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Ordinary review requests can invoke the workflow and may use the user's GitHub CLI session to request Copilot review. <br>
Mitigation: Confirm the intended PR or branch before running GitHub operations, especially when the request is ambiguous. <br>
Risk: The workflow can lead to external state changes such as pushes or issue creation during follow-up remediation. <br>
Mitigation: Require explicit user confirmation before the first push or issue creation in a session. <br>


## Reference(s): <br>
- [Skill workflow](artifact/SKILL.md) <br>
- [README](artifact/README.md) <br>
- [Subagent prompt templates](artifact/patterns/subagent-prompts.md) <br>
- [ClawHub skill page](https://clawhub.ai/conorbronsdon/skills/code-review) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown review guidance with inline shell commands and structured subagent prompts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Subagent reports are capped at about 500 words by the artifact guidance.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
