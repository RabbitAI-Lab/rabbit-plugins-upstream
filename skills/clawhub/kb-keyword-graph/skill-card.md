## Description: <br>
Reads a knowledge base keyword tree and helps an agent summarize structure, render an interactive keyword graph, compare topic distribution, or explain how two keywords relate. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ywc668](https://clawhub.ai/user/ywc668) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to inspect a 2brain knowledge base or configured local/Elasticsearch corpus by topic structure, topic distribution, keyword graph, or keyword relationship. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The optional local and Elasticsearch backends can process a local corpus or search index, expanding the data surface beyond the default 2brain keyword API. <br>
Mitigation: Keep the default backend unless local or Elasticsearch processing is intended, and review the configured corpus directory or index before use. <br>
Risk: The skill needs a 2brain graph API key or private config file to fetch keyword trees. <br>
Mitigation: Store the config file with restrictive permissions, avoid printing credentials, and rotate the key if it is exposed. <br>
Risk: Cached keyword trees and generated graph HTML may reveal sensitive taxonomy or topic distribution for a knowledge base. <br>
Mitigation: Write graph outputs only to approved locations and clear the state cache when the keyword tree should not persist. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/ywc668/skills/kb-keyword-graph) <br>
- [Workflow reference](references/workflows.md) <br>
- [Validation notes](references/validation.md) <br>
- [Chinese skill reference](references/SKILL.zh.md) <br>
- [Chinese workflow reference](references/workflows.zh.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, HTML file] <br>
**Output Format:** [Markdown guidance with JSON engine output summaries and optional self-contained HTML graph files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [All reported counts, percentages, and relations should come from kw_graph.py stdout; graph percentages are sibling-share values, not whole-KB percentages.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
