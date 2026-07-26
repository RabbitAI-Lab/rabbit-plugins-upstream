## Description: <br>
An unofficial Cellosaurus MCP-style skill for searching cell lines, retrieving accession-level details, finding disease or tissue associations, and checking Cellosaurus release information. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alinklab](https://clawhub.ai/user/alinklab) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, researchers, and agent users can use this skill to query Cellosaurus-style cell-line data by search term, accession, disease, tissue, or release metadata. Because server evidence marks the package suspicious, users should review the remote service dependency and credential handling before deployment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Server evidence reports a suspicious mismatch between the advertised Cellosaurus purpose and Xiaobenyang/Gaokao-related remote service behavior. <br>
Mitigation: Install only after reviewing the package and confirming that the remote endpoint, tool names, and credential variables match the intended Cellosaurus use case. <br>
Risk: Queries and API credentials may be sent to a third-party Xiaobenyang backend. <br>
Mitigation: Use only credentials intended for that service, avoid sensitive query content, and proceed only if the backend is trusted for the deployment context. <br>
Risk: The skill persists an API key in a local .env file. <br>
Mitigation: Protect the local environment file, rotate exposed credentials, and remove stored keys when the skill is no longer needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/alinklab/skills/cellosaurus) <br>
- [Xiaobenyang API key service](https://xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, API results, guidance] <br>
**Output Format:** [Markdown summaries of dictionary or JSON-like tool results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Tool calls may require user-provided query, accession, disease, tissue, field, pagination, or sort parameters.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
