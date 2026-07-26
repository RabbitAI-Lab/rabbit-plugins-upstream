## Description: <br>
YouTube Data API v3 analytics toolkit for analyzing channels, videos, search results, engagement metrics, and competitor comparisons using a YouTube Data API key. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[adamkristopher](https://clawhub.ai/user/adamkristopher) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to fetch public YouTube Data API v3 channel, video, and search metrics, compare channels, analyze engagement, and create local JSON results plus Markdown summaries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Saved YouTube queries, channel and video metadata, and generated summaries may remain on disk under results/. <br>
Mitigation: Use the skill only in a workspace where those saved results may persist, avoid sharing the results directory, and delete saved results when they are no longer needed. <br>
Risk: A YouTube Data API key stored in .env could be exposed if credentials are shared or committed. <br>
Mitigation: Use a restricted YouTube Data API key and keep the .env file private. <br>


## Reference(s): <br>
- [API Reference](references/api-reference.md) <br>
- [Google Cloud Console API Credentials](https://console.cloud.google.com/apis/credentials) <br>


## Skill Output: <br>
**Output Type(s):** [Code, Shell commands, Configuration, JSON, Markdown, Guidance] <br>
**Output Format:** [Markdown guidance with TypeScript examples, shell commands, and saved JSON or Markdown artifacts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires YOUTUBE_API_KEY and writes fetched results under results/.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and scripts/package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
