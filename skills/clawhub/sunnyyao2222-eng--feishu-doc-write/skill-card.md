## Description:

Feishu (Lark) Document API writing spec. Converts Markdown content to Feishu Block structures and writes to cloud docs. Handles concurrency ordering. Use when syncing articles, creating document blocks, or writing long-form content to Feishu docs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sunnyyao2222-eng](https://clawhub.ai/user/sunnyyao2222-eng)

### License/Terms of Use:


## Use Case:

Developers and engineers use this skill to guide agents that convert Markdown or long-form content into Feishu Docx block structures and write them to Feishu cloud documents while preserving ordering.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Feishu app secrets and access tokens could be exposed if real credentials are pasted into shared logs, prompts, or shell history.

Mitigation: Use environment variables or a secret manager, redact credentials from logs, and rotate any token or secret that may have been exposed.

Risk: API write examples can modify Feishu documents or folders the user did not intend to change.

Mitigation: Confirm the target document, folder, permissions, and tenant before issuing write requests.

Risk: Concurrent block creation can produce unexpected document ordering.

Mitigation: Prefer one batch write for the full block array, or serialize multi-request writes with explicit indexes.

## Reference(s):

- [Feishu Create Blocks API](https://open.feishu.cn/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/document-docx/docx-v1/document-block-children/create)
- [Feishu Block Data Structure](https://open.feishu.cn/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/document-docx/docx-v1/data-structure/block)
- [Feishu Markdown Convert API](https://open.feishu.cn/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/document-docx/docx-v1/document/convert)
- [Feishu App Access Token API](https://open.feishu.cn/open-apis/auth/v3/app_access_token/internal)

## Skill Output:

**Output Type(s):** [Guidance, Code, API Calls, Configuration instructions]

**Output Format:** [Markdown with JSON and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces Feishu Docx block mappings, API request examples, ordering guidance, and authentication notes.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
