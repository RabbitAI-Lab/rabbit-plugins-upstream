## Description: <br>
Lint, check, and auto-fix Markdown files, including table of contents generation, broken link checks, YAML frontmatter validation, and formatting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[itspremkumar](https://clawhub.ai/user/itspremkumar) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, documentation owners, open-source maintainers, and agents use this skill to lint Markdown, normalize formatting, validate frontmatter, generate tables of contents, and check links. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Formatting and TOC insertion options can modify Markdown files. <br>
Mitigation: Use write or insert options only on files that are backed up or intended to be changed. <br>
Risk: External link checking can contact linked websites. <br>
Mitigation: Use external link checks only when outbound network requests to those URLs are acceptable. <br>
Risk: The bundled CI verifier executes repository checks and should not be treated as a sandbox. <br>
Mitigation: Run the verifier only on trusted repositories or inside an isolated environment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/itspremkumar/skills/md-linter) <br>
- [Publisher profile](https://clawhub.ai/user/itspremkumar) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Terminal text and Markdown, with optional in-place Markdown file edits.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can modify Markdown files when write or insert options are used; optional external link checks make outbound HTTP requests.] <br>

## Skill Version(s): <br>
2.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
