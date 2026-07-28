## Description: <br>
FullContact connector skill for enriching company profiles, enriching person profiles, and verifying activity, matches, and identity signals through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and business users use this skill to run FullContact enrichment and verification actions through their OOMOL-connected account without handling raw API tokens. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Person or company identifiers may be sent to FullContact through OOMOL during enrichment or verification. <br>
Mitigation: Review each payload before execution and exclude sensitive personal data that is not needed for the requested task. <br>
Risk: The skill depends on the OOMOL CLI, account sign-in, billing, and a connected FullContact credential. <br>
Mitigation: Treat CLI installation, login, billing, and FullContact connection as account setup steps; perform them only when required and with the user's approval. <br>


## Reference(s): <br>
- [FullContact homepage](https://www.fullcontact.com/) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-full-contact) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before execution; connector responses include FullContact enrichment or verification data when actions succeed.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
