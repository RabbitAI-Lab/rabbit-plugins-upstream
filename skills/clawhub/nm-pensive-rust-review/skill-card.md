## Description: <br>
Audits Rust code for unsafe blocks, ownership issues, and Cargo dependency risks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use Rust Review to audit Rust code changes before merge, with focused checks for ownership, error handling, concurrency, unsafe blocks, dependency security, performance, tests, and idiomatic Rust patterns. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad Rust-related triggers may activate the skill during ordinary Rust discussions. <br>
Mitigation: Use the skill when structured Rust audit guidance is desired and review whether its checklist is relevant to the current task. <br>
Risk: The skill may suggest cargo commands, including package-installing tools such as cargo-mutants. <br>
Mitigation: Review suggested commands before execution and apply local project policy for installing or running Cargo tooling. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-pensive-rust-review) <br>
- [Skill homepage](https://github.com/athola/claude-night-market/tree/master/plugins/pensive) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown with structured review sections and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes review recommendations such as Approve, Approve with actions, or Block.] <br>

## Skill Version(s): <br>
1.9.17 (source: release evidence; artifact frontmatter says 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
