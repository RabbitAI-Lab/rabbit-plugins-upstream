## Description: <br>
Track Meta (Facebook/Instagram) ad creative performance and hit rates across multiple accounts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fortytwode](https://clawhub.ai/user/fortytwode) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Performance marketing teams and agents use this skill to report Meta Ads creative hit rates, compare creatives across accounts and time periods, and identify ads meeting configured CPT, CPI, IPM, or ROAS benchmarks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a user-provided Meta access token to read advertising performance data for configured accounts. <br>
Mitigation: Use a least-privileged Meta access token and store credentials in environment variables or a secret manager. <br>
Risk: Performance data may be cached locally in SQLite. <br>
Mitigation: Limit local access to the workspace and review cached data retention before using the skill with sensitive client accounts. <br>


## Reference(s): <br>
- [Meta Ad Creatives on ClawHub](https://clawhub.ai/fortytwode/skills/meta-ad-creatives) <br>
- [Meta Graph API endpoint](https://graph.facebook.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, code, configuration, guidance] <br>
**Output Format:** [Markdown guidance with Python examples and JSON configuration] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs ad performance summaries, hit-rate metrics, creative-level reports, and month-over-month comparisons based on configured Meta Ads accounts.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
