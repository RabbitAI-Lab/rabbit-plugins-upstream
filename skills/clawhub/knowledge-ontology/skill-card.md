## Description: <br>
Knowledge Ontology helps agents model local memory as a typed knowledge graph with entity relationships, constraint checks, schema evolution, and graph traversal planning. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent builders use this skill to structure agent memory, model entity relationships, analyze dependencies and impacts, and plan multi-step operations through typed graph commands. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security review found capability mismatches in the documentation, including unrelated paid-feature claims. <br>
Mitigation: Review the documented capabilities before installation and rely only on behavior that is supported by the artifact and release evidence. <br>
Risk: The skill accepts an optional callback URL even though the release is described as primarily local. <br>
Mitigation: Do not provide callback URLs or secrets unless network behavior is clearly documented and constrained for the deployment environment. <br>
Risk: Command examples can create, migrate, or modify local knowledge-graph files. <br>
Mitigation: Review generated commands and run them in a controlled workspace with backups before applying them to important data. <br>


## Reference(s): <br>
- [SkillHub homepage](https://skillhub.cn) <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/knowledge-ontology) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON result structures] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include graph schemas, entity records, validation reports, traversal results, and migration guidance for local knowledge-graph files.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
