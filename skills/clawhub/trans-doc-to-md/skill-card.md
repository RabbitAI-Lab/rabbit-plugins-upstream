## Description: <br>
Converts PDFs, Lexiang document links, and prepared Markdown packages into faithful bilingual Markdown work packages that preserve source paragraphs, local image paths, order, and rich document structure. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ajaxhe](https://clawhub.ai/user/ajaxhe) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and documentation engineers use this skill to turn PDFs, Lexiang document links, or prepared Markdown packages into bilingual Markdown work packages for review or downstream publishing. It is especially suited to workflows that need source paragraph preservation, local image path preservation, and validation of the final bilingual document. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The Lexiang workflow can use existing Lexiang credentials to retrieve documents and remote assets. <br>
Mitigation: Use it only with authorized Lexiang content and approved credentials; confirm credential scope before fetching documents or assets. <br>
Risk: The optional Gemini translation path can send Markdown text to Gemini. <br>
Mitigation: For confidential documents, prefer the default non-Gemini workflow unless Gemini use is explicitly approved. <br>
Risk: Document conversion can produce incomplete or misordered paragraphs, images, or rich PDF elements if validation is skipped. <br>
Mitigation: Run the bundled bilingual validation profile for the source type and review image counts, image ordering, and rich elements before downstream publishing. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/ajaxhe/skills/trans-doc-to-md) <br>
- [README](artifact/README.md) <br>
- [Extraction Reference](artifact/references/extraction.md) <br>
- [Translation Reference](artifact/references/translation.md) <br>
- [Rich Elements Reference](artifact/references/rich-elements.md) <br>
- [Lessons Learned](artifact/references/lessons-learned.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Files, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown work package with source.md, optional images/, meta.json, and a final bilingual Markdown file; scripts may also emit shell command output and JSON validation results.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Preserves source paragraphs and local image paths, supports generic and pdf-rich validation profiles, and can optionally use Gemini when GEMINI_API_KEY is configured.] <br>

## Skill Version(s): <br>
3.0.1 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
