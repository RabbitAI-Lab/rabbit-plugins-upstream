## Description: <br>
Fetches and displays BBC News stories from selected sections and regions via RSS feeds. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ddrayne](https://clawhub.ai/user/ddrayne) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and agent operators use this skill to retrieve BBC headlines and stories from selected BBC sections or regions in text or JSON form. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill runs a local script that makes outbound network requests to BBC RSS feed endpoints. <br>
Mitigation: Use it only in environments where agent-executed scripts and outbound access to BBC feed endpoints are allowed. <br>


## Reference(s): <br>
- [BBC News RSS Feeds](artifact/references/feeds.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON] <br>
**Output Format:** [Plain text headlines and story summaries, or a JSON array of story objects] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports selecting a BBC section or region and limiting the number of returned stories.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
