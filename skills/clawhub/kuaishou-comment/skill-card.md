## Description: <br>
Kuaishou Comment Analysis fetches paginated Kuaishou video comments, summarizes sentiment across positive, negative, demand, and competitor dimensions, and can generate HTML reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[redfox-data](https://clawhub.ai/user/redfox-data) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Creators, brand operators, MCNs, and data analysts use this skill to inspect Kuaishou video comments, track audience sentiment, monitor competitor mentions, and export browsed comments into visual reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a RedFox API key and sends Kuaishou opus IDs to the RedFox API. <br>
Mitigation: Install only when comfortable sharing that key and request data with RedFox; verify key scope, expiration, and revocation before use. <br>
Risk: Fetched comments can include commenter metadata such as nickname, avatar URL, user ID, IP location, timestamps, likes, and replies. <br>
Mitigation: Avoid exporting or sharing reports that contain sensitive commenter metadata unless there is a clear need and appropriate approval. <br>
Risk: Generated HTML reports are built from external comment data and can be opened locally in a browser. <br>
Mitigation: Treat generated HTML as untrusted content and review reports before sharing or opening them in sensitive environments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/redfox-data/skills/kuaishou-comment) <br>
- [Server-resolved GitHub source](https://github.com/redfox-data/redfox-community/tree/main/skills/kuaishou-comment) <br>
- [RedFoxHub API key settings](https://redfox.hk/settings/api-keys?source=github) <br>
- [RedFoxHub](https://redfox.hk?source=github) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, analysis, shell commands, html files] <br>
**Output Format:** [Markdown responses with JSON-backed script output and generated HTML reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses one API request per fetched page and can merge multiple browsed pages into a local HTML report.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata and changelog) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
