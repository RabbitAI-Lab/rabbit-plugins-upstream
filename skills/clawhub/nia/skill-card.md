## Description: <br>
Index and search code repositories, documentation, research papers, HuggingFace datasets, local folders, and packages with Nia AI. Includes Oracle autonomous research, dependency analysis, context sharing, and code advisor. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[arlanrakh](https://clawhub.ai/user/arlanrakh) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and engineers use this skill to index, search, and retrieve context from repositories, documentation, papers, datasets, packages, and selected local files through Nia's cloud API. It supports grounded code research, dependency analysis, source organization, and code advice workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Selected local files, dependency manifests, search queries, and supplied database connection or query details can be sent to Nia's cloud API. <br>
Mitigation: Review inputs before running folder, advisor, dependency, and database commands; avoid secret-heavy directories and sensitive manifests. <br>
Risk: Database import and preview commands can expose database connection strings and query results to the service. <br>
Mitigation: Use least-privilege database credentials and run only scoped, reviewed queries. <br>
Risk: The API key is read from ~/.config/nia/api_key and authorizes requests to the Nia service. <br>
Mitigation: Store the key with restrictive file permissions and rotate it if the local machine or file is exposed. <br>


## Reference(s): <br>
- [Nia website](https://trynia.ai) <br>
- [ClawHub skill page](https://clawhub.ai/arlanrakh/skills/nia) <br>
- [Skill README](artifact/README.md) <br>
- [Skill definition and usage guide](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API Calls, JSON, Markdown, Code, Configuration instructions, Guidance] <br>
**Output Format:** [Shell command output, usually JSON or streamed text, with Markdown guidance in the skill documentation] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl, jq, and a Nia API key stored at ~/.config/nia/api_key.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
