## Description: <br>
Search Kuaishou works by keyword, filter results by sort order and publish time, and return linked result tables with engagement metrics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[redfox-data](https://clawhub.ai/user/redfox-data) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users such as content creators, operations teams, data analysts, brands, MCNs, and e-commerce sellers use this skill to research Kuaishou trends, compare engagement, browse result pages, and subscribe to keyword updates. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a RedFox API key and sends search terms to RedFox. <br>
Mitigation: Install only if that data sharing is acceptable; use a scoped and revocable key, and avoid hardcoding or exposing it in prompts, logs, or files. <br>
Risk: The daily subscription flow may create recurring execution, including a raw crontab fallback. <br>
Mitigation: Prefer a platform-managed scheduler, confirm the recurring task before enabling it, and keep a clear way to list and remove any created task. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/redfox-data/skills/kuaishou-search) <br>
- [RedFoxHub](https://redfox.hk) <br>
- [RedFox API key settings](https://redfox.hk/settings/api-keys?source=clawhub) <br>
- [RedFox Kuaishou keyword search endpoint](https://redfox.hk/story/api/ks/search/keywordSearchWork) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, JSON, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown tables and user prompts, with JSON returned by the search script] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes Kuaishou titles, authors, engagement counts, links, publish times, pagination state, and subscription prompts.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
