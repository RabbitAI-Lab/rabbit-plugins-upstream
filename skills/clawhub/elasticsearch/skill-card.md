## Description: <br>
Elasticsearch helps agents design, query, troubleshoot, and operate Elasticsearch clusters across mappings, Query DSL, aggregations, bulk indexing, performance, security, and cluster health. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, search engineers, and operators use this skill to produce and review Elasticsearch queries, mappings, operational runbooks, troubleshooting steps, and configuration guidance for search and cluster health work. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can store Elasticsearch preferences and cluster context in a local Clawic data directory. <br>
Mitigation: Review the files under ~/Clawic/data/elasticsearch/ and avoid storing secrets or sensitive cluster details there. <br>
Risk: The skill provides recipes for powerful cluster operations, including destructive or high-impact Elasticsearch changes. <br>
Mitigation: Keep destructive_confirm enabled so DELETE, delete-by-query, close, force-merge, and cluster-setting changes are emitted for review before use. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/ivangdavila/skills/elasticsearch) <br>
- [Clawic Skill Homepage](https://clawic.com/skills/elasticsearch) <br>
- [Setup](artifact/setup.md) <br>
- [Mapping](artifact/mapping.md) <br>
- [Queries](artifact/queries.md) <br>
- [Security](artifact/security.md) <br>
- [Incidents](artifact/incidents.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON request bodies, REST or curl examples, code snippets, shell commands, and configuration notes.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May adapt emitted requests to a remembered client, deployment type, Elasticsearch version, and review posture.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
