## Description: <br>
Provides chemical lookups by substance name or CAS number and returns fields such as molecular formula, molecular weight, and CAS identifiers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alinklab](https://clawhub.ai/user/alinklab) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Agents use this skill to answer chemical information questions for users by calling a configured third-party chemical lookup service after the user supplies an XBY API key. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release evidence says the skill claims PubChem use but actually calls the XiaoBenYang MCP service. <br>
Mitigation: Use it only when the user intends to trust that third-party provider, and verify important chemical results against an authoritative source before relying on them. <br>
Risk: The release evidence says the skill asks for an XBY API key and stores it in a local plaintext .env file. <br>
Mitigation: Avoid sensitive chemical queries, protect the .env file, and remove or rotate the API key when it is no longer needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/alinklab/skills/pubchem) <br>
- [XiaoBenYang API key provider](https://xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Guidance] <br>
**Output Format:** [Markdown summary of structured JSON tool responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an XBY API key and may return upstream service errors or raw provider payloads.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact frontmatter is 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
