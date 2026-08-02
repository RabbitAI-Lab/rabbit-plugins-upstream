## Description: <br>
Audits shell scripts for correctness, portability, and common pitfalls. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to review shell, Bash, POSIX, CI, hook, wrapper, and build scripts before committing or shipping changes. It focuses the review on exit-code handling, portability, safety patterns, structure, and evidence-backed findings. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill includes shell and package-manager command examples that could be mistaken for commands to run automatically. <br>
Mitigation: Treat command snippets as review aids and approve any actual command execution separately. <br>
Risk: Some review guidance references format-changing commands such as shfmt -w that can modify files. <br>
Mitigation: Review proposed write operations before execution and prefer dry runs or diffs when available. <br>
Risk: Shell review guidance can miss project-specific behavior or test expectations. <br>
Mitigation: Confirm findings against file:line evidence, run shellcheck where applicable, and use the project's existing tests before accepting changes. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-pensive-shell-review) <br>
- [Pensive plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/pensive) <br>
- [Exit code patterns](modules/exit-codes.md) <br>
- [Shell portability](modules/portability.md) <br>
- [Shell safety patterns](modules/safety-patterns.md) <br>
- [Shell structure patterns](modules/structure-patterns.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, guidance] <br>
**Output Format:** [Markdown review report with findings, file references, command snippets, suggested fixes, and an approval recommendation.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill produces review guidance and proposed changes; it does not need to write files itself.] <br>

## Skill Version(s): <br>
1.9.17 (source: ClawHub release evidence; artifact frontmatter reports 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
