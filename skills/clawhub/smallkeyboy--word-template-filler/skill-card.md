## Description: <br>
Parses Word .docx templates for {{placeholder}} fields, helps generate topic-specific content, and fills the template to produce a new Word document. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smallkeyboy](https://clawhub.ai/user/smallkeyboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to extract placeholders from Word templates, generate content for those placeholders from a user-provided topic, and create filled .docx documents for review or sharing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Filled templates may contain sensitive contract, personal, or business information, and the documented uploader step can create a sharing link. <br>
Mitigation: Keep generated documents local by default; upload only after explicit user confirmation that the link should be created and shared. <br>
Risk: Template replacement can leave missing placeholders unchanged and may simplify formatting in replaced paragraphs. <br>
Mitigation: Review the generated Word document before distribution, especially for legal, business, or customer-facing templates. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smallkeyboy/word-template-filler) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Files] <br>
**Output Format:** [Markdown guidance with shell commands, JSON placeholder reports, and generated Word .docx files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python-docx for local Word document parsing and template filling.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
