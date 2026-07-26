## Description: <br>
Generates a weekly agentic commerce news briefing from recent public web and social sources, highlighting startups, products, funding, endorsements, and trends. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xuxinmaxen](https://clawhub.ai/user/xuxinmaxen) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, founders, investors, and operators use this skill to monitor recent agentic commerce market activity and produce a concise briefing with categorized news cards, source links, a summary table, and trend takeaways. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Recurring digest setup can create persistent scheduled execution when the runtime uses OpenClaw or system cron. <br>
Mitigation: Confirm the scheduler and persistence model before enabling recurrence; avoid system crontab unless local persistence is intended and document how to list and remove the job. <br>
Risk: Live public web results and recycled timestamps can cause stale or misdated items to appear in a news briefing. <br>
Mitigation: Verify publish dates on source pages for top and fuzzy-dated items, and drop items that cannot be confirmed inside the requested time window. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/xuxinmaxen/skills/agentic-commerce-news) <br>
- [README](README.md) <br>
- [Latest briefing archive entry](briefings/2026-06-29.md) <br>
- [Briefing archive](briefings/README.md) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, shell commands, guidance] <br>
**Output Format:** [Markdown news briefing with source links, categorized cards, a summary table, and weekly trend takeaways; scheduling guidance may include shell commands.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires web search and web fetch access. Recurring scheduling should be explicitly confirmed before setup.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
