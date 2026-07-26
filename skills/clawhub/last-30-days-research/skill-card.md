## Description: <br>
Searches Reddit, X/Twitter, and the broader web for recent opinions, sentiment, and signal on a topic and produces a structured report with consensus findings, pain points, positive signals, source links, and signal confidence. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mohitagw15856](https://clawhub.ai/user/mohitagw15856) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, product teams, and researchers use this skill to collect recent public community sentiment about a product, trend, event, company, or tool across Reddit, X/Twitter, and independent web sources. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Research topics may be sent to public platforms and search providers during web searches. <br>
Mitigation: Sanitize queries and avoid secrets, internal codenames, private incidents, personal data, or confidential business topics. <br>
Risk: Social and community sentiment can be sparse, fragmented, or misleading if treated as definitive evidence. <br>
Mitigation: Preserve source links, apply the stated date window and corroboration checks, and use the signal confidence rating to guide review. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/mohitagw15856/skills/last-30-days-research) <br>
- [Skill homepage](https://mohitagw15856.github.io/pm-claude-skills/skill/last-30-days-research.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Analysis, Guidance] <br>
**Output Format:** [Structured Markdown report with source links, consensus findings, disagreements, pain points, positive signals, notable takes, and a signal confidence rating] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses public web searches and should be run with sanitized, non-confidential topics; readers should verify linked sources and confidence ratings before relying on findings.] <br>

## Skill Version(s): <br>
50.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
