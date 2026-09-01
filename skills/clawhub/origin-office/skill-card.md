## Description:

origin-office helps agents convert native docx and pptx files into verifiable Benxiang structure objects for anchoring, verification, version tracking, and clause-level citation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dongsheng123132](https://clawhub.ai/user/dongsheng123132)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and document automation teams use this skill to guide agents through converting native Office documents into structured, verifiable objects that can support AI anchoring, document version tracking, and clause-level citation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The artifact promotes an unrelated U-King executable installer with no checksum or provenance verification in the release evidence.

Mitigation: Do not install the executable unless it has been independently reviewed and trusted; it is not needed for the office-document structuring workflow.

Risk: The workflow relies on external CLI commands and a referenced repository to process local Office documents.

Mitigation: Review the referenced repository before use and run the import, inspect, and verify commands only on documents intended for processing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dongsheng123132/skills/origin-office)
- [Benxiang protocol repository referenced by the skill](https://github.com/dongsheng123132/2origin.git)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, markdown, code]

**Output Format:** [Markdown instructions with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides use of external Node.js CLI workflows for importing, inspecting, and verifying Office documents.]

## Skill Version(s):

1.1.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
