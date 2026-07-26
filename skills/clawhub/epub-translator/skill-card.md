## Description: <br>
Translates English EPUB files into bilingual English-and-Chinese editions by preserving source text, inserting Chinese translations after each paragraph, skipping code blocks, preserving formula styling, and adding translated table copies. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[samonysh](https://clawhub.ai/user/samonysh) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, translators, and ebook workflow users use this skill to turn English EPUB books into Chinese bilingual comparison EPUBs while retaining source paragraphs, code blocks, formulas, and table structure. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: EPUB text may be sent to the configured LLM provider during translation. <br>
Mitigation: Use the skill only with content that may be shared with the configured provider, and set an approved API_KEY and BASE_URL before translating private material. <br>
Risk: The artifact includes bundled API configuration that should not be trusted as a production credential setup. <br>
Mitigation: Replace or remove the bundled API key and prefer environment-provided credentials. <br>
Risk: Translation cache and work files can retain source or translated book text. <br>
Mitigation: Run the skill in a dedicated work directory and clear cache/work files after handling sensitive EPUBs. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/samonysh/skills/epub-translator) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and generated EPUB files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces bilingual EPUB output and may create translation cache/work files during execution.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
