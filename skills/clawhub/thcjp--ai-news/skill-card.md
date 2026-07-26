## Description: <br>
Ai News helps an agent fetch daily news summaries, ranked headlines, category-filtered news, and article details from a third-party news API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to retrieve current or date-specific news, browse ranked headlines, filter by category, and read article details. It is intended for news retrieval and summarization, not database or SQL operations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill makes network requests to a third-party news API and grants shell execution for those requests. <br>
Mitigation: Install only in environments where outbound requests to the listed news API are acceptable, and review generated commands before execution. <br>
Risk: The release evidence reports unrelated database and SQL trigger text in the skill description. <br>
Mitigation: Use the skill only for news retrieval until the publisher narrows the description to news-only usage and removes the database and SQL wording. <br>
Risk: Article details may include HTML content from the upstream API. <br>
Mitigation: Strip or safely render HTML before presenting article details to users. <br>


## Reference(s): <br>
- [SkillHub homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown or JSON-style news summaries and article details, with shell commands used for API requests.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include dates, ranked headlines, categories, article summaries, article body text, and API error guidance.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
