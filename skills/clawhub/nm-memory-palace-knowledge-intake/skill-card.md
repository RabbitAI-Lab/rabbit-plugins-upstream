## Description: <br>
Processes external resources into stored knowledge with quality scoring and routing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and knowledge-maintenance agents use this skill to evaluate linked articles, documents, papers, and session findings, then decide whether and where to store them in a persistent knowledge corpus. It also guides routing to local codebase updates, meta-infrastructure updates, queue processing, pruning review, and optional GitHub Discussion promotion for evergreen entries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can publish or update knowledge entries in GitHub Discussions. <br>
Mitigation: Use Discussion promotion only when the target repository and content are intended to be public, and require explicit review before any public Discussion update. <br>
Risk: The skill can mutate local or agent knowledge stores, including corpus entries, developer drafts, queue records, and curation logs. <br>
Mitigation: Avoid --auto-accept on real corpora, use sandbox output paths for tests, and require explicit approval before skill, module, agent, or knowledge-store changes. <br>
Risk: External resources may be converted into durable knowledge with incorrect attribution or low-quality prose. <br>
Mitigation: Apply the skill's content-boundary, scribe validation, document verification, and human review steps before finalizing stored entries. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-memory-palace-knowledge-intake) <br>
- [ClawHub metadata homepage](https://github.com/athola/claude-night-market/tree/master/plugins/memory-palace) <br>
- [KonMari Method](https://konmari.com/about-the-konmari-method/) <br>
- [Spark Joy Philosophy](https://konmari.com/marie-kondo-rules-of-tidying-sparks-joy/) <br>
- [Why the KonMari Method Works](https://konmari.com/what-is-konmari-method/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with YAML examples and inline shell and Python code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update local knowledge entries, developer drafts, curation logs, queue records, and GitHub Discussion summaries when approved.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
