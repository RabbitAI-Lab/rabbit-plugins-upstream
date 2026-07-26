## Description: <br>
Lobster Memory adds durable knowledge-graph memory to AI agents, with automatic extraction, causal edges, emotion valence, recall, and observable consolidation and forgetting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[littlelollipop](https://clawhub.ai/user/littlelollipop) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use Lobster Memory to give AI assistants persistent conversation-derived memory for facts, preferences, feedback, tasks, and later recall. The skill is intended for agents that can run Python code and manage a local memory file during a conversation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill automatically saves conversation-derived information for future reuse without enough explicit consent, deletion, or sensitive-data controls. <br>
Mitigation: Enable it only when durable memory is needed, disclose memory use to affected users, avoid sharing secrets while it is enabled, keep memory files private, and define a process for inspecting, deleting, or disabling stored memories. <br>
Risk: Installation runs a shell script that creates a Python environment and may install or build the axolotl_rs dependency. <br>
Mitigation: Review install.sh before execution, run it in an appropriate local environment, and verify dependency sources before enabling the skill for routine use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/littlelollipop/skills/lobster-memory) <br>
- [README](README.md) <br>
- [Detailed design](docs/design.md) <br>
- [Competitive analysis](docs/competitive-analysis.md) <br>
- [Axolotl graph database](https://github.com/LittleLollipop/axolotl) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with Python examples, shell commands, JSON extraction payloads, memory context text, recall results, and consolidation reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces and updates local durable memory files; current artifact evidence limits runtime support to Apple Silicon macOS.] <br>

## Skill Version(s): <br>
0.2.1 (source: evidence release, SKILL.md frontmatter, and README changelog) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
