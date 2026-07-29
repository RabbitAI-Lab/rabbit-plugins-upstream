## Description: <br>
Provides agent guidance for querying Alibaba Bailian/DashScope WebSearch and returning concise multi-source search results. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and AI agents use this skill to run quick web searches through Bailian/DashScope, gather current facts, and pass summarized results into research or question-answering workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search queries are sent to Alibaba Bailian/DashScope using DASHSCOPE_API_KEY. <br>
Mitigation: Use the skill only when that external API use is acceptable, avoid sensitive query content, and manage the API key as a secret. <br>
Risk: The artifact documentation references a required search script or runtime integration, but the artifact only includes SKILL.md. <br>
Mitigation: Confirm the expected search script or integration is supplied by the installed package source before relying on the skill in an agent workflow. <br>
Risk: Some SEO and ranking language is broader than the artifact-backed search behavior. <br>
Mitigation: Treat the skill as a web-search helper, not an SEO manipulation or ranking automation tool. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/bailian-search-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and text or JSON-style search result examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires DASHSCOPE_API_KEY and network access to Bailian/DashScope; examples describe up to 20 results per query.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata; artifact frontmatter reports 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
