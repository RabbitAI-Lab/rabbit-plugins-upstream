## Description: <br>
Fetch latest news headlines from major RSS feeds (BBC, Reuters, AP, Al Jazeera, NPR, The Guardian, DW). No API keys required. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lknik](https://clawhub.ai/user/lknik) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Agents and users use this skill to fetch current headlines, daily briefings, and topic-specific news summaries from configured public RSS feeds. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The package includes unrelated local permission settings that could allow broad Python commands and git staging or commits. <br>
Mitigation: Review or remove .claude/settings.local.json before installing; the news reader itself only needs python3 and outbound HTTP access to public RSS feeds. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/lknik/skills/news-feed) <br>
- [Artifact README](README.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json] <br>
**Output Format:** [Markdown grouped by source, with JSON available when requested] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3 and outbound HTTP access to configured public RSS feeds; no API keys are required.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
