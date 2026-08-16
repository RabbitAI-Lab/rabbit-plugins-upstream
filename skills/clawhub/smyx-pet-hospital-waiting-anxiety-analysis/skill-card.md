## Description:

Analyzes pet hospital waiting-area videos or video URLs for anxiety-related behavior signals and returns a standardized 1-5 anxiety level to help veterinary staff prioritize comfort or care without diagnosing disease or prescribing treatment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Veterinary clinic staff, pet hospital teams, and pet-care operators use this skill to analyze waiting-area pet videos for stress indicators such as panting, trembling, flattened ears, hiding, stiffness, and other anxiety signals. The output is intended to support triage and comfort workflows, not clinical diagnosis or treatment planning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends videos or video URLs to Life Emergence cloud endpoints for analysis.

Mitigation: Review data handling requirements before installation, avoid submitting sensitive media without authorization, and confirm that cloud processing is acceptable for the veterinary workflow.

Risk: The skill silently creates or reuses account identities and can store account tokens and profile fields in a workspace SQLite database.

Mitigation: Inspect local workspace data storage, restrict filesystem access to trusted users, and remove or rotate stored identity data when the skill is no longer needed.

Risk: Broad report-history triggers can retrieve cloud report history automatically.

Mitigation: Use the history-list behavior only in authorized contexts and review returned reports before sharing them with users.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-pet-hospital-waiting-anxiety-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](artifact/references/api_doc.md)
- [Analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown text with structured JSON-style analysis results, optional report-history output, and optional saved output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report export links and report history tables; local video uploads are limited to mp4, avi, or mov files up to 10 MB.]

## Skill Version(s):

1.0.10 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
