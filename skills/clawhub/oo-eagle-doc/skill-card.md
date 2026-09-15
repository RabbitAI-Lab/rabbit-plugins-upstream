## Description:

Helps agents operate Eagle Doc through an OOMOL-connected account to inspect usage, quota, request logs, and process finance documents with OCR.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill when an agent needs to work with a connected Eagle Doc account, including checking billing-month usage, quota summaries, monthly history, request logs, or extracting structured data from invoices, receipts, and PDFs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access a connected Eagle Doc account and upload documents for OCR when used by an agent.

Mitigation: Use it only when the user intends that account access or document upload, and confirm payloads for any action that changes state.

Risk: Setup instructions include remote installer commands for the oo CLI.

Mitigation: Install the oo CLI through a trusted, versioned, verifiable method and review any installer before execution.

Risk: The security summary reports that the trigger scope is broader than necessary.

Mitigation: Invoke the skill only for explicit Eagle Doc tasks and avoid using it for unrelated document or billing requests.

## Reference(s):

- [Eagle Doc API Product Page](https://www.eagle-doc.com/en/products/eagle-doc-apis/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Skill Release Page](https://clawhub.ai/oomol/skills/oo-eagle-doc)
- [Publisher Profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, JSON, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON action results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
