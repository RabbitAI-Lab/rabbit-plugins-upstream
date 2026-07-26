## Description: <br>
PuzzleTide Word Search helps an agent generate word search puzzles with the local PuzzleTide CLI for themed, custom, printable, or app-oriented outputs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[catorch](https://clawhub.ai/user/catorch) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, educators, creators, and developers use this skill to generate word search grids, printable PDF or SVG worksheets, and JSON puzzle data through the local PuzzleTide CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Installing the third-party puzzletide npm CLI adds external code to the user's environment. <br>
Mitigation: Check for an existing ptide or puzzletide binary first and ask the user before installing the npm package. <br>
Risk: PDF, SVG, or JSON generation can overwrite a user-specified output path. <br>
Mitigation: Confirm output paths before running generation commands and review generated files before relying on them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/catorch/skills/puzzletide-word-search) <br>
- [PuzzleTide word search](https://puzzletide.com/word-search) <br>
- [Printable puzzles](https://puzzletide.com/printable) <br>
- [PuzzleTide CLI source](https://github.com/Caravaca-Labs/puzzletide-cli) <br>
- [PuzzleTide CLI reference](https://github.com/Caravaca-Labs/puzzletide-cli/blob/main/docs/cli.md) <br>
- [puzzletide npm package](https://www.npmjs.com/package/puzzletide) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Files, Configuration] <br>
**Output Format:** [Markdown guidance with shell commands; generated puzzle outputs may be PDF, SVG, or JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses a local CLI and may write output files when PDF, SVG, or JSON paths are requested.] <br>

## Skill Version(s): <br>
0.1.1 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
