## Description: <br>
Query Umami Cloud (v2) analytics data via API using an environment-provided API key. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hfichter](https://clawhub.ai/user/hfichter) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, marketers, analysts, and agent operators use this skill to fetch read-only Umami analytics for traffic, pages, events, sessions, realtime activity, reports, and attribution analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: An overbroad or admin-scoped Umami API key can expose more analytics data than the task requires. <br>
Mitigation: Use the narrowest Umami API key available and avoid admin-scoped keys unless the requested endpoint genuinely requires them. <br>
Risk: A misconfigured UMAMI_BASE_URL can send the API key to an untrusted service. <br>
Mitigation: Point UMAMI_BASE_URL only at Umami Cloud or a trusted self-hosted Umami instance before running queries. <br>
Risk: Broad or ambiguous analytics requests can return unnecessary traffic, session, event, or attribution data. <br>
Mitigation: Prefer explicit website IDs, endpoint paths, and time ranges, and handle returned JSON as potentially sensitive analytics data. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/hfichter/skills/umami-stats) <br>
- [Publisher profile](https://clawhub.ai/user/hfichter) <br>
- [Umami API documentation](https://v2.umami.is/docs/api) <br>
- [Umami read endpoints](artifact/references/read-endpoints.md) <br>
- [Query helper](artifact/scripts/umami_query.py) <br>
- [SKILL.md](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON API responses from the Umami query helper.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a user-provided UMAMI_API_KEY and supports explicit website IDs, path variables, query parameters, and time-range presets.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
