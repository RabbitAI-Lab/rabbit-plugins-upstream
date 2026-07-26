## Description: <br>
Full access to Moon Banking API endpoints for data about every bank on Earth, including stories, votes, scores, search, country overviews, world overview, crypto-friendliness, and more. Requires MOON_BANKING_API_KEY env var. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[juanwall](https://clawhub.ai/user/juanwall) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to query Moon Banking for bank, country, story, vote, search, and global banking overview data. It helps agents produce banking comparisons, rankings, lookup summaries, and API-backed guidance when a Moon Banking API key is available. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses MOON_BANKING_API_KEY to make requests to the Moon Banking API. <br>
Mitigation: Install it only when the publisher and API provider are trusted, keep the API key secret, and scope access according to the Moon Banking account's needs. <br>
Risk: Free-form banking searches can send user-provided details to Moon Banking. <br>
Mitigation: Ask for explicit Moon Banking lookups and avoid including private financial details unless the user intends to send them to that provider. <br>
Risk: Broad activation wording may make the skill relevant to many banking-related questions. <br>
Mitigation: Use the skill when API-backed Moon Banking data is needed, and summarize returned data rather than treating it as independent financial advice. <br>


## Reference(s): <br>
- [Moon Banking OpenClaw Skill Documentation](https://docs.moonbanking.com/openclaw-skill) <br>
- [Moon Banking API Base URL](https://api.moonbanking.com/v1) <br>
- [Moon Banking ClawHub Skill Page](https://clawhub.ai/juanwall/skills/moonbanking) <br>
- [Moon Banking Pro Plan](https://moonbanking.com/pro) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and summarized JSON results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires MOON_BANKING_API_KEY; uses curl and jq when available.] <br>

## Skill Version(s): <br>
1.1.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
