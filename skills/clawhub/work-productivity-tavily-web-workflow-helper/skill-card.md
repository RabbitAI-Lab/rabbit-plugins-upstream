## Description: <br>
Helps agent users, skill authors, maintainers, and teams plan, debug, harden, and improve Tavily-style web-search workflows or adjacent skills. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, AI-agent users, skill authors, maintainers, and teams use this skill to turn Tavily-style web-search workflow needs into actionable plans, checklists, code-change support, and verification notes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may be invoked more often than intended because its trigger terms are generic and implicit invocation is enabled. <br>
Mitigation: Invoke it explicitly by name for Tavily or web-search workflow tasks; maintainers should narrow trigger wording if the package is updated. <br>
Risk: Generated workflow, checklist, analysis, or code-change guidance may be incomplete or misleading if the user's constraints are underspecified. <br>
Mitigation: Restate assumptions and success criteria, ask only for missing inputs that materially affect the result, and include a verification note with remaining risks. <br>


## Reference(s): <br>
- [Requirement Plan](references/requirement-plan.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/kyro-ma/skills/work-productivity-tavily-web-workflow-helper) <br>
- [Tavily Search Demand Signal](https://clawhub.ai/skills/openclaw-tavily-search) <br>
- [Ask HN: Combining Global Knowledge, Internet Search, and User RAG](https://news.ycombinator.com/item?id=49059969) <br>
- [PostHog Question Routing Feature Request](https://github.com/PostHog/posthog/issues/74084) <br>
- [SeerrFin Discovery Tabs Request](https://github.com/varunaditya-plus/SeerrFin/issues/18) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Analysis, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown with optional code blocks, shell commands, checklists, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs should state assumptions, success criteria, validation performed, and remaining risks when helpful.] <br>

## Skill Version(s): <br>
0.20260728.1730 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
