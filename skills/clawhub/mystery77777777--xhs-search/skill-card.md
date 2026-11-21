## Description:

Searches Xiaohongshu by keyword and returns filtered note metadata, with optional CSV export.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mystery77777777](https://clawhub.ai/user/mystery77777777)

### License/Terms of Use:

MIT-0

## Use Case:

External users can collect filtered Xiaohongshu search-result metadata for content research, competitor monitoring, creator screening, and category surveys.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The default service uses unencrypted HTTP, exposing the bearer token in transit; optional insecure TLS mode disables certificate verification.

Mitigation: Defer installation until token transport is protected. Use verified HTTPS, keep insecure TLS disabled, and protect the locally stored token.

Risk: The security summary flags collection and recharge capabilities beyond the stated search purpose, and only two of seven components were fully inspected.

Mitigation: Review and clearly explain or remove unnecessary collection and recharge capabilities, and complete inspection of the remaining components before installation.

## Reference(s):


## Skill Output:

**Output Type(s):** [JSON, CSV files]

**Output Format:** [JSON results on stdout; CSV file on export]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search-result note metadata; CSV exports are retained for seven days.]

## Skill Version(s):

1.0.1 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
