## Description: <br>
Sorts, deduplicates, reverses, or shuffles lines in local UTF-8 text files using a Python standard-library command-line script. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[freedompixels](https://clawhub.ai/user/freedompixels) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and text-maintenance users use this skill to run a local Python utility for sorting, deduplicating, reversing, or shuffling line-oriented text files such as keyword lists, task lists, names, and sample lists. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Passing an existing path with -o can overwrite that file with the processed line output. <br>
Mitigation: Choose output paths deliberately, write to a new file when preserving originals matters, and review the result before replacing source files. <br>
Risk: When no output path is provided, the selected file's contents are printed to the terminal. <br>
Mitigation: Use -o for sensitive files or avoid running the utility on confidential text in shared terminals or logged sessions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/freedompixels/skills/cn-line-sorter) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and terminal text output guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can print transformed text to the terminal or write UTF-8 text output to a user-specified file path.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
