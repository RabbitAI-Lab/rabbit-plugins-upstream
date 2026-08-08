## Description: <br>
Archive captures webpages, videos, tweets, PDFs, images, and notes as persistent searchable Markdown snapshots with summaries, semantic tags, and contextual resurfacing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, researchers, and knowledge workers use Archive to preserve external content as local Markdown records, then retrieve it later through semantic search, tags, project metadata, and contextual resurfacing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Archived material may persist long-term in local Markdown files and expose sensitive, regulated, or confidential content if the archive directory is mishandled. <br>
Mitigation: Avoid archiving secrets or restricted documents unless local storage is approved; periodically review, protect, or delete archive files under ~/archive. <br>
Risk: Archived content may be processed by the agent's LLM or API environment when creating summaries, tags, and semantic search results. <br>
Mitigation: Use the skill only with content whose provider-side processing is acceptable, and redact sensitive details before asking the agent to archive them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/archive) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown files with YAML frontmatter, text summaries, search result lists, and brief operational guidance.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Archive items are saved under ~/archive/items/{date}_{slug}.md and may include source metadata, summaries, key points, tags, project names, and archive rationale.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
