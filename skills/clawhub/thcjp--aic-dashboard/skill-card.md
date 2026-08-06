## Description: <br>
AIC Dashboard helps agents provide a local, token-protected read-only dashboard for recent inbox.jsonl messages and browser session status. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and teams use this skill to view AIC mail and browser-session status from local data files without sending mail, controlling a browser, or storing credentials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release is documented as a local read-only dashboard, but the declared permissions are broader than that purpose requires. <br>
Mitigation: Review the skill before installing and avoid granting write or broad command authority unless the publisher clarifies why a read-only dashboard needs it. <br>
Risk: Dashboard access depends on a token that may be shared through URLs. <br>
Mitigation: Set a strong DASHBOARD_TOKEN, keep the service bound to 127.0.0.1 unless LAN sharing is intentional, and avoid sharing URLs that contain the token. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and configuration values] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Local read-only dashboard guidance; no public provenance reference is available for this release.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence; artifact frontmatter reports 1.8.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
