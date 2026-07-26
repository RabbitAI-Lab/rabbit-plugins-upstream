## Description: <br>
DocuGenerate operates DocuGenerate through an OOMOL-connected account to list templates and documents, generate documents from templates, retrieve documents, rename documents, and delete documents. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to operate DocuGenerate from an OOMOL-connected account, including reading templates and documents, generating documents with JSON merge data, renaming documents, and deleting documents after confirmation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can act on a DocuGenerate account, including generating, renaming, and permanently deleting documents. <br>
Mitigation: Approve write or delete commands only after checking the exact template, document ID, and payload. <br>
Risk: First-time setup may require installing the oo CLI. <br>
Mitigation: Install the oo CLI only from the documented OOMOL source when setup is needed. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-docugenerate) <br>
- [DocuGenerate Homepage](https://www.docugenerate.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Connector responses are JSON objects containing data and meta.executionId.] <br>

## Skill Version(s): <br>
1.0.0 (source: server evidence release.version and SKILL.md metadata.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
