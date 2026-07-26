## Description: <br>
Use when building or maintaining a personal LLM-powered knowledge base. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paudyyin](https://clawhub.ai/user/paudyyin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, researchers, and knowledge workers use this skill to ingest sources into a workspace wiki, compile them into persistent Markdown knowledge articles, query that knowledge base, archive answers, and lint wiki quality. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Ingest, archive, and lint workflows can create or update files under wiki-kb/. <br>
Mitigation: Review workspace diffs after these workflows, especially before committing or sharing the knowledge base. <br>
Risk: Lint auto-fixes can change index entries, links, raw references, and same-topic cross-references. <br>
Mitigation: Review lint changes when preserving the exact wiki structure or link layout matters. <br>
Risk: External source ingestion can introduce stale, inaccurate, or conflicting source claims into compiled articles. <br>
Mitigation: Keep source attribution, review compiled articles, and retain conflict annotations when sources disagree. <br>


## Reference(s): <br>
- [Article Template](references/article-template.md) <br>
- [Archive Template](references/archive-template.md) <br>
- [Index Template](references/index-template.md) <br>
- [Raw Source Template](references/raw-template.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Files, Guidance] <br>
**Output Format:** [Markdown files and conversational Markdown answers] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create and update wiki-kb/raw/ and wiki-kb/wiki/ files during ingest, archive, and lint workflows.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
