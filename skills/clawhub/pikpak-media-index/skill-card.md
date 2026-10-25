## Description:

Builds searchable Markdown or CSV indexes of PikPak video candidates, filters by known duration or resolution, redacts source URLs, and leaves unknown metadata unknown.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pipiguai87-alt](https://clawhub.ai/user/pipiguai87-alt)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can inventory an authorized PikPak media library and create searchable video catalogs or filter by duration and resolution. The skill reads listings only; it does not fetch media or probe files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Index reports contain private metadata; redacting source URLs does not remove the sensitivity of names, paths, and source identifiers.

Mitigation: Use a trusted PikPak CLI, choose a narrower folder when appropriate, and keep generated reports private.

Risk: Compatibility with live PikPak CLI raw JSON is unverified.

Mitigation: Use fixtures or mocks for development and verify live CLI behavior before relying on an index.

## Reference(s):

- [PikPak connected-app speed limits](https://mypikpak.com/zh-CN/help-center/connected_apps/webdav/speed_limit)
- [PikPak connected-app transfer quota](https://mypikpak.com/zh-CN/help-center/transfer_quota/connected_apps_quota)

## Skill Output:

**Output Type(s):** [Markdown, CSV]

**Output Format:** [Markdown table or CSV file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scalar metadata only; missing fields remain unknown; source URLs are redacted, but names, paths, and identifiers can remain sensitive.]

## Skill Version(s):

1.0.9 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
