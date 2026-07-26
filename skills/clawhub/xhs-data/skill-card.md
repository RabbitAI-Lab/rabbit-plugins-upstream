## Description: <br>
Collects public Xiaohongshu note, profile, search, comment, and media data using API and browser automation workflows. <br>

This skill is for research and development only. <br>

## Publisher: <br>
[cooperiano](https://clawhub.ai/user/cooperiano) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and researchers use this skill to guide agents through Xiaohongshu data collection tasks such as note metadata extraction, user page crawling, keyword search, comment retrieval, and media download. Users should apply it only to authorized public-content collection and manage locally saved data responsibly. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Xiaohongshu scraping may be disallowed for some use cases or may collect private or sensitive personal content if misused. <br>
Mitigation: Confirm the collection is permitted, fetch only public content, and avoid collecting private or sensitive personal information. <br>
Risk: Logged-in sessions, proxy use, and saved local data can create account, privacy, and retention exposure. <br>
Mitigation: Use only necessary sessions and proxies, protect session material, and periodically review or delete saved data under ~/disk/xiaohongshu. <br>
Risk: High-volume collection can trigger anti-scraping controls or create unreliable results. <br>
Mitigation: Respect the documented delay and per-user limits, back off on access errors, and stop collection when authorization or rate limits are unclear. <br>


## Reference(s): <br>
- [Xhs Data ClawHub skill page](https://clawhub.ai/cooperiano/skills/xhs-data) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with Python and bash examples; workflows may save JSON, Markdown, HTML, images, and videos locally.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are organized under ~/disk/xiaohongshu and include rate-limit, public-content, and per-item media-count guidance.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
