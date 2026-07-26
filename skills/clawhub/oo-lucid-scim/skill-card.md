## Description: <br>
Lucid SCIM helps agents inspect schemas and run read-only OOMOL connector actions for Lucid SCIM users, groups, teams, and service provider configuration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, administrators, and support agents use this skill to search and read Lucid SCIM directory information through an OOMOL-connected account without handling raw Lucid SCIM tokens. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Lucid SCIM user, group, and team lookup results can contain sensitive organization directory data. <br>
Mitigation: Review the OOMOL Lucid SCIM connection and scopes, and share retrieved directory data only with authorized users. <br>
Risk: The skill depends on a valid OOMOL connection, account authentication, and sufficient billing or scopes. <br>
Mitigation: Use the live connector schema before running an action and resolve authentication, scope, connection, or billing errors through the documented OOMOL setup flow. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-lucid-scim) <br>
- [Lucid SCIM homepage](https://lucid.co) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL Lucid SCIM connection page](https://console.oomol.com/app-connections?provider=lucid_scim) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON connector payloads or results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the oo CLI, an authenticated OOMOL account, and a connected Lucid SCIM app connection; the available actions in the artifact are read-only.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
