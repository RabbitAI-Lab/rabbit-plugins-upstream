## Description: <br>
Queries Zhihuiya (PatSnap) for a single patent's current legal standing, validity status, and legal event history by patent ID or publication number. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Patent professionals, legal operations teams, and agents use this skill to check a single patent's legal status, validity, and legal events through the LinkFox Zhihuiya/PatSnap endpoint. It is suited for direct patent status lookups, not broader patent search, valuation, freedom-to-operate analysis, or family/citation analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends patent identifiers and query context to LinkFox/Zhihuiya services. <br>
Mitigation: Use only when sharing the patent query with those services is acceptable, and avoid confidential patent work unless the environment's data-handling controls are appropriate. <br>
Risk: Full API responses and cache files can persist locally under linkfox output directories. <br>
Mitigation: Review and manage local output/cache files, especially in shared workspaces or when query results may be sensitive. <br>
Risk: The security review notes silent feedback reporting and remote onboarding installation behavior. <br>
Mitigation: Review before installing and control feedback/onboarding behavior in the target environment. <br>
Risk: The endpoint consumes credits and supports only one patent per request. <br>
Mitigation: Confirm user intent before additional or repeated lookups, especially for multiple patents or retry attempts. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-zhihuiya-legal-status) <br>
- [API reference](artifact/references/api.md) <br>
- [Zhihuiya legal status endpoint](https://tool-gateway.linkfox.com/zhihuiya/legalStatus) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, Files, JSON, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Structured patent legal-status guidance with JSON API responses saved locally and optional stdout JSON or summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Queries one patent per request; responses may be cached for 24 hours and full API responses are written under a local linkfox session data directory.] <br>

## Skill Version(s): <br>
1.0.5 (source: evidence.release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
