## Description:

Helps agents parse, extract, split, and edit documents through Reducto using a Maton connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can use this skill to process documents, extract structured information, and modify PDF or DOCX files through their connected Reducto account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected documents are sent to Reducto through Maton for processing.

Mitigation: Review each document and connection before authorizing access or processing.

Risk: Document edits or processing can change content or consume credits.

Mitigation: Confirm the target, intended change, and expected cost before approving a write or processing request.

Risk: Hosted functions, triggers, and destinations can create ongoing data flows or expose credentials if configured incorrectly.

Mitigation: Approve each automation and destination separately, limit access, and never place credentials in destination settings.

## Reference(s):

- [Reducto documentation](https://docs.reducto.ai)
- [Reducto API reference](https://docs.reducto.ai/api-reference)
- [Maton homepage](https://maton.ai)
- [Maton CLI manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Guidance]

**Output Format:** [Markdown with command and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may include extracted document text or structured data; document changes and automated workflows require user approval.]

## Skill Version(s):

1.2.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
