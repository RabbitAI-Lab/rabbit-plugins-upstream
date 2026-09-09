## Description:

Uploads tender and bid documents to the 百炼标书 cloud API so an agent can interpret tender requirements, generate bid-document drafts, review bid compliance risks, and compare bid files for similarity signals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External bidding teams and proposal developers use this skill to analyze tender files, produce .docx bid drafts, check bid submissions for compliance risks, and compare 2-3 bid documents for similarity or duplication signals before submission.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender and bid documents can contain sensitive commercial, pricing, and personal information and are uploaded to the vendor cloud service.

Mitigation: Use only files the user is authorized to process, obtain explicit consent before upload, and avoid using the skill for documents that cannot be shared with the vendor service.

Risk: The skill uses a paid API-key account, and exposed API keys, SMS codes, phone numbers, or key-bearing links could compromise the account.

Mitigation: Have users configure credentials themselves, never paste or repeat keys in chat, and share only non-credential platform URLs.

Risk: Security evidence flags unsafe report filename handling and broad output paths until filename containment is fixed.

Mitigation: Avoid custom report basenames or broad output directories, keep generated files under the declared output folder, and review paths before opening or sharing reports.

Risk: Security evidence notes under-disclosed local persistence, including possible state under ~/.zcm.

Mitigation: Review local state locations during installation and cleanup, and remove local credentials or cached state when the skill is no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-review-pro)
- [百炼标书 platform](https://biaoshu.zhiliaobiaoxun.com/)
- [API dispatcher](references/api.md)
- [Authentication, jobs, and billing API](references/api-auth.md)
- [Tender interpretation and bid-document generation API](references/api-bid-workflow.md)
- [Bid compliance review API](references/api-compliance.md)
- [Bid duplication review API](references/api-duplicate.md)
- [Knowledge-base fields](references/knowledge-fields.md)
- [Usage guide](references/usage.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown summaries with JSON results, local HTML/Word reports, .docx bid-document files, configuration guidance, and short-lived download links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include risk labels, evidence excerpts, report file paths, progress updates, and paid-account usage guidance.]

## Skill Version(s):

3.1.0 (source: server release evidence and scripts/zcm_lib/cli.py)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
