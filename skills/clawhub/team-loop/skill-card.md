## Description: <br>
team-loop is an autonomous task loop engine that turns a quantifiable development goal into repeated plan, execute, verify, memorize, and replan cycles. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ifeel-is-a-mouse](https://clawhub.ai/user/ifeel-is-a-mouse) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use team-loop to pursue quantifiable repository goals such as coverage improvement, code migration, refactoring, test completion, and token-budgeted tasks. The skill is intended for repositories where autonomous edits, test execution, commits, reverts, and persisted loop state are acceptable. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can autonomously create, edit, delete, commit, revert, and branch repository files after a quantifiable goal is accepted. <br>
Mitigation: Install only in repositories where autonomous code changes are acceptable, prefer a disposable clone or branch, and set tight budget and max_rounds limits before invoking it. <br>
Risk: The skill runs project code and tests in subprocesses, which can execute untrusted code paths. <br>
Mitigation: Avoid untrusted or secrets-heavy repositories and run the loop only in controlled environments where test execution risk is acceptable. <br>
Risk: The skill persists prompts, code context, file paths, debug logs, RDF memory, and patches on disk. <br>
Mitigation: Verify `.team-loop/`, `logs/`, and `rdf/` are ignored, reviewed, or cleaned before sharing the repository. <br>
Risk: Broad trigger terms could start a powerful autonomous workflow when the user did not intend it. <br>
Mitigation: Rely on explicit user invocation, review the goal before launch, and use `.team-loop/STOP` to request a safe halt. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ifeel-is-a-mouse/skills/team-loop) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/ifeel-is-a-mouse) <br>


## Skill Output: <br>
**Output Type(s):** [Code, Files, Shell commands, Configuration, Markdown, JSON, Turtle] <br>
**Output Format:** [Repository changes plus JSON, Markdown, Turtle, logs, patches, and audit artifacts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces incremental deliverables, state snapshots, audit reports, token reports, change records, patches, and RDF memory entries; may commit or revert changes during the loop.] <br>

## Skill Version(s): <br>
2.4.1 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
