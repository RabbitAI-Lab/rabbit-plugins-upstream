## Description:

Select a document release.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Document teams use this skill to select an eligible release using supplied version guidance and record the selection locally.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The local selection record may contain private release data supplied in the request.

Mitigation: Use a dedicated output directory and omit private release data unless it is intended for the local record.

## Reference(s):

- [Document Release Selector on ClawHub](https://clawhub.ai/wxt-ai/skills/draft-precedence-guidance-workbench)

## Skill Output:

**Output Type(s):** [JSON, Markdown]

**Output Format:** [JSON selection result and local Markdown record]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns selected_version, eligible_versions, and reason, plus a receipt for the local record.]

## Skill Version(s):

1.1.0 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
