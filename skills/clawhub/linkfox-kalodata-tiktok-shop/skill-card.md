## Description: <br>
Uses Kalodata-backed data to browse TikTok Shop store leaderboards and fetch individual shop details, including GMV, sales volume, product counts, revenue channel split, and creator, video, and livestream counts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External ecommerce analysts, sellers, and operators use this skill to discover high-performing TikTok Shop stores by region and time window, then inspect a selected shop by shopId for sales, revenue, product, and channel metrics. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill saves full API responses, cache files, and session metadata locally, which may retain shop research data beyond the immediate task. <br>
Mitigation: Review where the linkfox session and cache directories are written, avoid running in sensitive workspaces when not needed, and clean saved JSON responses or session metadata after use. <br>
Risk: The skill sends request parameters and authentication headers to a LinkFox/Kalodata service and includes automatic feedback reporting behavior. <br>
Mitigation: Confirm what data is sent to the provider, whether feedback reporting can be disabled or governed, and whether the use aligns with the user's data-sharing requirements before installation. <br>
Risk: Each live lookup consumes paid credits, and repeated pagination or retries can increase cost. <br>
Mitigation: Use the built-in cache for identical parameters, keep page sizes and page numbers intentional, and ask the user before making additional paid calls. <br>


## Reference(s): <br>
- [Kalodata-TikTok店铺搜索与详情 API Reference](references/api.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-kalodata-tiktok-shop) <br>
- [Publisher Profile](https://clawhub.ai/user/linkfox-ai) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown summaries and tables, shell command examples, and saved JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Responses may be summarized when large; full JSON responses are saved under a session data directory, with 24-hour local caching for matching parameters.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
