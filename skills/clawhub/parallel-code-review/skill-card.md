## Description: <br>
Parallel Code Review dispatches two read-only review lenses to audit runtime safety and architecture consistency, then merges the findings into one concise review report. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hhetli](https://clawhub.ai/user/hhetli) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to review PRs, diffs, or completed work for runtime bugs, edge cases, race conditions, design alignment, and API contract consistency before merge. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Selected repository diffs may be sent to external review CLIs or providers during review. <br>
Mitigation: Choose an explicit mode, base, or commit; use dry-run to confirm scope; disable web search when it is not needed; and avoid including secrets in diffs or prompt files. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown review report with overview, issue lines, recommendations, and verdict] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill frames a read-only review and reports the resolved diff range when available.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
