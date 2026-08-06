## Description: <br>
ai-news helps agents retrieve daily news summaries, ranked headlines, category views, and article details from an external news API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to ask an agent for current or date-specific Chinese news summaries, headline rankings, category-filtered lists, and article details. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The published instructions advertise database, file, and command capabilities that are broader than a passive news retrieval skill needs. <br>
Mitigation: Limit routine use to news retrieval, tighten prompts and documentation to news-only behavior, and review any proposed command before execution. <br>
Risk: The skill depends on external API responses and article content that may include HTML or unavailable dates. <br>
Mitigation: Validate API status codes, handle empty results, and strip or sanitize HTML before presenting article details. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/ai-news) <br>
- [Daily news API endpoint](https://api.cjiot.cc/api/v1/daily?date={current_date}) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown or JSON news summaries and article details] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include API calls to external news endpoints; article detail content may require HTML stripping.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
