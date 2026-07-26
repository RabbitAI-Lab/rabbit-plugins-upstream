## Description: <br>
Lightweight engineering workflow for agent-led development. Provides plan, work, verify, ship, and analyse commands with TDD, documentation discipline, security review, code review, and quality gates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[raunakkathuria](https://clawhub.ai/user/raunakkathuria) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use Buildwright to guide agent-led software development through planning, implementation, verification, review, and shipping workflows with TDD, documentation discipline, and security checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide real repository changes and GitHub shipping actions. <br>
Mitigation: Use it only in repositories where agent-led development is acceptable, review planned changes before committing or pushing, and run the workflow's verification and review steps. <br>
Risk: Generated implementation, documentation, or review guidance may be incorrect or incomplete. <br>
Mitigation: Treat outputs as engineering recommendations, inspect changed files, and require human review before relying on shipped changes. <br>


## Reference(s): <br>
- [Buildwright homepage](https://github.com/raunakkathuria/buildwright) <br>
- [Buildwright ClawHub skill page](https://clawhub.ai/raunakkathuria/skills/buildwright) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline commands and generated or updated project files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide file edits, quality-gate execution, security review, git commits, pushes, and PR creation according to the selected workflow command.] <br>

## Skill Version(s): <br>
0.0.19 (source: server release evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
