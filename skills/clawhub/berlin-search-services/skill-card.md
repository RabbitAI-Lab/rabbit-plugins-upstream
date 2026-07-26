## Description: <br>
A model-context skill for searching, listing, and retrieving details about Berlin administrative public services. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alinklab](https://clawhub.ai/user/alinklab) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agent developers can use this skill to search Berlin public-service records, list available services, retrieve service details, and check dataset statistics through the provided tool functions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release presents Berlin public-service lookup behavior while security evidence reports unrelated XiaoBenYang/Gaokao integration and required API-key handling. <br>
Mitigation: Review the publisher explanation and request destinations before installation; prefer a cleaned-up release with matching documentation, scoped configuration, secure secret handling, and pinned dependencies. <br>
Risk: The artifact can persist an XBY_APIKEY value in a local .env file. <br>
Mitigation: Do not provide an API key unless the backend and need are trusted, and remove the key from .env when access is no longer needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/alinklab/skills/berlin-search-services) <br>
- [XiaoBenYang API site](https://xiaobenyang.com) <br>
- [XiaoBenYang backend endpoint](https://mcp.xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, Text, JSON, Guidance] <br>
**Output Format:** [Markdown summaries derived from JSON tool responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Tool functions return dictionaries containing success, raw, and message fields.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact frontmatter says 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
