## Description: <br>
Moorcheh enables agents to manage Moorcheh namespaces, documents, and semantic text search through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to operate Moorcheh text namespaces and documents, including listing namespaces, searching text, retrieving documents, uploading text documents, and deleting selected documents with confirmation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can change Moorcheh account data, including uploading documents and deleting up to 1,000 documents. <br>
Mitigation: Require clear user confirmation before write or destructive actions, and verify the target namespace and document identifiers before execution. <br>
Risk: The skill operates through a connected OOMOL account. <br>
Mitigation: Use only a trusted connected account and avoid handling raw credentials directly. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-moorcheh) <br>
- [Moorcheh Homepage](https://www.moorcheh.ai) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown with inline bash and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Connector responses include returned data and an execution identifier when actions run.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
