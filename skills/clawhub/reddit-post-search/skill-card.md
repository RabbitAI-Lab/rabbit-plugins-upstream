## Description: <br>
Extracts Reddit posts from keyword search, subreddit browsing, or direct Reddit URLs and returns structured JSON records with post metadata, engagement metrics, media fields, pagination state, and filtering controls. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[browseract-cli](https://clawhub.ai/user/browseract-cli) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and analysts use this skill to collect Reddit post records for search, subreddit monitoring, content analysis, or pipeline ingestion from Reddit pages available in the user's browser context. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill contacts Reddit directly through Reddit JSON API requests from the user's browser context. <br>
Mitigation: Use it only for explicit Reddit collection tasks and confirm the user is comfortable with external Reddit requests before execution. <br>
Risk: Large or repeated collections may encounter Reddit rate limits. <br>
Mitigation: Throttle pagination requests and use the documented 1-2 second delay guidance for batch runs. <br>
Risk: The skill may keep limited local troubleshooting notes when unexpected execution issues occur. <br>
Mitigation: Review local memory-file behavior before use in environments that restrict persistent workspace notes. <br>
Risk: Results can include NSFW posts when explicitly enabled. <br>
Mitigation: Keep NSFW inclusion disabled unless the task requires it and the environment permits that content. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/browseract-cli/skills/reddit-post-search) <br>
- [Publisher Profile](https://clawhub.ai/user/browseract-cli) <br>
- [Reddit JSON API endpoints](https://www.reddit.com/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, JSON] <br>
**Output Format:** [Markdown guidance with bash command templates that return JSON post records] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces paginated post arrays with an after cursor, count, has_more flag, and derived engagement fields.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
