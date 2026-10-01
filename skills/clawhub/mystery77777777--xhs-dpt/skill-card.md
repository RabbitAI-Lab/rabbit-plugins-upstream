## Description:

xhs-dpt helps agents submit Xiaohongshu note links and retrieve public engagement metrics such as likes, saves, comments, shares, note titles, and note IDs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mystery77777777](https://clawhub.ai/user/mystery77777777)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to collect public Xiaohongshu note engagement data in batches for campaign reporting, social media index tracking, activity monitoring, popular content analysis, and KOL analysis. It can return task results as JSON or export CSV files for spreadsheet review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The default service URL uses plain HTTP, which can expose submitted note links, xsec_token URL parameters, and bearer tokens in transit.

Mitigation: Configure a working HTTPS base URL before login or submission when available, and avoid using the skill on untrusted networks.

Risk: The local configuration file stores an account token used by the service.

Mitigation: Protect ~/.xhs-platform/config.json as a credential, do not share or commit it, and use XHS_CONFIG_PATH for isolated test configurations.

Risk: Disabling HTTPS certificate validation can increase man-in-the-middle exposure.

Mitigation: Use insecure TLS settings only for controlled testing against known endpoints, and prefer valid HTTPS certificates for normal use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mystery77777777/skills/xhs-dpt)

## Skill Output:

**Output Type(s):** [JSON, CSV files, Shell commands, Configuration, Guidance]

**Output Format:** [CLI stdout JSON with optional CSV exports and concise agent-facing guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 18 or newer, authenticated service access, and Xiaohongshu note URLs with xsec_token parameters.]

## Skill Version(s):

1.0.0 (source: frontmatter, package.json, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
