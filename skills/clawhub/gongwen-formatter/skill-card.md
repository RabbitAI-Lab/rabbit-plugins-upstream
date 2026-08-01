## Description: <br>
Converts Markdown into GB/T 9704-2012 Chinese government official-document Word files, with optional remote image embedding. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[edwardwason](https://clawhub.ai/user/edwardwason) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to turn Markdown reports, briefs, and other structured text into formatted .docx files that follow GB/T 9704-2012 layout conventions. It focuses on document formatting and does not classify official document types, add official decorations, or review content compliance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Markdown with remote images can trigger outbound HTTP or HTTPS requests during conversion. <br>
Mitigation: Review image URLs before processing untrusted Markdown or pass download_images=False in sensitive or restricted network environments. <br>
Risk: The generated Word file may look like an official document even though the skill does not review content or validate required official-document elements. <br>
Mitigation: Review generated documents for content, regulatory, and organizational requirements before relying on or distributing them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/edwardwason/skills/gongwen-formatter) <br>
- [Project homepage](https://github.com/EdwardWason/official-doc) <br>


## Skill Output: <br>
**Output Type(s):** [files, text] <br>
**Output Format:** [.docx file plus success status and output path] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes a Word document to the requested output path; remote image downloads are optional and can be disabled with download_images=False.] <br>

## Skill Version(s): <br>
1.1.3 (source: server release evidence and artifact metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
