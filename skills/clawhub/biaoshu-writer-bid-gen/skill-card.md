## Description:

Analyzes tender and bid files, generates finished bid documents, reviews proposal compliance risks, and compares bid files for similarity through the Bailian Biaoshu service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External bid, procurement, and proposal teams use this skill to interpret tender requirements, draft .docx bid documents, check compliance issues, and identify similarity risks before submission.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uploads commercially sensitive tender and bid files to the vendor service, and files or results may remain associated with the API-key account.

Mitigation: Use only files the user is authorized to process, obtain consent before upload, and review the vendor's data-handling expectations before confidential use.

Risk: A full-account API key is stored locally and could be exposed if pasted into chat or included in copied links.

Mitigation: Have the user configure the API key locally, keep the credential out of conversation history, and avoid sharing key-bearing redirect or billing links.

Risk: Bid generation, review, and duplicate checking can consume the account word balance.

Mitigation: Confirm paid actions such as target pages and document checks before submission, and show available-balance information when the platform returns it.

Risk: Server security guidance flags under-disclosed persistence, an unsafe phone-registration prompt, redirect handling, and local metadata-cache concerns.

Mitigation: Review or fix those areas before using the skill with confidential procurement documents.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-bid-gen)
- [Bailian Biaoshu service](https://biaoshu.zhiliaobiaoxun.com/)
- [Open API dispatch guide](references/api.md)
- [Authentication, jobs, and word balance API](references/api-auth.md)
- [Tender interpretation and bid-document workflow API](references/api-bid-workflow.md)
- [Bid compliance review API](references/api-compliance.md)
- [Bid duplicate checking API](references/api-duplicate.md)
- [Knowledge-base fields](references/knowledge-fields.md)
- [Usage guide](references/usage.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, files, guidance]

**Output Format:** [Markdown/text responses, JSON results, HTML or Word reports, short-lived download links, and .docx bid documents.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Long-running tasks report progress; paid actions can consume the connected account's word balance.]

## Skill Version(s):

3.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
