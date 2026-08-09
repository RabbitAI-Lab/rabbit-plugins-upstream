## Description:

Manages Amazon Store A+ Content documents through LinkFox, including search, create, read, update, ASIN relations, validation, publish-record search, approval submission, and suspend submission workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators managing Amazon seller storefront content use this skill to inspect and change A+ Content through LinkFox-backed Amazon SP-API workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create, update, submit, suspend, or replace ASIN relations for Amazon A+ content.

Mitigation: Confirm sellerId, region, marketplaceId, contentReferenceKey, ASIN set, and user intent before write, submit, suspend, or replacement operations.

Risk: The skill handles LinkFox API keys, account setup, API-key recovery, and payment flows.

Mitigation: Use self-service account and billing pages when possible, avoid exposing API keys in logs or chat history, and review any payment details before acting.

Risk: Configured LINKFOX_* endpoint values or compatible gateway environment variables affect where API requests are sent.

Mitigation: Verify LINKFOX_* endpoint values and STORE_API_BASE_URL or SPAPI_BASE_URL before use.

Risk: Scripts save complete API responses under linkfox/ in the working directory.

Mitigation: Review or delete saved response files after use, and avoid inline full-response output when responses may contain sensitive store data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-amazon-store-aplus-content)
- [Amazon Store A+ Content Management API reference](artifact/references/api.md)
- [LinkFox authentication and billing onboarding](artifact/references/onboarding.md)
- [Amazon SP-API searchContentDocuments](https://developer-docs.amazon.com/sp-api/reference/searchcontentdocuments)
- [Amazon SP-API createContentDocument](https://developer-docs.amazon.com/sp-api/reference/createcontentdocument)
- [Amazon SP-API getContentDocument](https://developer-docs.amazon.com/sp-api/reference/getcontentdocument)
- [Amazon SP-API updateContentDocument](https://developer-docs.amazon.com/sp-api/reference/updatecontentdocument)
- [Amazon SP-API postContentDocumentAsinRelations](https://developer-docs.amazon.com/sp-api/reference/postcontentdocumentasinrelations)
- [Amazon SP-API postContentDocumentApprovalSubmission](https://developer-docs.amazon.com/sp-api/reference/postcontentdocumentapprovalsubmission)
- [Amazon SP-API postContentDocumentSuspendSubmission](https://developer-docs.amazon.com/sp-api/reference/postcontentdocumentsuspendsubmission)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance, JSON files]

**Output Format:** [Markdown guidance with shell commands and JSON API responses or summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scripts save complete responses under linkfox/<date>/<session>/data and may print summaries unless --inline is used.]

## Skill Version(s):

1.0.6 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
