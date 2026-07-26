## Description: <br>
Use this skill for HTML documents that go through LLM-human review cycles, including drafting, reading annotated files, and revising documents from embedded feedback. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ljn-hust](https://clawhub.ai/user/ljn-hust) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and document authors use this skill to create browser-openable HTML drafts with review metadata, read human annotations from html-collab files, and produce revised HTML that preserves feedback history. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may write generated HTML files or overwrite revised documents. <br>
Mitigation: Use it on non-sensitive drafts first, keep backups, and ask the agent to confirm before saving or replacing an original file. <br>
Risk: The skill may run local image-processing commands while handling embedded screenshots. <br>
Mitigation: Review proposed commands before execution and confirm compression behavior before modifying document data. <br>
Risk: The artifact includes hidden AI-facing bootstrap text in generated HTML. <br>
Mitigation: Review generated HTML before sharing or deploying it, especially bootstrap comments and embedded collaboration metadata. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ljn-hust/skills/html-collab) <br>
- [html-collab live demo](https://ljn-hust.github.io/html-collab/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, HTML files, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and complete HTML document output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write generated or revised HTML files and may propose local image-compression commands when processing embedded screenshots.] <br>

## Skill Version(s): <br>
0.2.0 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
