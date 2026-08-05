## Description: <br>
Reduce code complexity while preserving behavior using Chesterton's Fence, the Rule of 500, and verification-focused refactoring guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paudyyin](https://clawhub.ai/user/paudyyin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering agents use this skill to simplify existing code while preserving behavior, keeping changes scoped, readable, and consistent with project conventions. It is intended for refactoring workflows that require tests, build checks, linting, and diff review before changes are accepted. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Behavior-preserving refactors can still alter edge-case behavior when code context is incomplete. <br>
Mitigation: Limit changes to requested or recently modified code, inspect callers and tests first, and run existing tests without modifying expectations. <br>
Risk: Broad activation phrases may trigger refactoring work when the intended scope is ambiguous. <br>
Mitigation: Use an explicit file, function, or diff scope and review the proposed changes before accepting them. <br>
Risk: Large refactors or suggested commits can mix unrelated cleanup with functional work. <br>
Mitigation: Keep refactors incremental, avoid separate git commits without user approval, and use automated tooling for changes that exceed the Rule of 500 threshold. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/paudyyin/skills/code-simplifier) <br>
- [Publisher profile](https://clawhub.ai/user/paudyyin) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, code, shell commands, guidance] <br>
**Output Format:** [Markdown report with code blocks and concise refactoring guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Preserves behavior and expects verification with tests, build, lint, and diff review.] <br>

## Skill Version(s): <br>
1.1.0 (source: release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
