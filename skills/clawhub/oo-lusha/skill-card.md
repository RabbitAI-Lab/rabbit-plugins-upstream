## Description: <br>
Lusha helps agents search, read, and enrich Lusha company and contact data through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to search Lusha company and contact previews, enrich returned records, and inspect account usage through an OOMOL-connected Lusha account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Contact enrichment can reveal personal contact details. <br>
Mitigation: Use the skill only for Lusha queries the user is authorized to perform. <br>
Risk: Search and enrichment actions may consume Lusha or OOMOL account credits. <br>
Mitigation: Check account usage when cost is relevant and avoid retrying after billing or insufficient-credit errors until the account is recharged. <br>
Risk: The skill depends on OOMOL as the access path for Lusha. <br>
Mitigation: Install it only when the user intends to use OOMOL-managed Lusha access and server-side credential handling. <br>


## Reference(s): <br>
- [Lusha homepage](https://www.lusha.com) <br>
- [oo CLI repository](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-lusha) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Connector responses are JSON objects with data and meta.executionId fields.] <br>

## Skill Version(s): <br>
1.0.1 (source: server evidence release.version and skill metadata.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
