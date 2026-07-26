## Description: <br>
Structural code quality metrics, lattice verification, and refactor loops for agent-written code. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[krv-labs](https://clawhub.ai/user/krv-labs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and AI coding agents use this skill to assess local repositories, identify structural code quality issues, verify refactors, and optimize toward SILVER or GOLD lattice medals. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Installation uses an external install script and an npm package dependency. <br>
Mitigation: Review the install script and npm package source before installation. <br>
Risk: The tool reads local project code and git state and can write dependency graph artifacts. <br>
Mitigation: Use it only on repositories that are acceptable for local analysis and review generated artifacts before committing them. <br>
Risk: Topos scores are advisory structural signals rather than proof of functional correctness or full security assurance. <br>
Mitigation: Run normal tests, linters, security tooling, and code review before accepting refactors. <br>


## Reference(s): <br>
- [Topos documentation](https://docs.krv.ai/topos/) <br>
- [Topos agent contract](https://docs.krv.ai/topos/agents.html) <br>
- [ClawHub listing](https://clawhub.ai/krv-labs/skills/topos) <br>


## Skill Output: <br>
**Output Type(s):** [analysis, markdown, json, shell commands, guidance] <br>
**Output Format:** [CLI tables and ranked file lists, markdown reports, and MCP structured payloads with agent_contract fields.] <br>
**Output Parameters:** [Medal verdict, pillar scores, ranked refactor targets, and assessment status.] <br>
**Other Properties Related to Output:** [May write .gitnexus dependency graph artifacts when dependency graph generation is used; source edits are performed only if the agent acts on the guidance.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata; artifact frontmatter reports 0.4.2) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
