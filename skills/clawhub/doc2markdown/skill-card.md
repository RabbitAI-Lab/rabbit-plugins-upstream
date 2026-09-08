## Description:

Lightweight document utility designed to convert files to Markdown (MD), built specifically for intelligent agents (e.g., OpenClaw, ClaudeCode) to read and process content.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haoyt27](https://clawhub.ai/user/haoyt27)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use Doc2Markdown to convert office documents, PDFs, images, ebooks, and related file formats into Markdown so agents can read, summarize, analyze, or export document content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can upload private PDFs, office files, images, or business documents to the third-party cloud service at lab.hjcloud.com for conversion.

Mitigation: Use it only when third-party cloud processing is acceptable, and avoid submitting sensitive or confidential documents unless the service's data handling practices have been reviewed.

Risk: Agents may invoke conversion for broad read, summarize, or analyze requests without an explicit consent step.

Mitigation: Confirm user intent before converting documents that may contain private, regulated, or business-confidential content.

Risk: The optional API key is sent to the conversion service when configured.

Mitigation: Configure the API key only when the service is trusted, keep the token scoped to this skill, and prefer environment-based secret management over checked-in configuration files.

## Reference(s):

- [Doc2Markdown service endpoint](https://lab.hjcloud.com/llmdoc)
- [ClawHub skill page](https://clawhub.ai/haoyt27/skills/doc2markdown)

## Skill Output:

**Output Type(s):** [Markdown, Files, Shell commands, Configuration guidance]

**Output Format:** [Markdown files or extracted ZIP packages with command-line status text and document IDs for pending conversions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js. Outputs are saved beside the source file as either a single Markdown file or a directory containing the converted Markdown package.]

## Skill Version(s):

1.0.11 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
