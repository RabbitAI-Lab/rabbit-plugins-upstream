## Description: <br>
DocToSkill converts TXT, Markdown, DOCX, and PDF documents into a reusable skill ZIP backed by normalized Markdown, extracted images, generated skill metadata, and a grounded JSONL knowledge index. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jarvisyaoht](https://clawhub.ai/user/jarvisyaoht) <br>

### License/Terms of Use: <br>
Apache-2.0 <br>


## Use Case: <br>
Developers and agent builders use DocToSkill to turn document collections into portable, indexed skill packages that agents can search and inspect as bounded knowledge sources. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Source documents, extracted images, and indexed excerpts may contain sensitive information that is packaged into the generated skill archive. <br>
Mitigation: Review input documents and the generated archive for sensitive content before sharing, publishing, or installing the resulting skill. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/jarvisyaoht/skills/doc-to-skill) <br>
- [README](README.md) <br>
- [Batch Indexing Contract](references/indexing.md) <br>
- [Skill Metadata Contract](references/metadata.md) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, code, shell commands, configuration] <br>
**Output Format:** [Skill ZIP containing generated Markdown instructions, YAML agent metadata, JSONL index data, source Markdown, extracted assets, and a Python retrieval helper.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated packages are self-contained and may include source document text, extracted images, and indexed excerpts.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
