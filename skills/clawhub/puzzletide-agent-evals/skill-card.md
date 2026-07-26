## Description: <br>
Generates reproducible puzzle-based reasoning tasks and local grading workflows for benchmarking or testing LLMs and agents with the PuzzleTide CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[catorch](https://clawhub.ai/user/catorch) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and evaluators use this skill to generate deterministic sudoku or word-search task sets, run a subject model, and check answers locally with objective pass/fail scoring. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Running npm or npx may download and execute the published PuzzleTide package. <br>
Mitigation: Approve the package source intentionally and ask before installing or using npx when the local CLI is unavailable. <br>
Risk: Puzzle-based evals can be overinterpreted as a complete model benchmark. <br>
Mitigation: Use the generated tasks as objective reasoning checks and pair the results with broader evaluations for production decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/catorch/skills/puzzletide-agent-evals) <br>
- [PuzzleTide Agent Evals documentation](https://github.com/Caravaca-Labs/puzzletide-cli/blob/main/docs/agent-skills.md#puzzletide-agent-evals) <br>
- [PuzzleTide CLI repository](https://github.com/Caravaca-Labs/puzzletide-cli) <br>
- [PuzzleTide CLI reference](https://github.com/Caravaca-Labs/puzzletide-cli/blob/main/docs/cli.md) <br>
- [puzzletide npm package](https://www.npmjs.com/package/puzzletide) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, JSON] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON file expectations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses local ptide or puzzletide commands when available; asks before installing packages; generated task sets and grading outputs are deterministic for the selected type, difficulty, count, and seed.] <br>

## Skill Version(s): <br>
0.1.1 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
