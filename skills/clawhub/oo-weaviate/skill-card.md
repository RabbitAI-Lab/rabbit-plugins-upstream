## Description: <br>
The Weaviate skill guides agents to search and read Weaviate data through the OOMOL `oo` CLI instead of calling the API directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to inspect Weaviate instance metadata, collection schemas, and objects through an OOMOL-connected Weaviate account. It is suited for read-only data discovery and retrieval workflows where the agent should use the `oo` connector instead of handling raw Weaviate credentials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Read actions can expose Weaviate schemas, metadata, and object contents to the agent through the OOMOL connector. <br>
Mitigation: Use the skill only with accounts and collections the agent is permitted to inspect, and scope collection, object, tenant, and include options to the user's request. <br>
Risk: The skill relies on OOMOL as an intermediary for Weaviate access. <br>
Mitigation: Install and use it only when OOMOL-mediated access is intended, and review CLI installation, sign-in, and app-connection steps before use. <br>
Risk: Incorrect connector payloads can query the wrong collection, tenant, or object. <br>
Mitigation: Inspect the live action schema with `oo connector schema` before constructing each `oo connector run` payload. <br>


## Reference(s): <br>
- [Weaviate homepage](https://weaviate.io) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON payload instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include connector responses shaped as JSON objects containing `data` and `meta.executionId`.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
