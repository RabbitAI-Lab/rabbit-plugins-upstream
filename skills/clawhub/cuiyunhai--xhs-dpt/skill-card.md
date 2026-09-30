## Description:

Collects engagement counts for public Xiaohongshu notes in batches and exports the results as CSV.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cuiyunhai](https://clawhub.ai/user/cuiyunhai)

### License/Terms of Use:

MIT-0

## Use Case:

Social media analysts and marketing teams use this skill to gather likes, saves, comments, and shares for batches of public Xiaohongshu notes, monitor campaign performance, and export results for reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The default service endpoint sends account tokens and submitted note links over plaintext HTTP.

Mitigation: Use a working HTTPS service URL and avoid the default HTTP endpoint on untrusted networks.

Risk: A reusable account token is stored locally and an older related token may be migrated automatically.

Mitigation: Protect the local configuration file, check any migrated credentials, and use a one-time token override when migration is unwanted.

Risk: Disabling HTTPS certificate verification exposes service credentials to interception.

Mitigation: Keep insecure TLS disabled and use a valid service certificate.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/cuiyunhai/skills/xhs-dpt)

## Skill Output:

**Output Type(s):** [Text, CSV files]

**Output Format:** [JSON task results, Markdown summaries, and CSV exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Engagement counts may be missing rather than zero; comment content is not collected.]

## Skill Version(s):

1.1.0 (source: frontmatter, package.json, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
