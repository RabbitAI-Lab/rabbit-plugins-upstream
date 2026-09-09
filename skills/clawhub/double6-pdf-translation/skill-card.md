## Description:

Translate user-supplied text PDFs into Simplified Chinese and bilingual PDFs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[double6-ai](https://clawhub.ai/user/double6-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to translate non-scanned English PDFs into Simplified Chinese while preserving layout and producing bilingual review copies. It is intended for workflows where users explicitly choose the model endpoint, credentials, input PDF, and output directory.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Document text is sent to the model endpoint selected for the translation run.

Mitigation: Confirm the endpoint and provider before use, and install or run the skill only when sending the document text to that endpoint is acceptable.

Risk: API credentials can be exposed through command history or logs if passed carelessly.

Mitigation: Use --api-key-file for credentials and review generated outputs and diagnostics before sharing them.

Risk: The output directory stores translated PDFs, diagnostics, text snippets, and runtime cache files.

Mitigation: Choose an appropriate output directory and inspect or clean generated artifacts according to the document's sensitivity.

Risk: Dependency setup modifies the selected Python environment.

Mitigation: Run setup_venv.sh only inside a dedicated virtual environment that is acceptable to modify.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/double6-ai/skills/double6-pdf-translation)
- [Project Homepage](https://github.com/double6-ai/double6-skills/tree/main/skills/double6-pdf-translation)
- [Workflow](references/workflow.md)
- [Runtime Dependencies](references/runtime-dependencies.md)
- [Academic Translation Policy](references/academic-translation-policy.md)
- [Known Pitfalls](references/known-pitfalls.md)
- [Provider Base URL Candidates](references/provider-base-urls.md)
- [Glossary Template](references/glossary-template.tsv)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and generated PDF, JSON, TSV, and diagnostic files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces translated Chinese and bilingual PDFs, a render manifest, optional glossary artifacts, quality diagnostics, and local runtime cache files under the selected output directory.]

## Skill Version(s):

1.0.5 (source: frontmatter, changelog, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
