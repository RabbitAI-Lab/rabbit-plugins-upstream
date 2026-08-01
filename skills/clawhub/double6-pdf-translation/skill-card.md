## Description: <br>
Translate user-supplied text PDFs into Simplified Chinese and bilingual PDFs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[double6-ai](https://clawhub.ai/user/double6-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and document-processing agents use this skill to translate non-scanned English PDFs into Simplified Chinese while preserving layout, terminology, formulas, references, and bilingual deliverables. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Full PDF text is sent to the selected model endpoint and retained in output-directory diagnostics. <br>
Mitigation: Use approved endpoints for confidential documents, run on a trusted single-user machine, and keep output folders private. <br>
Risk: API keys can be exposed through child process arguments. <br>
Mitigation: Prefer key-file based configuration, restrict local process visibility, and treat API keys as exposed to local process inspection until command-line key handling is fixed. <br>
Risk: Optional arXiv, Docker, cloud layout, and compatibility-proxy features expand the network or execution surface. <br>
Mitigation: Leave these options disabled unless required for the document workflow and explicitly approved. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/double6-ai/skills/double6-pdf-translation) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/double6-ai) <br>
- [Homepage](https://github.com/double6-ai/double6-skills/tree/main/skills/double6-pdf-translation) <br>
- [Workflow](references/workflow.md) <br>
- [Academic Translation Policy](references/academic-translation-policy.md) <br>
- [Runtime Dependencies](references/runtime-dependencies.md) <br>
- [Provider Base URLs](references/provider-base-urls.md) <br>
- [Known Pitfalls](references/known-pitfalls.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with shell commands and generated PDF, JSON, and diagnostic files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces Chinese-only and bilingual PDF outputs, a render manifest, and quality diagnostics under the selected output directory.] <br>

## Skill Version(s): <br>
1.0.4 (source: frontmatter, release evidence, CHANGELOG) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
