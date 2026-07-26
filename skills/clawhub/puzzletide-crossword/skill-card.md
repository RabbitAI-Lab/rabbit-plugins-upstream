## Description: <br>
Use this skill whenever the user asks for a crossword puzzle: custom word/clue lists, themed crosswords, educational worksheets, or printable PDFs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[catorch](https://clawhub.ai/user/catorch) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, educators, puzzle creators, and developers use this skill to have an agent generate valid crossword grids, printable worksheets, PDFs, or structured JSON through the local PuzzleTide CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may ask the agent to run the third-party PuzzleTide npm CLI or use npx. <br>
Mitigation: Prefer an already-installed local binary and require user approval before npm install, npx execution, or global package installation. <br>
Risk: Generated crossword content can contain incorrect clues or unplaced words if the supplied word list is unsuitable. <br>
Mitigation: Review the generated clue list, solution, and any reported unplaced words before using the puzzle in teaching, publication, or distribution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/catorch/skills/puzzletide-crossword) <br>
- [PuzzleTide crossword](https://puzzletide.com/crossword) <br>
- [PuzzleTide printable puzzles](https://puzzletide.com/printable) <br>
- [PuzzleTide npm package](https://www.npmjs.com/package/puzzletide) <br>
- [PuzzleTide CLI reference](https://github.com/Caravaca-Labs/puzzletide-cli/blob/main/docs/cli.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Markdown, Files, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with inline bash commands, optional JSON output, and generated PDF files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses a local PuzzleTide CLI binary when available; npm installation should require user approval.] <br>

## Skill Version(s): <br>
0.1.1 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
