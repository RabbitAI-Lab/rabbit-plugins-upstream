## Description:

Extracts WeChat contact-list screen recordings on macOS into deduplicated raw text and structured CRM exports using FFmpeg, Apple Vision OCR, and rule-based contact parsing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[emergencescience](https://clawhub.ai/user/emergencescience)

### License/Terms of Use:

MIT

## Use Case:

Developers and authorized operators use this skill to turn their own WeChat contact-list screen recordings into local raw text, CSV, JSON, and HTML CRM views for contact management and analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill bulk-extracts private WeChat contact information into persistent CRM files.

Mitigation: Run it only for contact data you are authorized to process, keep exports in protected storage, and confirm consent or another lawful basis before sharing or importing the data into CRM systems.

Risk: Temporary video frames and OCR outputs may retain sensitive personal data after processing.

Mitigation: Delete cached frames and intermediate raw text when the analysis is complete, and avoid storing outputs in shared or synced folders unless that storage is approved for personal data.

Risk: The Python pipeline compiles and executes a local Swift OCR helper.

Mitigation: Review the Swift helper and Python subprocess calls before execution, and run the pipeline in a trusted local workspace.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/emergencescience/skills/emergence-wechat-contact-crm)
- [Server-resolved source repository](https://github.com/emergencescience/emergence-wechat-contact-crm)

## Skill Output:

**Output Type(s):** [text, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with command examples; generated artifacts are TXT, CSV, JSON, and HTML files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Processes local screen-recording files and writes durable contact exports and cached frames to disk.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata; artifact frontmatter states 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
