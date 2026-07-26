## Description: <br>
A personal academic knowledge-base skill that helps researchers ingest literature and research materials, search a local library with BM25 and vector retrieval, supplement results through SmartLib, manage references and tags, maintain wiki-style notes, and export research-session artifacts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[j-levee](https://clawhub.ai/user/j-levee) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Academic researchers and research teams use this skill to build a private literature knowledge base, preserve research materials, search saved and external literature, organize tags and references, and generate research-session notes or exports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Research queries, document metadata, extracted text, an email address, and optional vectorization inputs may be sent to SmartLib or a selected embedding provider. <br>
Mitigation: Review the skill before installing, avoid unpublished or sensitive documents unless remote matching and vectorization are disabled or explicitly controlled, and confirm which provider will receive each request. <br>
Risk: The skill uses shared SmartLib credential and quota configuration with related skills. <br>
Mitigation: Inspect local configuration files and permissions before storing API keys, and confirm quota and credential behavior before enabling external literature retrieval. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/j-levee/skills/academic-knowledge-base) <br>
- [Karpathy LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) <br>
- [SmartLib API](https://www.vipslib.com/) <br>
- [SiliconFlow API keys](https://cloud.siliconflow.cn/account/ak) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown responses plus local JSON, Markdown, configuration, and archive-oriented file outputs.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce SmartLib query results, quota status text, local knowledge-base records, wiki pages, vectors, tags, citations, HTML statistics reports, and research-session exports.] <br>

## Skill Version(s): <br>
3.11.3 (source: server release metadata; artifact frontmatter reports 3.11.2) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
