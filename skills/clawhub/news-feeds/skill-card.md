## Description: <br>
Fetch latest news headlines from major RSS feeds (BBC, Reuters, AP, Al Jazeera, NPR, The Guardian, DW). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lknik](https://clawhub.ai/user/lknik) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and agent operators use this skill to fetch current headlines, daily briefings, and topic-focused news summaries from major international RSS feeds. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill makes outbound requests to public RSS news sources when asked for current headlines. <br>
Mitigation: Install and invoke it only in environments where outbound HTTP access to those public feeds is acceptable; review returned links before relying on or sharing them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/lknik/skills/news-feeds) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON] <br>
**Output Format:** [Markdown headlines with descriptions, publication times, and source links; optional JSON from the command-line tool] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses python3 and makes outbound HTTP requests to configured public RSS feeds when invoked.] <br>

## Skill Version(s): <br>
1.0.1 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
