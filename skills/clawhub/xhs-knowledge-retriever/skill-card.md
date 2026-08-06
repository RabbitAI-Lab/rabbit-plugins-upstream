## Description: <br>
Retrieve semantically relevant Xiaohongshu competitor-note chunks from a local RAG index built by xhs-knowledge-indexer. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kekena1016](https://clawhub.ai/user/kekena1016) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Content strategists, planners, and agent workflows use this skill to retrieve relevant examples from a local Xiaohongshu competitor-note RAG index before planning or writing. Retrieved chunks are intended as inspiration, not text to republish verbatim. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads a caller-configured local XHS knowledge index and can write JSON to a caller-provided output path. <br>
Mitigation: Install and run it only where access to the configured knowledge index is intended, and use trusted local paths for --index-dir and --output. <br>
Risk: sentence-transformers may use or fetch embedding models when the requested model is not already cached locally. <br>
Mitigation: Pre-cache the model named by index.json for offline use, and pin dependencies or use a lockfile for repeatable installs. <br>
Risk: Retrieved competitor-note chunks could be misused as copy-ready source text. <br>
Mitigation: Use retrieved chunks as planning inspiration only and review generated content to avoid publishing competitor text verbatim. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kekena1016/skills/xhs-knowledge-retriever) <br>
- [Skill homepage](https://github.com/catherinewu/xhs-knowledge-retriever) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, guidance] <br>
**Output Format:** [JSON retrieval results or readiness status, with optional human-facing shell command guidance in the skill documentation.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Results include query, embedding model, top-k setting, cosine similarity score, retrieved chunk text, and associated metadata.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata and changelog, released 2026-07-31) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
