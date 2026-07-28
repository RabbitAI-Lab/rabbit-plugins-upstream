## Description: <br>
Query alltrails.com trail, review, photo, weather, saved-list, completed-trail, and activity-feed data from a shell with the fpx CLI through a signed-in browser tab. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to make read-only AllTrails lookups and account-scoped queries from shell workflows when the alltrails-mcp server is not installed or not desired. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can use a signed-in AllTrails browser session to read account-linked saved lists, completed trails, and activity-feed data. <br>
Mitigation: Use it only for explicit user-requested lookups, review shell commands before account-scoped calls, and avoid running it from shared browser profiles. <br>
Risk: The fpx browser pairing can persist after initial approval. <br>
Mitigation: Remove or rotate the fpx pairing when the workflow is finished or when browser access should no longer be available. <br>
Risk: Missing or stale x-at-key captures can cause failed requests or misleading non-JSON challenge responses. <br>
Mitigation: Recapture the x-at-key from a live AllTrails tab and verify returned bodies as JSON before using results. <br>


## Reference(s): <br>
- [AllTrails endpoints for fpx](references/endpoints.md) <br>
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/alltrails-fpx) <br>
- [Publisher profile](https://clawhub.ai/user/chrischall) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance, JSON] <br>
**Output Format:** [Markdown with shell commands and JSON response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only examples require fpx, the Transporter browser extension, a signed-in AllTrails tab for account-scoped calls, and a live x-at-key header capture.] <br>

## Skill Version(s): <br>
2.1.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
