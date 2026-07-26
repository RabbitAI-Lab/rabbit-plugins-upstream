## Description: <br>
Fetch Sudoku puzzles and store them as JSON in the workspace; render images on demand; reveal solutions later. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[odrobnik](https://clawhub.ai/user/odrobnik) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and puzzle creators use this skill to fetch Sudoku puzzles, store puzzle state locally, render printable puzzle assets, reveal solutions, and create share links. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill contacts sudokuonline.io and depends on listed Python libraries. <br>
Mitigation: Install and run it only in environments where that network access and those dependencies are acceptable. <br>
Risk: Generated local puzzle files include full solutions and generated share URLs. <br>
Mitigation: Treat puzzle JSON and generated links as shareable puzzle content, and avoid publishing them when a solution or puzzle identifier should remain private. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/odrobnik/skills/sudoku) <br>
- [Sudoku Data Format](references/DATA_FORMAT.md) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Markdown, Code, Shell commands, Files] <br>
**Output Format:** [JSON responses, human-readable text, local JSON puzzle files, rendered PNG/PDF/HTML files, and share URLs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3 with requests, Pillow, and lzstring; may contact sudokuonline.io and create local files containing puzzle solutions and generated share URLs.] <br>

## Skill Version(s): <br>
2.6.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
