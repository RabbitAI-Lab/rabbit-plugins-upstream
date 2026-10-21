## Description:

Helps users respond to Chinese patent office actions by drafting a response statement, amended claims, and a Word amendment comparison table.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ip930](https://clawhub.ai/user/ip930)

### License/Terms of Use:

MIT-0

## Use Case:

Chinese patent applicants and practitioners use this skill to prepare responses to CNIPA examination opinions from the complete office action and application materials. It drafts a response statement, revised claims, and an amendment comparison document, with user review of the strategy and claims.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Server responses may write files outside the selected folder, and API-key safeguards are incomplete.

Mitigation: Run in a filesystem-isolated environment that restricts writable locations; prefer a version that confines output paths, validates API destinations and redirects, and protects credentials.

Risk: Full patent materials are sent to PatentMax at api.ip930.com.

Mitigation: Confirm confidentiality and retention terms before uploading sensitive documents.

Risk: Each task incurs a ¥15 charge.

Mitigation: Obtain explicit user consent before submitting a task, and only use automatic drafting when explicitly requested.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/ip930/skills/office-action-response)
- [PatentMax service](https://ip930.com)
- [PatentMax API service](https://api.ip930.com)

## Skill Output:

**Output Type(s):** [Guidance, Text, Files]

**Output Format:** [Conversational text and Microsoft Word (.docx) documents]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The user reviews the response strategy and confirms amended claims before final drafting; each task costs ¥15.]

## Skill Version(s):

1.0.7 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
