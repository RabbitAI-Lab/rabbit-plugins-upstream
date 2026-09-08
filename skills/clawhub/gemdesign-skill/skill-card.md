## Description:

Generate, save, and modify GemDesign prototype pages via CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gemdesign-ai](https://clawhub.ai/user/gemdesign-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, designers, and product teams use this skill to generate high-fidelity GemDesign UI prototype pages from requirements, preview them locally, modify existing pages, and save them to the GemDesign platform.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can trigger global installation or update of the GemDesign npm CLI.

Mitigation: Install or update @gemdesign-ai/cli manually outside the agent, or review and approve the command before execution.

Risk: Token-based login and cloud syncing can upload prototype requirements, pages, and documents to GemDesign.

Mitigation: Use an approved GemDesign account token and avoid sensitive internal or customer data unless the upload is authorized.

Risk: Local preview server and browser actions can start background processes and bind local ports.

Mitigation: Verify the server status and port, stop prior GemDesign server processes before reuse, and review the saved app or page before continuing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gemdesign-ai/skills/gemdesign-skill)
- [GemDesign platform](https://design.gemcoder.com)
- [Node.js](https://nodejs.org/)
- [Agent Skills open standard](https://agentskills.io)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and generated HTML/code file content]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local HTML prototype files and invoke GemDesign CLI commands that sync pages to GemDesign.]

## Skill Version(s):

0.1.11 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
