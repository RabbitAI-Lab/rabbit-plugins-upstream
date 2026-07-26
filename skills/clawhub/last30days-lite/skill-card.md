## Description: <br>
Research any topic across Reddit, X/Twitter, and the web from the last 30 days. Synthesizes findings into actionable insights or copy-paste prompts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dylanbaker24](https://clawhub.ai/user/dylanbaker24) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to research recent discussion and practical sentiment about fast-moving topics across web search, Reddit, and X/Twitter. It is useful for prompt research, trend discovery, product feedback, and generating concise copy-paste prompts based on current findings. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Research topics may be sent to web search, Reddit search results, and optionally X/Twitter through the local bird CLI. <br>
Mitigation: Avoid confidential or sensitive topics, and use the skill only when sending the topic to those services is acceptable. <br>
Risk: X/Twitter searches may use the local bird CLI with an account or cookies configured in the environment. <br>
Mitigation: Review which X/Twitter account or cookies bird uses before running X/Twitter searches. <br>
Risk: The workflow may be invoked for recent-topic research where the user did not intend to query external services. <br>
Mitigation: Prefer explicit /last30days usage when this research workflow is desired. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/dylanbaker24/skills/last30days-lite) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown research synthesis with source links and optional copy-paste prompt] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include web, Reddit, and X/Twitter findings from the last 30 days; X/Twitter coverage depends on local bird CLI availability and account or cookie configuration.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
