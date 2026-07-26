## Description: <br>
China News aggregates Chinese-source news and returns news lists, summaries, categories, metadata, and execution status. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use China News to collect Chinese news by date, channel, keyword, or source, then return news items, summaries, category tags, and processing status. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security review flags that the skill presents as a China news helper while also activating for coding and deployment workflows and declaring command execution. <br>
Mitigation: Restrict activation to news use cases and remove or tightly bound command execution before normal installation. <br>
Risk: The artifact includes API key setup guidance. <br>
Mitigation: Use scoped credentials and keep API keys out of version control, shared transcripts, and generated outputs. <br>
Risk: News aggregation and summarization can produce incomplete or misleading summaries. <br>
Mitigation: Review source coverage, dates, and source links before relying on summaries for consequential decisions. <br>


## Reference(s): <br>
- [China News ClawHub page](https://clawhub.ai/thcjp/skills/china-news) <br>
- [Skill homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, shell commands, guidance] <br>
**Output Format:** [JSON or Markdown summaries with optional shell configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include news results, metadata, status, execution logs, retry counts, and quality-gate counts.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release metadata; artifact frontmatter reports 1.0.4) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
