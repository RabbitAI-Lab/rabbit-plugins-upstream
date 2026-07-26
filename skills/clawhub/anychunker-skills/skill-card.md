## Description: <br>
Helps agents use the anychunker Python library to split text, Markdown, code, and long documents for LLM, RAG, and agent pipelines. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[anyforge](https://clawhub.ai/user/anyforge) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to choose an AnyChunker splitter, generate minimal working examples, verify installation, and prepare chunked content for LLM, RAG, or agent workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may activate for broad chunking-related prompts and provide AnyChunker-specific guidance when the user's intent is still ambiguous. <br>
Mitigation: Confirm the intended input type and desired chunking strategy before applying the guidance. <br>
Risk: Generated examples may be adapted to private repositories, external embedding APIs, or vector databases. <br>
Mitigation: Review data paths, credentials, and outbound service usage before running examples on sensitive content. <br>


## Reference(s): <br>
- [AnyChunker API Reference](references/api-reference.md) <br>
- [AnyChunker Recipes](references/recipes.md) <br>
- [AnyChunker on PyPI](https://pypi.org/project/anychunker/) <br>
- [AnyChunker GitHub Repository](https://github.com/anyforge/anychunker) <br>
- [AnyChunker DeepWiki](https://deepwiki.com/anyforge/anychunker/) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown with Python and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include installation checks, chunker selection guidance, small Python examples, and RAG ingestion patterns.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
