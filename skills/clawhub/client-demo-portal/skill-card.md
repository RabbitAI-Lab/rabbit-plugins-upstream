## Description:

Helps agents rapidly prepare enterprise PatSnap intelligence portal demo prototypes, including requirements analysis, local setup, data integration, and demo talk tracks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Customer-facing solution engineers and demo builders use this skill to assemble a local intelligence portal proof of concept for enterprise conversations. It provides implementation notes, integration details, troubleshooting lessons, and a short demo script for client presentations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Customer or internal context may be sent to external AI or API services.

Mitigation: Use non-sensitive demo data by default and require customer or IT approval before sending internal documents or proprietary questions to PatSnap MCP, DeepSeek, SerpAPI, or NewsAPI.

Risk: API keys may be exposed if copied into source files or shared artifacts.

Mitigation: Keep API keys in local environment files, keep them out of source control, and review generated portal files before sharing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/client-demo-portal)
- [Hongyuan portal lessons 0527](references/hongyuan_lessons_0527.md)
- [Hongyuan portal current state](references/hongyuan_portal_state.md)
- [Lessons learned](references/lessons-learned.md)
- [PatSnap open platform](https://open.zhihuiya.com/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with code snippets, shell commands, and configuration notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference external API and MCP configuration that must be supplied by the user environment.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
