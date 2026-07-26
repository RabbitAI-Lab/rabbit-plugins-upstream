## Description: <br>
Archive Free helps agents capture articles, webpages, videos, tweets, and PDFs as local Markdown snapshots with basic metadata, summaries, tags, and keyword search. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to collect research and personal knowledge materials into a local archive, then retrieve saved items by keyword or tag. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Archived content and metadata are saved persistently under ~/archive/. <br>
Mitigation: Avoid archiving private documents, secret-bearing URLs, or content that should not be retained locally; periodically review and remove archived files that are no longer needed. <br>
Risk: The optional callback_url may disclose processing status or archive-related metadata. <br>
Mitigation: Use callback URLs only from trusted endpoints and avoid callbacks for sensitive archive requests. <br>
Risk: The skill can propose shell commands for creating archive directories. <br>
Mitigation: Review shell commands before execution and confirm that paths point only to the intended local archive location. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/archive-free) <br>
- [SkillHub homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with JSON-style processing results and local file paths] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Archives are described as local Markdown files under ~/archive/.] <br>

## Skill Version(s): <br>
1.0.1 (source: server-resolved release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
