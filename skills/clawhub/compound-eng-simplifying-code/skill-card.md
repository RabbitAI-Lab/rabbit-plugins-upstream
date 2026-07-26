## Description: <br>
Simplifies, polishes, and declutters code without changing behavior for requests to clean up, refactor, remove dead code or AI slop, or improve readability. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[iliaal](https://clawhub.ai/user/iliaal) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering agents use this skill to make scoped, behavior-preserving simplification changes to authorized codebases. It is intended for cleanup and refactoring work where readability and maintainability improve without changing public APIs, side effects, or error behavior. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Behavior-preserving cleanup can still change runtime behavior if edge cases, public APIs, side effects, or error paths are misunderstood. <br>
Mitigation: Review diffs, preserve documented invariants, and run tests or type checks covering touched files and importers before accepting changes. <br>
Risk: The skill may remove dead-looking code or simplify defensive checks that encode domain constraints. <br>
Mitigation: Require evidence before removals, ask when intent is unclear, and keep domain-specific complexity or API changes out of scope unless explicitly authorized. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/iliaal/skills/compound-eng-simplifying-code) <br>
- [SPEC.md](artifact/SPEC.md) <br>


## Skill Output: <br>
**Output Type(s):** [code, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown status reports with code edits and optional shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports scope touched, key simplifications, verification performed, and residual risks.] <br>

## Skill Version(s): <br>
4.3.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
