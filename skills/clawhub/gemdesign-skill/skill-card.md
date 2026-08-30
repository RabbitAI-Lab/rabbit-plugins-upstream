## Description:

Generate, save, and modify GemDesign prototype pages via CLI for UI prototyping, page design, and batch generation from requirements.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gemdesign-ai](https://clawhub.ai/user/gemdesign-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, product teams, and design-oriented agent users use this skill to create, preview, modify, validate, and save high-fidelity GemDesign UI prototype pages from conversational prompts or requirements documents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or update a global npm package.

Mitigation: Review the skill before installing and prefer manually installing a pinned GemDesign CLI version.

Risk: The skill may ask for or use a GemDesign access token.

Mitigation: Authenticate through a secure channel and avoid pasting tokens into chat where possible.

Risk: The skill may create or modify GemDesign apps, pages, generated files, uploaded HTML/docs, browser state, and configuration under ~/.gemdesign.

Mitigation: Run it in an appropriate workspace/account, review generated files before upload, and inspect configuration changes after use.

## Reference(s):

- [Server-resolved GitHub source](https://github.com/gemdesign-ai/skills/tree/main/gemdesign-skill)
- [ClawHub skill page](https://clawhub.ai/gemdesign-ai/skills/gemdesign-skill)
- [GemDesign platform](https://design.gemcoder.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and generated HTML or documentation files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or modify local prototype files and platform pages through the GemDesign CLI when authorized.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata; artifact frontmatter reports 0.1.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
