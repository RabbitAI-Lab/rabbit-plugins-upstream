## Description: <br>
Audits Rust code for unsafe blocks, ownership issues, and Cargo dependency risks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to review Rust changes for ownership, error handling, concurrency, unsafe code, dependency risk, performance, idioms, and test quality before merge or release. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can suggest local Cargo analysis commands, including commands that may install tools or perform dependency and network checks. <br>
Mitigation: Review proposed commands before running them, especially installation, audit, outdated, deny, or other dependency-check commands. <br>
Risk: Broad Rust-related triggers may activate the skill in contexts where its opinionated audit workflow is not needed. <br>
Mitigation: Use it for Rust code-review tasks and disregard or disable it for unrelated review work. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/athola/skills/nm-pensive-rust-review) <br>
- [Project Homepage from ClawHub Metadata](https://github.com/athola/claude-night-market/tree/master/plugins/pensive) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, shell commands, guidance] <br>
**Output Format:** [Markdown review report with optional inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes categorized findings, recommendations, evidence logging, and an approve / approve with actions / block recommendation.] <br>

## Skill Version(s): <br>
1.9.16 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
