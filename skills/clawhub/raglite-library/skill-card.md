## Description: <br>
Local-first RAG cache: distill docs into structured Markdown, then index/query with Chroma + hybrid search (vector + keyword). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[virajsanghvi1](https://clawhub.ai/user/virajsanghvi1) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, engineers, and agent users use this skill to create a local, auditable retrieval cache for private or recurring document collections, then query it with hybrid vector and keyword search. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The installer pulls executable code from an unpinned GitHub main branch. <br>
Mitigation: Review and pin a specific upstream commit before installation when reproducibility or supply-chain control is required. <br>
Risk: The skill can process sensitive local documents and persist generated Markdown, cache metadata, and Chroma data. <br>
Mitigation: Use a dedicated output directory and Chroma collection, avoid highly sensitive inputs unless persistence is acceptable, and define a deletion process for the output directory, `.raglite` cache, and Chroma collection. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/virajsanghvi1/skills/raglite-library) <br>
- [Install source declared by artifact](https://github.com/VirajSanghvi1/raglite.git@main) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown files, shell command output, and local retrieval results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes distilled Markdown, optional outlines and node files, per-document indexes, a root index, and .raglite cache metadata under the selected output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: release metadata and SKILL.md frontmatter; manifest and plugin declare 1.0.6) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
