## Description: <br>
Code Simplification helps agents simplify existing working code by removing speculative abstractions, dead flexibility, and needless indirection while preserving verified behavior and documenting removals. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mohitagw15856](https://clawhub.ai/user/mohitagw15856) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill after working code exists to reduce unnecessary abstractions, dead configuration, forwarding layers, and hard-to-read cleverness while preserving behavior. It is useful after feature work, for over-engineered AI-generated code, and as a cleanup pass before code review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A simplification pass can unintentionally change behavior in working code. <br>
Mitigation: Run the relevant verification before and after changes, add pinning tests where coverage is thin, and accept only diffs with identical behavior evidence. <br>
Risk: Removing unusual or indirect code can delete load-bearing behavior whose purpose is not obvious locally. <br>
Mitigation: Check history with git log or blame before deleting strange code, and inspect callers when changing exported or shared surfaces. <br>
Risk: Large cleanup diffs can be hard to review if removals are unexplained. <br>
Mitigation: Require a removal ledger that states what was removed, why it was safe, and what future flexibility was intentionally foreclosed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mohitagw15856/skills/code-simplification) <br>
- [Skill homepage](https://mohitagw15856.github.io/pm-claude-skills/skill/code-simplification.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, guidance] <br>
**Output Format:** [Markdown with code changes, verification notes, and a removal-ledger table] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes a simplified code result, removal justifications, verification evidence, and notes on deliberately retained complexity.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
