## Description: <br>
Conducts rigorous code and pull request reviews that identify security holes, edge case failures, accessibility problems, performance risks, type-safety issues, and code-quality concerns with severity-tiered recommendations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yun520-1](https://clawhub.ai/user/yun520-1) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this skill to perform adversarial reviews of code snippets and pull requests across Python, R, JavaScript/TypeScript, SQL, and front-end code before merging or relying on changes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Review feedback may be overly strict, incomplete, or misleading when the agent sees only partial code or lacks repository context. <br>
Mitigation: Validate findings against the full codebase, tests, and project conventions before making code or merge decisions. <br>
Risk: The skill is designed to surface security and operational concerns, but its findings are advisory and may include false positives. <br>
Mitigation: Use scoped credentials for any follow-up investigation, review proposed commands or changes before execution, and confirm material security findings through normal engineering review. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/yun520-1/skills/critical-code-reviewer) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown with structured review sections and severity tiers] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes actionable findings, review boundaries when context is incomplete, verdicts, and optional next-step guidance.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
