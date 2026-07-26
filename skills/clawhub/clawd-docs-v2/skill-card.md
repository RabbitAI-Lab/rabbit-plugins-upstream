## Description: <br>
Smart ClawdBot documentation access with local search index, cached snippets, and on-demand fetch. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aranej](https://clawhub.ai/user/aranej) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to find ClawdBot setup and troubleshooting documentation efficiently. It guides an agent to check local snippets and indexes first, then fetch full documentation pages only when needed. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Cached documentation can be stale or unexpected. <br>
Mitigation: Check cache freshness and verify important setup or troubleshooting guidance against the live ClawdBot documentation when cached snippets appear stale or surprising. <br>
Risk: The local documentation cache is used as an input source. <br>
Mitigation: Keep the local ~/clawd/data documentation cache trusted and review cached snippets before relying on sensitive setup instructions. <br>


## Reference(s): <br>
- [ClawdBot Documentation](https://docs.clawd.bot/) <br>
- [ClawdBot Skills Documentation](https://docs.clawd.bot/tools/skills) <br>
- [ClawdBot Multi-Agent Documentation](https://docs.clawd.bot/concepts/multi-agent) <br>
- [ClawdBot Documentation Index](https://docs.clawd.bot/llms.txt) <br>
- [ClawHub Skill Page](https://clawhub.ai/aranej/skills/clawd-docs-v2) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Code] <br>
**Output Format:** [Markdown guidance with shell commands and web_fetch examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Directs the agent to use local cached documentation first and fetch live documentation only when cache results are insufficient.] <br>

## Skill Version(s): <br>
2.2.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
