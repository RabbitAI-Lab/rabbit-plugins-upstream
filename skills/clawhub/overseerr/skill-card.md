## Description: <br>
Request movies/TV and monitor request status via the Overseerr API (stable Overseerr, not the beta Seerr rewrite). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[j1philli](https://clawhub.ai/user/j1philli) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and self-hosted media server operators use this skill to search Overseerr, create movie or TV requests, inspect request records, and monitor request-status changes through the Overseerr API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses an Overseerr API key that can read and create requests. <br>
Mitigation: Install it only for trusted Overseerr instances and protect the OVERSEERR_API_KEY value in agent configuration and logs. <br>
Risk: The request command chooses the first search result for a title, which can create the wrong media request for ambiguous titles. <br>
Mitigation: Run search first for ambiguous titles and use more specific query terms before creating a request. <br>
Risk: Monitor output can include media request metadata that may be sensitive in shared logs. <br>
Mitigation: Avoid routing monitor output to shared logs or public channels unless that metadata is acceptable to disclose. <br>


## Reference(s): <br>
- [Overseerr project homepage](https://overseerr.dev/) <br>
- [ClawHub Overseerr skill page](https://clawhub.ai/j1philli/skills/overseerr) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance, json] <br>
**Output Format:** [Markdown guidance with shell commands and JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires node, OVERSEERR_URL, and OVERSEERR_API_KEY; commands can read and create requests in the configured Overseerr instance.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
