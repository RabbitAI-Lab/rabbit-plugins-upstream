## Description:

Helps agents manage Amazon Store A+ Content through LinkFox and Amazon SP-API operations for searching, creating, reading, updating, validating, associating ASINs, submitting approvals, checking publish records, and suspending A+ display.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, agencies, and developers use this skill to operate Amazon A+ Content workflows through LinkFox, including document management, ASIN association checks, approval submission, publish-record lookup, and suspension requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can handle LinkFox account login, SMS verification, API key creation, subscription ordering, and payment QR generation.

Mitigation: Use onboarding flows only when the user initiated them, use trusted LinkFox endpoint environment variables, and treat verification codes, API keys, stdout, and logs as secret-bearing.

Risk: The skill stores Amazon A+ response data persistently in the workspace.

Mitigation: Run it only in trusted workspaces, review saved response files for sensitive store data, and remove retained data when it is no longer needed.

Risk: Write operations can change live Amazon A+ Content, including replacing ASIN associations, submitting approval, or suspending display.

Mitigation: Confirm user intent before write operations and verify seller, region, marketplace, contentReferenceKey, and ASIN inputs before execution.

## Reference(s):

- [Amazon Store A+ Content Management API Reference](references/api.md)
- [Authentication and Billing Onboarding](references/onboarding.md)
- [Amazon SP-API searchContentDocuments](https://developer-docs.amazon.com/sp-api/reference/searchcontentdocuments)
- [Amazon SP-API createContentDocument](https://developer-docs.amazon.com/sp-api/reference/createcontentdocument)
- [Amazon SP-API getContentDocument](https://developer-docs.amazon.com/sp-api/reference/getcontentdocument)
- [Amazon SP-API updateContentDocument](https://developer-docs.amazon.com/sp-api/reference/updatecontentdocument)
- [Amazon SP-API postContentDocumentAsinRelations](https://developer-docs.amazon.com/sp-api/reference/postcontentdocumentasinrelations)
- [Amazon SP-API validateContentDocumentAsinRelations](https://developer-docs.amazon.com/sp-api/reference/validatecontentdocumentasinrelations)
- [Amazon SP-API postContentDocumentApprovalSubmission](https://developer-docs.amazon.com/sp-api/reference/postcontentdocumentapprovalsubmission)
- [Amazon SP-API postContentDocumentSuspendSubmission](https://developer-docs.amazon.com/sp-api/reference/postcontentdocumentsuspendsubmission)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, API Calls, Files]

**Output Format:** [Markdown guidance, JSON command arguments, API response summaries, and saved JSON response files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scripts persist full LinkFox and Amazon A+ responses under the current workspace's linkfox session data directory and may print full responses when inline output is requested.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
