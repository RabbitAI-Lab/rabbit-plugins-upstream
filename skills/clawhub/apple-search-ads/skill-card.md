## Description: <br>
Plans, launches, and optimizes Apple Search Ads campaigns for iOS apps, including bids, keywords, budgets, CPA, attribution, API automation, and campaign troubleshooting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers, growth marketers, and iOS app teams use this skill to plan and operate Apple Search Ads campaigns, automate reporting and campaign changes, troubleshoot performance problems, and integrate AdServices or SKAdNetwork attribution. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can make real Apple Ads campaign and spend changes when credentials are provided, and may skip prompts if confirm_before_push is disabled. <br>
Mitigation: Keep confirm_before_push true, review every proposed API mutation, and only use credentials for ad accounts you control. <br>
Risk: Apple Ads credentials and private keys are required for API automation. <br>
Mitigation: Provide credentials via environment variables and key files only; do not store real secrets in credentials.md or skill memory. <br>
Risk: Attribution token or raw attribution payload logging can expose sensitive advertising data. <br>
Mitigation: Avoid logging attribution tokens or raw attribution payloads, and limit IDFA access to cases with a clear compliance basis. <br>
Risk: The included shell automation needs review before operational use. <br>
Mitigation: Review or rewrite shell scripts with safe JSON construction and test against non-critical campaigns first. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/ivangdavila/skills/apple-search-ads) <br>
- [Clawic Skill Homepage](https://clawic.com/skills/apple-search-ads) <br>
- [Apple Ads Campaign Management API v5](https://api.searchads.apple.com/api/v5) <br>
- [Apple OAuth Token Endpoint](https://appleid.apple.com/auth/oauth2/token) <br>
- [Apple AdServices API](https://api-adservices.apple.com/api/v1/) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration, API calls] <br>
**Output Format:** [Markdown guidance with code snippets, shell commands, JSON payloads, and configuration notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May generate or suggest Apple Ads API calls and local report/config files; spend-changing actions should remain confirmed before execution.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
