## Description: <br>
Google Docs API integration with managed OAuth for creating documents, inserting text, applying formatting, and managing document content. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[byungkyu](https://clawhub.ai/user/byungkyu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to access Google Docs through Maton's managed OAuth proxy for document reads, creation, text insertion, formatting, and batch updates. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Google Docs document content and requests are routed through Maton's API proxy. <br>
Mitigation: Use only the Google account intended for the task and avoid sending content that should not be processed through Maton. <br>
Risk: MATON_API_KEY grants access through the connected Maton account. <br>
Mitigation: Store MATON_API_KEY as a secret, rotate it if exposed, and do not paste it into chat or logs. <br>
Risk: Write or delete operations can change Google Docs content. <br>
Mitigation: Confirm the target document, selected connection, and intended change before approving any create, update, or delete action. <br>
Risk: Multiple Google Docs connections can cause requests to affect the wrong account. <br>
Mitigation: Specify the intended connection ID whenever more than one Google Docs connection is active. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/google-docs) <br>
- [Google Docs API overview](https://developers.google.com/docs/api/how-tos/overview) <br>
- [Get document](https://developers.google.com/docs/api/reference/rest/v1/documents/get) <br>
- [Create document](https://developers.google.com/docs/api/reference/rest/v1/documents/create) <br>
- [Batch update](https://developers.google.com/docs/api/reference/rest/v1/documents/batchUpdate) <br>
- [Request types](https://developers.google.com/docs/api/reference/rest/v1/documents/request) <br>
- [Document structure](https://developers.google.com/docs/api/concepts/structure) <br>
- [Maton CLI manual](https://cli.maton.ai/manual) <br>
- [Maton community](https://discord.com/invite/dBfFAcefs2) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Code, Configuration instructions] <br>
**Output Format:** [Markdown with inline shell, Python, JavaScript, and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires network access, MATON_API_KEY, and a Google Docs OAuth connection through Maton.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
