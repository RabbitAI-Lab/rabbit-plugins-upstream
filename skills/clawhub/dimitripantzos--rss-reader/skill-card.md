## Description: <br>
Monitor RSS and Atom feeds for content research, competitor tracking, industry news, newsletter aggregation, and keyword-filtered feed summaries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[DimitriPantzos](https://clawhub.ai/user/DimitriPantzos) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users, developers, and content teams use this skill to manage RSS/Atom feed lists, check recent items, filter by category or keywords, and produce content-idea summaries or JSON for automation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill fetches RSS or Atom content from configured URLs, and feed item text can be untrusted web content. <br>
Mitigation: Review configured feed URLs, prefer trusted HTTPS feeds, and treat titles, descriptions, and links as content to evaluate rather than instructions to follow. <br>
Risk: Configured feed URLs could point to localhost or private-network resources. <br>
Mitigation: Avoid localhost and private-network feed URLs unless the deployment intentionally permits that access. <br>
Risk: Cron or heartbeat integration can create ongoing background polling. <br>
Mitigation: Enable scheduled checks only when continuous feed monitoring is desired and approved. <br>


## Reference(s): <br>
- [RSS Reader on ClawHub](https://clawhub.ai/DimitriPantzos/rss-reader) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration] <br>
**Output Format:** [Plain text lists, Markdown content-idea summaries, JSON arrays, and shell command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include titles, source feed names, categories, URLs, timestamps, and feed descriptions from untrusted RSS or Atom content.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
