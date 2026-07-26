## Description: <br>
Pre-release code review that runs lint and type checks, reviews diffs for cleanliness, design, efficiency, and side-effect ordering issues, validates findings, and fixes approved issues. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tenequm](https://clawhub.ai/user/tenequm) <br>

### License/Terms of Use: <br>
Apache 2.0 <br>


## Use Case: <br>
Developers and engineering teams use this skill before committing, pushing, or releasing code to catch actionable issues in changed files and apply targeted fixes after approval. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may run project-defined validation commands while reviewing a repository. <br>
Mitigation: Use it only where running the repository's scripts is acceptable, especially for untrusted repositories, and review commands before allowing execution. <br>
Risk: The skill can edit files and the security summary notes some fixes may occur before clear approval. <br>
Mitigation: Require explicit approval before automatic fixes and review all generated changes before committing or releasing them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/tenequm/skills/code-polish) <br>
- [Project homepage](https://github.com/tenequm/skills/tree/main/skills/polish) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, guidance] <br>
**Output Format:** [Markdown review report with file references; shell commands and code or file edits may be produced when fixes are approved.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Accepts an optional base-ref argument and requires approval before proceeding from reported findings to fixes.] <br>

## Skill Version(s): <br>
2.4.1 (source: frontmatter and changelog, released 2026-07-22) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
