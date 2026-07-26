## Description: <br>
Interact with Apollo.io REST API (people/org enrichment, search, lists). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jhumanj](https://clawhub.ai/user/jhumanj) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to query Apollo.io for people and organization search, enrichment, and list-related API workflows from an agent session. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prospecting searches, domains, and enrichment requests are sent to Apollo.io with the user's Apollo API key. <br>
Mitigation: Install only when this data sharing is acceptable for the intended workflow and use a least-privileged Apollo key where possible. <br>
Risk: A local apollo.env file contains API configuration used by the scripts. <br>
Mitigation: Keep apollo.env private, verify APOLLO_BASE_URL before use, and limit the file to trusted variable assignments. <br>


## Reference(s): <br>
- [Apollo.io API base URL](https://api.apollo.io) <br>
- [ClawHub Apollo skill page](https://clawhub.ai/jhumanj/skills/apollo) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON API responses from Apollo.io scripts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses APOLLO_BASE_URL and APOLLO_API_KEY from a local Apollo configuration file.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
