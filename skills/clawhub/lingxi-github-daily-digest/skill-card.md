## Description: <br>
Monitors GitHub Trending daily, uses AI to analyze prominent projects, and produces a formatted digest with topic tags, star-growth prediction, and recommendations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nima54851](https://clawhub.ai/user/nima54851) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, investors, and technology analysts use this skill to track GitHub Trending projects, filter by language or time range, and receive an AI-generated daily Markdown digest for open-source trend monitoring. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Scheduled runs can create recurring local digest files in ~/github-digest without automatic retention controls. <br>
Mitigation: Decide whether scheduled local file creation is desired before installing, and manage cleanup or retention for saved reports. <br>
Risk: Using a broad GITHUB_TOKEN can expose unnecessary account permissions for public repository metadata collection. <br>
Mitigation: Use the least-privilege token needed for public repository metadata, or omit the token when higher rate limits are not required. <br>


## Reference(s): <br>
- [Skill instructions](artifact/SKILL.md) <br>
- [ClawHub skill page](https://clawhub.ai/nima54851/skills/lingxi-github-daily-digest) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown digest with tables, rankings, topic summaries, insights, recommendations, and optional shell or configuration snippets.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can save scheduled reports to ~/github-digest/YYYY-MM-DD.md when configured.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
