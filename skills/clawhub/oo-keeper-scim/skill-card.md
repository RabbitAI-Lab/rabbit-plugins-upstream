## Description: <br>
Keeper SCIM (keepersecurity.com). Use this skill for searching and reading Keeper SCIM users, groups, and service provider configuration through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to inspect Keeper SCIM directory data through OOMOL, including users, groups, and service provider configuration, without handling raw connector credentials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Keeper SCIM results can expose sensitive identity directory data. <br>
Mitigation: Treat returned users, groups, and service provider configuration as sensitive and review list queries before execution. <br>
Risk: The skill depends on an OOMOL-connected account and server-side credential injection. <br>
Mitigation: Complete oo CLI sign-in and Keeper SCIM connection only for trusted OOMOL accounts and providers. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-keeper-scim) <br>
- [OOMOL publisher profile](https://clawhub.ai/user/oomol) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [Keeper SCIM homepage](https://www.keepersecurity.com/) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May return JSON data from the oo CLI connector, including Keeper SCIM user, group, and service provider configuration records.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
