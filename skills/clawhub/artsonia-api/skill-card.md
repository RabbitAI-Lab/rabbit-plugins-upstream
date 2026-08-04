## Description: <br>
Access Artsonia student-art portfolios, comments, fans, teacher feedback, profile data, and artwork downloads from a shell using curl against server-rendered member pages. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and authorized Artsonia account holders use this skill to script account-scoped reads, inspect student artwork data, and perform documented Artsonia member-site actions without running the MCP server. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can access student artwork, profile contact details, cookies, and private portfolio data. <br>
Mitigation: Use it only for Artsonia accounts and student portfolios you are authorized to access, and protect or delete local cookies and downloaded files when finished. <br>
Risk: The skill documents account-changing actions, including posting comments, sending fan invites, marking feedback read, and changing notification settings. <br>
Mitigation: Require explicit user confirmation before each write action and re-read the affected page afterward to verify the result. <br>
Risk: Artwork images may be downloadable from the public CDN without authentication, including private pieces. <br>
Mitigation: Avoid bulk downloads unless necessary and treat downloaded images as sensitive content. <br>


## Reference(s): <br>
- [Endpoint Recipes](artifact/references/endpoints.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/chrischall/skills/artsonia-api) <br>
- [Artsonia](https://www.artsonia.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Code, Configuration] <br>
**Output Format:** [Markdown guidance with inline shell commands and parsing examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes curl flows, endpoint paths, parser usage, verification checks, and account-action caveats.] <br>

## Skill Version(s): <br>
0.8.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
