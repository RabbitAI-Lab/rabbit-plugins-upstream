## Description: <br>
Manages Amazon Store A+ Content documents through LinkFox and Amazon SP-API A+ Content Management v2020-11-01, including search, create, get, update, ASIN relations, validation, publish records, approval submission, and suspend submission. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External sellers, marketplace operators, and their agents use this skill to manage authorized Amazon A+ Content documents and their ASIN relationships. It supports operational workflows for inspecting content, preparing updates, validating document-to-ASIN eligibility, submitting content for approval, reviewing publish records, and suspending front-end display. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create, update, submit, suspend, or replace ASIN relations for live Amazon A+ Content. <br>
Mitigation: Use it only in private authorized workspaces, require explicit user confirmation before write actions, and review contentReferenceKey, marketplaceId, and the full asinSet before execution. <br>
Risk: Full API responses may be saved locally and can include sensitive storefront data. <br>
Mitigation: Inspect and protect files written under linkfox session directories, and remove or restrict access to saved responses when no longer needed. <br>
Risk: ASIN replacement is full-set replacement, so omitting existing ASINs can suspend content for those ASINs. <br>
Mitigation: Submit the complete intended asinSet and verify current associations before replacing them. <br>


## Reference(s): <br>
- [Amazon Store A+ Content Management API Reference](references/api.md) <br>
- [Amazon SP-API searchContentDocuments](https://developer-docs.amazon.com/sp-api/reference/searchcontentdocuments) <br>
- [Amazon SP-API createContentDocument](https://developer-docs.amazon.com/sp-api/reference/createcontentdocument) <br>
- [Amazon SP-API getContentDocument](https://developer-docs.amazon.com/sp-api/reference/getcontentdocument) <br>
- [Amazon SP-API updateContentDocument](https://developer-docs.amazon.com/sp-api/reference/updatecontentdocument) <br>
- [Amazon SP-API postContentDocumentAsinRelations](https://developer-docs.amazon.com/sp-api/reference/postcontentdocumentasinrelations) <br>
- [Amazon SP-API validateContentDocumentAsinRelations](https://developer-docs.amazon.com/sp-api/reference/validatecontentdocumentasinrelations) <br>
- [Amazon SP-API searchContentPublishRecords](https://developer-docs.amazon.com/sp-api/reference/searchcontentpublishrecords) <br>
- [Amazon SP-API postContentDocumentApprovalSubmission](https://developer-docs.amazon.com/sp-api/reference/postcontentdocumentapprovalsubmission) <br>
- [Amazon SP-API postContentDocumentSuspendSubmission](https://developer-docs.amazon.com/sp-api/reference/postcontentdocumentsuspendsubmission) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON API responses saved to local files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Scripts write full API responses under linkfox/<date>/<session>/data and print full or summarized JSON to stdout.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
