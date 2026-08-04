## Description: <br>
Perform a single, read-only subagent review when the user explicitly invokes `$delegated-code-review`. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wufei-png](https://clawhub.ai/user/wufei-png) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to delegate a focused code review to a read-only subagent, verify the findings, and summarize accepted issues, fixes, tests, and remaining risks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill is framed as a read-only delegated review, but the runtime prompt can make fixes, run tests, and create commits after review findings. <br>
Mitigation: Review the skill before installation when a strictly read-only workflow is required, and constrain or supervise repository modification and commit permissions during use. <br>
Risk: Delegated review findings may be invalid, low-value, or not applicable to the current change. <br>
Mitigation: Verify each finding against the cited file and line before accepting it, record rejected findings, and rerun relevant tests after accepted fixes. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/wufei-png/skills/delegated-code-review) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, Code, Shell commands] <br>
**Output Format:** [Markdown summary with findings, decisions, fixes, verification results, and remaining risks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include code changes, test commands, and commit activity when accepted review findings require fixes.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
