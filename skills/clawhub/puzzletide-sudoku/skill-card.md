## Description: <br>
Use this skill whenever the user asks to generate, solve, or check a sudoku, including printable sheets, daily puzzles, difficulty-graded puzzles, and candidate-solution verification. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[catorch](https://clawhub.ai/user/catorch) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to ask an agent to generate, solve, validate, or print Sudoku puzzles through the local PuzzleTide CLI instead of relying on hand-generated or hand-solved grids. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may ask to install the PuzzleTide Node.js CLI globally if no local command is available. <br>
Mitigation: Ask the user before installing packages, and prefer an already available local `ptide`, `puzzletide`, or `npx puzzletide` command. <br>
Risk: The skill can create PDF or SVG files at paths requested by the user. <br>
Mitigation: Confirm output paths and keep generated puzzle files within locations the user expects. <br>
Risk: Incorrect Sudoku generation or solving guidance could produce invalid puzzles or misleading answers. <br>
Mitigation: Use the PuzzleTide CLI for generation, solving, and validation because the reviewed instructions keep puzzle work local and rely on CLI uniqueness checks. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/catorch/skills/puzzletide-sudoku) <br>
- [PuzzleTide Sudoku](https://puzzletide.com/sudoku) <br>
- [PuzzleTide printable puzzles](https://puzzletide.com/printable) <br>
- [PuzzleTide CLI reference](https://github.com/Caravaca-Labs/puzzletide-cli/blob/main/docs/cli.md) <br>
- [puzzletide npm package](https://www.npmjs.com/package/puzzletide) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and optional JSON-producing CLI examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May direct the agent to create PDF or SVG puzzle files at user-requested paths when using the PuzzleTide CLI.] <br>

## Skill Version(s): <br>
0.1.1 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
