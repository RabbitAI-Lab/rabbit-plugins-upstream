## Description: <br>
Structural code quality metrics, lattice verification, and refactor loops for agent-written code. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[krv-labs](https://clawhub.ai/user/krv-labs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and AI coding agents use Topos to improve structural code quality, reduce complexity, verify refactors, and optimize local repositories toward SILVER or GOLD quality medals. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Topos is advisory and may guide structural refactors that change behavior. <br>
Mitigation: Run the project's tests, linters, and code review after edits; treat Topos verdicts as structural signals rather than proof of correctness. <br>
Risk: SECURE medal findings are structural heuristics, not complete security assurance. <br>
Mitigation: Use dedicated security tooling for high-stakes code and explicitly acknowledge any remaining SECURE findings. <br>
Risk: COMPOSABLE scoring depends on the external GitNexus package and generated .gitnexus project data. <br>
Mitigation: Install GitNexus only if acceptable for the environment, review generated .gitnexus artifacts as local project data, and check warnings before trusting composability scores. <br>


## Reference(s): <br>
- [Topos documentation](https://docs.krv.ai/topos/) <br>
- [Topos agent contract](https://docs.krv.ai/topos/agents.html) <br>
- [Topos source repository](https://github.com/Krv-Labs/topos) <br>
- [ClawHub listing](https://clawhub.ai/krv-labs/skills/topos) <br>
- [Krv Labs publisher profile](https://clawhub.ai/user/krv-labs) <br>


## Skill Output: <br>
**Output Type(s):** [analysis, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [CLI tables, ranked file lists, markdown guidance, and MCP structured payloads with agent_contract fields.] <br>
**Output Parameters:** [Medal verdict, SIMPLE/COMPOSABLE/SECURE pillar scores, ranked refactor targets, and assessment status.] <br>
**Other Properties Related to Output:** [May write .gitnexus graph artifacts when dependency graph generation is used; the skill does not modify source files unless the agent applies edits based on its guidance.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
