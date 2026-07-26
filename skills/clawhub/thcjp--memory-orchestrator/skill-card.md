## Description: <br>
Memory Orchestrator helps AI agents organize durable memory with four memory tiers, keyword, semantic, and hybrid retrieval, summaries, health checks, conflict handling, cleanup, and optional vector database configuration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external agent users use this skill to manage long-running conversational memory, multi-agent shared memory, chatbot context, and customer-support assistant context. It supports adding, searching, summarizing, persisting, checking, and cleaning memory records. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Stored memories may contain sensitive personal or operational context. <br>
Mitigation: Avoid storing credentials, financial data, health data, government identifiers, or other sensitive personal data unless there is a clear need and retention policy. <br>
Risk: Callback URLs or optional external vector providers may expose memory content outside the agent environment. <br>
Mitigation: Use callback URLs and retrieval providers only when they are trusted, expected, and appropriate for the data being processed. <br>
Risk: Automatic cleanup, deletion, archival, and conflict resolution can remove or alter useful context. <br>
Mitigation: Keep backups or review logs, and require human review for important memory edits or unresolved same-field conflicts. <br>


## Reference(s): <br>
- [ClawHub Skill Listing](https://clawhub.ai/thcjp/skills/memory-orchestrator) <br>
- [SkillHub Homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline TypeScript examples, JSON-like status reports, and file persistence guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce memory IDs, search results, summaries, health reports, cleanup logs, configuration confirmations, and persistent memory files.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata; artifact frontmatter lists 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
