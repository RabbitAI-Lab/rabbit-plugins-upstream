## Description: <br>
Generate a Table of Contents from Markdown headings. Pure Python stdlib, no deps. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fuzzyb33s](https://clawhub.ai/user/fuzzyb33s) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and documentation authors use this skill to generate clickable Markdown tables of contents from headings in local Markdown files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read whichever local file path is passed to its Markdown TOC script. <br>
Mitigation: Run it only against intended Markdown files and avoid passing paths that contain private or unrelated content. <br>
Risk: The documented --anchor option is not supported by the current script. <br>
Mitigation: Use the supported options --ol, --min, and --flat, or update the script before relying on --anchor behavior. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/fuzzyb33s/skills/markdown-toc) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown table-of-contents text with optional shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports ordered lists, minimum heading level filtering, and flat list output.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
