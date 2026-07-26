## Description: <br>
Provides local TF-IDF and SQLite search over MEMORY.md or markdown documentation so agents can retrieve relevant context quickly without external dependencies. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mig6671](https://clawhub.ai/user/mig6671) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent operators use this skill to index local memory or documentation files and search for relevant context before acting on a task. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads and locally indexes an agent memory file, which may include sensitive operational context if users store it there. <br>
Mitigation: Keep secrets and credentials out of MEMORY.md, and review or clear the local SQLite index when sensitive memory content changes. <br>
Risk: Using memory search as an automatic step for every request can surface irrelevant or stale context. <br>
Mitigation: Use targeted queries and review the returned sections before relying on them for task decisions. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/mig6671/skills/vector-memory-hack) <br>
- [OpenClaw](https://openclaw.ai) <br>
- [Python 3.8+](https://www.python.org/downloads/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and plain-text search results.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Search results include ranked section titles, similarity scores, and truncated local memory content.] <br>

## Skill Version(s): <br>
1.0.3 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
