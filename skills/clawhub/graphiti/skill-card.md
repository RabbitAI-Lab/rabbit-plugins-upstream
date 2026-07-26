## Description: <br>
Knowledge graph operations via Graphiti API. Search facts, add episodes, and extract entities/relationships. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[emasoudy](https://clawhub.ai/user/emasoudy) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agents use this skill to search a Graphiti knowledge graph for relevant facts and add new episodes or memories through the Graphiti REST API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can add persistent entries to a Graphiti knowledge graph, which may store sensitive or untrusted content. <br>
Mitigation: Avoid storing secrets or untrusted content as memories, and review content before adding it to the graph. <br>
Risk: A misconfigured Graphiti endpoint could send queries or memory content to the wrong service. <br>
Mitigation: Verify the configured Graphiti endpoint before use with the environment check and Clawdbot or GRAPHITI_URL configuration. <br>


## Reference(s): <br>
- [Graphiti project](https://github.com/getzep/graphiti) <br>
- [ClawHub Graphiti skill page](https://clawhub.ai/emasoudy/skills/graphiti) <br>
- [Environment check reference](references/env-check.sh) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with bash and curl command snippets; Graphiti API responses are JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a reachable Graphiti API plus curl and jq.] <br>

## Skill Version(s): <br>
1.0.1 (source: release evidence and manifest.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
