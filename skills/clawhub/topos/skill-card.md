## Description: <br>
Structural code quality metrics, lattice verification, and refactor loops for agent-written code. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[krv-labs](https://clawhub.ai/user/krv-labs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and AI coding agents use Topos to measure structural quality in local repositories, identify refactor targets, and verify whether changes improve SIMPLE, COMPOSABLE, and SECURE scores. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The installer and global npm package execute code on the local machine. <br>
Mitigation: Review the remote installer and global package before installation. <br>
Risk: Refactor guidance can change program behavior because Topos measures structure, not functional correctness. <br>
Mitigation: Review changes and run the project's tests or linters before accepting refactors. <br>
Risk: SECURE scores are structural heuristics rather than full security assurance. <br>
Mitigation: Use dedicated security tooling for high-stakes code and explicitly review remaining SECURE findings. <br>
Risk: Dependency graph generation may create local .gitnexus artifacts. <br>
Mitigation: Review generated artifacts and repository status before committing changes. <br>


## Reference(s): <br>
- [Topos documentation](https://docs.krv.ai/topos/) <br>
- [Topos agent contract](https://docs.krv.ai/topos/agents.html) <br>
- [ClawHub listing](https://clawhub.ai/krv-labs/skills/topos) <br>


## Skill Output: <br>
**Output Type(s):** [analysis, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [CLI tables and ranked file lists, Markdown guidance, and MCP structured JSON payloads.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write local .gitnexus graph artifacts when dependency graph generation is enabled; does not modify source files unless the agent acts on the guidance.] <br>

## Skill Version(s): <br>
1.0.7 (source: ClawHub release metadata; artifact frontmatter reports 0.4.3) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
