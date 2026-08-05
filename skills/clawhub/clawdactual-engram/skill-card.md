## Description: <br>
Engram helps agents build, query, and maintain persistent local knowledge graphs for code, services, people, infrastructure, concepts, and their relationships. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[morpheis](https://clawhub.ai/user/morpheis) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and AI agents use Engram to preserve relationship knowledge across sessions, map architecture, query dependencies, assess change blast radius, and maintain graph models alongside code changes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Persistent local knowledge graphs can retain sensitive workplace, infrastructure, credential-location, private communication, or people-trust information longer than intended. <br>
Mitigation: Set explicit rules before use: do not store secrets, credential contents, unnecessary credential paths, private email details, or personal trust judgments unless authorized and covered by a deletion plan. <br>
Risk: Stored graph knowledge can become stale or misleading as repositories, services, roles, and relationships change. <br>
Mitigation: Prefer code and architecture metadata over broad memory, verify updates against the source of truth, and use the skill's stale, check, refresh, and verification workflows to keep records current. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/morpheis/skills/clawdactual-engram) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and CLI examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide creation of local SQLite-backed graph data and exports such as JSON, JSON-LD, DOT, or Graphviz-rendered files when the Engram CLI is used.] <br>

## Skill Version(s): <br>
0.1.11 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
