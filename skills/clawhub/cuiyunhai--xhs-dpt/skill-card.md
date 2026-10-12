## Description:

Collects likes, saves, comments, and shares for batches of public Xiaohongshu notes and exports the results as CSV.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cuiyunhai](https://clawhub.ai/user/cuiyunhai)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing analysts and other users collect engagement counts from batches of public Xiaohongshu notes for campaign reporting and content analysis. A paid third-party service requires an account and note links containing xsec_token.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The default service connection sends account tokens over unencrypted HTTP.

Mitigation: Set an HTTPS base URL with a valid certificate before login when available; avoid using the default connection on untrusted networks.

Risk: Login tokens persist locally and an older token may be reused automatically.

Mitigation: Review and remove ~/.xhs-platform/config.json and legacy ~/.xhs-convert/config.json tokens if credential reuse is unwanted.

Risk: Enabling insecure TLS disables HTTPS certificate verification.

Mitigation: Leave insecure TLS disabled except for tightly controlled testing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/cuiyunhai/skills/xhs-dpt)

## Skill Output:

**Output Type(s):** [Text, Markdown, CSV files]

**Output Format:** [Markdown summaries of engagement metrics; UTF-8 CSV exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Missing engagement values are not zero; comment text is not collected.]

## Skill Version(s):

1.1.1 (source: skill frontmatter, package.json, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
