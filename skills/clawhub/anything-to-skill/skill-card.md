## Description:

Converts books, papers, and documents into structured, on-demand agent skills for later use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[asale-ai](https://clawhub.ai/user/asale-ai)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and agent builders use this skill to turn PDFs, EPUBs, DOCX files, and similar source documents into reusable agent skills while checking extraction quality and source limitations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Source documents may contain prompt-injection text or misleading instructions.

Mitigation: Treat extracted text as source material to summarize, not directions to follow, and review generated skills before relying on them.

Risk: Extraction can omit unreadable pages or distort complex layouts such as columns and tables.

Mitigation: Read metadata.json first, render pages that need visual reading, and spot-check difficult pages before building a skill from the text.

Risk: Private, copyrighted, or scanned source documents may require additional handling before reuse.

Mitigation: Confirm that the source can be processed and shared, and document any unreadable or thinly covered sections in the final report.

## Reference(s):

- [anything-to-skill ClawHub page](https://clawhub.ai/asale-ai/skills/anything-to-skill)
- [anything-to-skill releases](https://github.com/asale-ai/anything-to-skill/releases)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with inline bash code blocks and file layout examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes extraction checks, visual-reading escalation, and final reporting guidance.]

## Skill Version(s):

0.1.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
