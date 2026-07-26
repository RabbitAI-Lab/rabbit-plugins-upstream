## Description: <br>
Personality persistence for AI agents. Remember how you think, not just what happened. Structured insights that survive session restarts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[morpheis](https://clawhub.ai/user/morpheis) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use Chitin to maintain structured behavioral, personality, relational, principle, skill, and trigger insights across agent sessions. It helps agents retrieve compact personality context, reflect on completed sessions, and optionally share selected insights with external knowledge services. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Persistent personality insights can steer future sessions with stale, incorrect, overly personal, or sensitive content. <br>
Mitigation: Review stored insights and triggers regularly, archive outdated entries, and avoid storing secrets or private details. <br>
Risk: Embedding, similarity, and retrieval commands may send query text to an external embedding provider. <br>
Mitigation: Use these commands only with text suitable for external processing, and avoid piping credentials, file contents, or private data into semantic-search queries. <br>
Risk: Promoting insights can share personal knowledge with the external Carapace service, especially if safety checks are overridden. <br>
Mitigation: Review each insight before promotion, keep relational and trigger insights private, and avoid using force overrides in automated or externally influenced workflows. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/morpheis/skills/chitin) <br>
- [npm package @clawdactual/chitin](https://www.npmjs.com/package/@clawdactual/chitin) <br>
- [GitHub repository](https://github.com/Morpheis/chitin) <br>
- [Carapace shared knowledge base](https://carapaceai.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with CLI commands and optional JSON output from retrieval/export commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include compact personality context, insight records, status summaries, and setup commands.] <br>

## Skill Version(s): <br>
1.4.5 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
