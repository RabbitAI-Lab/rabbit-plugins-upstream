## Description:

Organizes source material into an IMA Wiki knowledge base, with topic guides, tags, folders, and knowledge-base health checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cookfish1979](https://clawhub.ai/user/cookfish1979)

### License/Terms of Use:

MIT-0

## Use Case:

IMA knowledge-base users use this skill to import and organize materials, create and update linked topic guides, manage tags and folders, and review knowledge-base health. It requires IMA OpenAPI credentials and is not intended for simple Q&A or single-document summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Exposure of IMA OpenAPI credentials.

Mitigation: Keep the IMA API key private and use it only for intended knowledge-base management.

Risk: Unintended changes to notes, tags, or folders.

Mitigation: Review planned changes and affected content before confirming updates.

Risk: Importing untrusted web content into a private or sensitive knowledge base.

Mitigation: Check web sources and their suitability before importing them.

## Reference(s):

- [IMA Wiki skill release](https://clawhub.ai/cookfish1979/skills/ima-wiki)
- [IMA agent interface](https://ima.qq.com/agent-interface)
- [IMA API reference](artifact/references/api-reference.md)
- [Guide schema](artifact/references/schema.md)
- [Knowledge-base safety guidance](artifact/references/security.md)

## Skill Output:

**Output Type(s):** [Markdown, Guidance, API calls]

**Output Format:** [Markdown guides, health-check reports, and suggested IMA knowledge-base changes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update IMA notes, tags, and folders after user confirmation.]

## Skill Version(s):

1.0.0 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
