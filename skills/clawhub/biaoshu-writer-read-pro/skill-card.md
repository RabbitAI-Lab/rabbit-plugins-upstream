## Description:

This skill helps agents use the 百炼®标书 service to interpret tender documents, generate bid documents, review bid compliance, and compare bid files for similarity risks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External procurement, bidding, and proposal teams use this skill to process local tender and bid files through 百炼®标书 for tender interpretation, draft bid generation, compliance review, and similarity-risk checks before submission.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender and bid files may contain confidential commercial, pricing, or personal information and are uploaded to the 百炼®标书 cloud service.

Mitigation: Use the skill only after confirming the user is comfortable with cloud processing and retention under the API-key account.

Risk: The API key grants access to the user's 百炼®标书 account.

Mitigation: Keep the API key out of chat and store it only in the local config file as instructed.

Risk: Similarity checks can surface risk signals but do not make legal determinations about collusion, bid rigging, or bid validity.

Mitigation: Present similarity results as internal review signals and route legal conclusions to qualified reviewers.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-read-pro)
- [百炼®标书 service](https://biaoshu.zhiliaobiaoxun.com/?ch=c666)
- [Open API contract reference](references/api.md)
- [Usage guide](references/usage.md)
- [Knowledge field reference](references/knowledge-fields.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Plain-language summaries, structured JSON results, HTML or Word reports, and generated .docx bid files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs depend on uploaded tender and bid files, the user's API-key account, and available account word balance.]

## Skill Version(s):

1.0.18 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
