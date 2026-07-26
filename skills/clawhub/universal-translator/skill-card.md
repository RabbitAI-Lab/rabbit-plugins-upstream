## Description: <br>
Framework for translating Word, PDF, Excel, PowerPoint, HTML, Markdown, and TXT documents, with the AI agent's configured LLM performing the actual translation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tobewin](https://clawhub.ai/user/tobewin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to translate selected documents or folders across common office and text formats while preserving document structure where supported. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Document text is read and sent to the configured LLM for translation, which may be remote depending on the user's OpenClaw setup. <br>
Mitigation: Use this skill only with documents approved for the configured LLM, choose explicit input and output folders, and avoid broad directories containing unrelated sensitive files. <br>
Risk: Translated output files may contain translation errors or formatting changes. <br>
Mitigation: Review translated copies before replacing originals or using them in production workflows. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/tobewin/skills/universal-translator) <br>
- [LICENSE.txt](artifact/LICENSE.txt) <br>


## Skill Output: <br>
**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with Python and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces guidance for parsing documents, invoking the agent's translation function, and writing translated output files.] <br>

## Skill Version(s): <br>
1.0.5 (source: frontmatter, release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
