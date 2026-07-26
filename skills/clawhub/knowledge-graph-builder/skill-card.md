## Description: <br>
Builds, updates, and deploys an interactive knowledge graph from a structured knowledge vault by scanning INDEX.md entries, article frame_analysis metadata, framework nodes, and configurable cross-links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[milesnee](https://clawhub.ai/user/milesnee) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and knowledge-base maintainers use this skill to turn a structured vault into a browsable Canvas-based HTML graph with search, filters, edge highlighting, and node inspection. It is suited for visualizing cross-domain relationships after adding or recategorizing articles. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads a selected knowledge-vault directory to build the graph. <br>
Mitigation: Run it only on vaults the user intends to analyze and keep generated outputs in a controlled local directory. <br>
Risk: Serving the generated graph from a vault directory on 0.0.0.0 can expose private files over the network. <br>
Mitigation: Prefer opening the HTML locally or bind any temporary server to 127.0.0.1 from a dedicated output directory. <br>


## Reference(s): <br>
- [Knowledge Graph Builder ClawHub page](https://clawhub.ai/milesnee/skills/knowledge-graph-builder) <br>
- [Publisher profile](https://clawhub.ai/user/milesnee) <br>
- [INDEX classification reference](artifact/references/index-classification.md) <br>
- [Example graph configuration](artifact/templates/config.example.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with bash commands and JSON configuration examples; the bundled script can generate a self-contained HTML graph file.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The generated HTML graph is designed for local viewing; network serving should be restricted when the source vault contains private material.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release evidence and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
