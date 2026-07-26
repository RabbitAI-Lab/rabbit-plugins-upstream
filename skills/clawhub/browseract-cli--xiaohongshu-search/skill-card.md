## Description: <br>
Searches Xiaohongshu (RedNote / xhs) notes by keyword and returns paginated result data including titles, authors, engagement counts, cover image URLs, and xsecToken values for detail lookup. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[browseract-cli](https://clawhub.ai/user/browseract-cli) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to collect Xiaohongshu search result lists from a normal logged-in browser session for content discovery, monitoring, or follow-up detail lookup. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security review reports suspicious guidance around scaled scraping with stealth sessions and independent fingerprints. <br>
Mitigation: Use only low-volume, user-directed searches in a normal logged-in browser session and avoid stealth-session, fingerprint, and batch-scaling guidance. <br>
Risk: Search extraction depends on the user's Xiaohongshu login state and data visible in the browser. <br>
Mitigation: Do not attempt to bypass authentication or access controls; stop if the user cannot or will not log in. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/browseract-cli/skills/xiaohongshu-search) <br>
- [Xiaohongshu web search](https://www.xiaohongshu.com/search_result/?keyword={keyword}) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, shell commands, guidance] <br>
**Output Format:** [JSON result data with browser interaction guidance and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns visible search result fields from the current browser session, with pagination controlled by scrolling and a configurable result limit.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
