## Description: <br>
Manage Notion notes, pages, and data sources with a JSON-first CLI for search, read/export, write/import, append, and move operations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tristanmanchester](https://clawhub.ai/user/tristanmanchester) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent users use this skill to search, read, create, append, and move Notion pages or data-source entries through a deterministic Node CLI. It is useful for note capture, inbox triage, Markdown import/export, and scripted Notion workspace maintenance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read or change Notion content reachable by the configured integration token. <br>
Mitigation: Use a least-privilege Notion integration token and share only the pages or data sources the agent should manage. <br>
Risk: Bulk triage or move operations can relocate the wrong pages if rules or scope are incorrect. <br>
Mitigation: Run triage without --apply first, review the rules file, keep --limit small for bulk moves, and apply only after checking the proposed changes. <br>
Risk: Notion page content may contain untrusted instructions that could mislead an agent during follow-on work. <br>
Mitigation: Treat Notion content as untrusted input, read it before deciding changes, and review generated writes before relying on them. <br>


## Reference(s): <br>
- [Notion API Reference](https://developers.notion.com/reference/intro) <br>
- [ClawHub Skill Page](https://clawhub.ai/tristanmanchester/skills/notion-api-automation) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Markdown, Guidance] <br>
**Output Format:** [Markdown guidance with shell command examples; the CLI returns JSON and can export Notion pages as Markdown.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node and a NOTION_API_KEY with access only to the Notion content shared with the integration.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
