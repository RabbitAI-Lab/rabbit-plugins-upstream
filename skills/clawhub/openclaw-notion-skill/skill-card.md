## Description: <br>
Integrates OpenClaw agents with explicitly shared Notion pages and databases so they can read content, query databases, create entries, update records, append blocks, and search workspace content. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[moikapy](https://clawhub.ai/user/moikapy) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and OpenClaw users use this skill to connect agents to Notion for knowledge bases, project tracking, content pipelines, CRM records, and collaborative documentation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can change Notion pages and databases that are shared with its integration. <br>
Mitigation: Share only the minimum required pages or databases with a dedicated Notion integration, and review agent automation before it modifies business, CRM, project, or customer records. <br>
Risk: The skill depends on a local Notion token. <br>
Mitigation: Keep NOTION_TOKEN out of source control, store it with restrictive local permissions, and rotate the token if it may have been exposed. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/moikapy/skills/openclaw-notion-skill) <br>
- [Publisher Profile](https://clawhub.ai/user/moikapy) <br>
- [Notion Integrations](https://www.notion.so/my-integrations) <br>
- [Notion](https://notion.so) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, TypeScript examples, JSON templates, and JSON CLI output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a local NOTION_TOKEN and only operates on Notion pages or databases explicitly shared with the integration.] <br>

## Skill Version(s): <br>
0.1.0 (source: SKILL.md frontmatter, package.json, skill.json, ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
