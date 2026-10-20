## Description:

Creates preliminary Word patent drafts from invention materials, R&D reports, technical proposals, or an initial idea.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ip930](https://clawhub.ai/user/ip930)

### License/Terms of Use:

MIT-0

## Use Case:

External users and R&D teams use the skill to turn invention disclosures, technical materials, or an idea into a preliminary patent draft with claims and drawings, plus separate review notes. Users with only an idea can first explore possible patent directions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated requests could be exposed or sent to an unintended destination if transport and destination checks are weak.

Mitigation: Require HTTPS and validate destinations before sending authenticated requests.

Risk: Permanent API credentials could be exposed through chat or insecure storage.

Mitigation: Store credentials privately and do not send permanent keys through chat.

Risk: Unpublished invention materials may be sensitive when uploaded for processing.

Mitigation: Review the materials being shared and confirm PatentMax's confidentiality and retention terms before upload.

Risk: A paid submission could start without the user's informed agreement.

Mitigation: Obtain confirmation before submitting a paid task; explain that running tasks can be cancelled.

## Reference(s):

- [Workflow](references/workflow.md)
- [Materials Guide](references/materials-guide.md)
- [FAQ](references/faq.md)
- [Demo Solution](references/demo-solution.md)
- [PatentMax API Platform Documentation](https://api.ip930.com/features/api-platform)

## Skill Output:

**Output Type(s):** [Word documents, Guidance]

**Output Format:** [Microsoft Word (.docx) preliminary patent draft and review notes; idea-only requests produce a list of directions.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preliminary drafts require review by a patent professional before filing.]

## Skill Version(s):

1.1.7 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
