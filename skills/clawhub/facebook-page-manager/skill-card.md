## Description: <br>
Manage Facebook Pages via Meta Graph API. Post content (text, photos, links), list posts, manage comments (list/reply/hide/delete). Use when user wants to publish to Facebook Page, check Page posts, or handle comments. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[longmaba](https://clawhub.ai/user/longmaba) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, operators, and page managers can use this skill to configure Meta Graph API access and manage Facebook Page posts and comments from an agent-guided CLI workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Facebook Page tokens can publish posts, delete posts, and moderate comments. <br>
Mitigation: Install only when those permissions are intended, protect stored tokens, rotate or revoke tokens periodically, and confirm target page, post, and comment IDs before write or delete actions. <br>
Risk: The release includes undisclosed X-to-Facebook digest scripts that use X session cookies and can publish selected content to a Facebook Page. <br>
Mitigation: Do not provide AUTH_TOKEN or CT0 cookies unless that workflow is intentional; review or remove the x_digest scripts before deployment. <br>


## Reference(s): <br>
- [Graph API Reference](references/graph-api.md) <br>
- [Meta App Dashboard](https://developers.facebook.com/apps/) <br>
- [ClawHub Skill Page](https://clawhub.ai/longmaba/skills/facebook-page-manager) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, code] <br>
**Output Format:** [Markdown guidance with shell commands and JSON CLI responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces commands and configuration guidance for Meta OAuth setup, Facebook Page posting, post listing, and comment moderation.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
