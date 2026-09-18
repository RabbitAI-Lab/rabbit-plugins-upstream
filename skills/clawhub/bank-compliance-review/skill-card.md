## Description:

AI-powered bank compliance and regulatory review assistant for screening marketing materials, KYC documents, AML alerts, and NFRA/CBIRC compliance checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gechengling](https://clawhub.ai/user/gechengling)

### License/Terms of Use:

MIT-0

## Use Case:

Bank compliance officers, legal counsel, KYC/AML analysts, and product teams use this skill to draft reviews of marketing materials, KYC documents, AML alerts, China banking regulatory checklists, and reporting language. Its outputs are draft compliance aids that require review under the user's institutional process.

### Deployment Geography for Use:

China-focused banking compliance contexts

## Known Risks and Mitigations:

Risk: Users may paste unredacted customer identifiers, account data, or other sensitive banking information into the conversation.

Mitigation: Use only the minimum fields required for review, redact customer identifiers and account details, and prefer aggregate descriptions where full records are not needed.

Risk: AML, KYC, sanctions, reporting, or legal conclusions may be incomplete or unsuitable for a specific institution's obligations.

Mitigation: Treat outputs as drafts and route final decisions through qualified compliance or legal reviewers under the institution's formal process.

Risk: A suspected sanctions, blacklist, or AML match may be mistaken for a final determination.

Mitigation: Use the skill's output as a triage prompt only, confirm matches with approved systems and human review, and retain the institution's normal escalation workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gechengling/skills/bank-compliance-review)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown-formatted compliance review drafts, checklists, risk ratings, and recommended revisions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Conversation-only output; no code execution, persistence, external system access, or direct regulatory filing.]

## Skill Version(s):

4.1.2 (source: server release and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
