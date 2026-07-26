## Description: <br>
Xiaohongshu Search helps agents collect Xiaohongshu search results, notes, user posts, and comments through agent-browser using user-provided login cookies. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[excalibursssooo](https://clawhub.ai/user/excalibursssooo) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agents use this skill to gather Xiaohongshu content from keywords, note IDs, or user profiles and produce local reports for review. It is intended for authenticated workflows where the user provides Xiaohongshu session cookies. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill relies on sensitive Xiaohongshu session cookies stored in local files. <br>
Mitigation: Keep cookie, state, token cache, and data directories private, use restrictive file permissions, and do not commit or share those files. <br>
Risk: The skill saves scraped posts, comments, and related harvest artifacts on disk. <br>
Mitigation: Review platform rules and privacy implications before collection, limit collection to appropriate use cases, and control access to harvest directories. <br>
Risk: Repeated browser-driven collection can trigger Xiaohongshu captcha or IP risk controls. <br>
Mitigation: Respect the documented rate limits, stop rather than retrying through captcha or IP-risk errors, and rerun only after the account or network state is acceptable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/excalibursssooo/xiaohongshu-search) <br>
- [Project homepage](https://github.com/excalibursssooo/xiaohongshu-search) <br>
- [README](README.md) <br>
- [Pitfalls guide](docs/pitfalls.md) <br>
- [Known issues](KNOWN_ISSUES.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, JSON, Files, Shell commands, Guidance] <br>
**Output Format:** [Markdown reports, JSON data files, and shell command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes local harvest directories under data/harvests and uses user-provided Xiaohongshu cookies.] <br>

## Skill Version(s): <br>
1.4.1 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
