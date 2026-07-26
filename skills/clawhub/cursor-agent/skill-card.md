## Description: <br>
A comprehensive skill for using the Cursor CLI agent for software engineering tasks, including tmux-based automation guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[swiftlysingh](https://clawhub.ai/user/swiftlysingh) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to install, authenticate, configure, and operate Cursor CLI for code review, refactoring, debugging, CI-style analysis, and terminal-based AI pair programming. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill includes automation patterns that install remote code and may approve workspace trust prompts. <br>
Mitigation: Use a verifiable installer or package-manager path, and do not automate workspace trust for untrusted or newly downloaded projects. <br>
Risk: Force or automated execution can apply repository changes without normal interactive review. <br>
Mitigation: Avoid force mode unless changes are reviewed and reversible, and inspect generated file and command changes before relying on them. <br>


## Reference(s): <br>
- [Cursor CLI installer](https://cursor.com/install) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes command examples for interactive, non-interactive, tmux, MCP, and CI-style Cursor CLI workflows.] <br>

## Skill Version(s): <br>
2.1.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
