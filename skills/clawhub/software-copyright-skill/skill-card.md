## Description:

Generates Chinese software copyright registration documents by using an LLM to analyze project code and draft content, with Python scripts for Word template filling and format control.

This skill is ready for commercial/non-commercial use.

## Publisher:

[foamtor](https://clawhub.ai/user/foamtor)

### License/Terms of Use:

MIT

## Use Case:

Developers and legal or compliance teams use this skill to prepare Chinese software copyright registration packages for a codebase, including collection forms, user manuals, and source-code documents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill scans local project files and may include source code or sensitive project details in generated documents.

Mitigation: Run it only on projects intended for documentation, review generated code documents before sharing, and remove secrets or confidential implementation details.

Risk: Screenshots or browser-assisted documentation steps may expose production credentials or account data.

Mitigation: Use limited-scope test accounts or cookie files and avoid supplying real production credentials unless they are necessary and approved.

Risk: Optional global git proxy configuration can affect later repository operations outside this skill.

Mitigation: Review proxy commands before applying them and prefer scoped or temporary proxy settings when possible.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/foamtor/skills/software-copyright-skill)
- [Server-resolved GitHub provenance](https://github.com/Foamtor/software-copyright-skill)
- [README](README.md)
- [Format specification](references/格式规范.md)
- [Information collection form guidance](references/信息采集表填写要求.md)
- [python-docx](https://github.com/python-openxml/python-docx)
- [AgentSkills specification](https://github.com/vercel-labs/skills)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance, JSON content plans, Word document outputs, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create DOCX files, JSON content or configuration files, screenshots, diagrams, and validation reports in the user's workspace.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata; artifact frontmatter is 4.7.0 and artifact changelog top entry is 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
