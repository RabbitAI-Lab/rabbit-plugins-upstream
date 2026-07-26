## Description: <br>
Complete agent memory + performance system that extracts structured facts, builds knowledge graphs, generates briefings, enforces execution discipline, and ingests external knowledge into searchable memory. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[joe-rlo](https://clawhub.ai/user/joe-rlo) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use this skill to maintain durable local memory across sessions, consolidate decisions and preferences, generate daily briefings, import ChatGPT exports, and apply session lifecycle routines for more consistent execution. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Workspace notes, session transcripts, imported conversations, identity files, and after-action summaries may be stored as local memory. <br>
Mitigation: Review generated memory files, avoid importing highly sensitive archives, and disable or tightly configure transcript ingestion and after-action persistence in sensitive environments. <br>
Risk: Configured LLM providers may process workspace memory during extraction, linking, and briefing generation. <br>
Mitigation: Use a dedicated API key, confirm provider configuration before running the pipeline, and run dry-runs before importing external conversation archives. <br>


## Reference(s): <br>
- [Setup Guide](references/setup.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/joe-rlo/skills/memory-pipeline) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown, JSONL, JSON, and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local memory files, a generated BRIEFING.md, extracted fact records, a knowledge graph, knowledge summaries, and imported conversation markdown.] <br>

## Skill Version(s): <br>
0.4.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
