## Description:

Temu欧洲站-促销 helps agents call LinkFox-forwarded Temu Partner EU promotion APIs for campaign queries, candidate goods, enrollment, operation status, and enrolled goods updates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, operators, and developers use this skill to inspect and manage Temu Partner EU promotion activity workflows through LinkFox gateway scripts and API references.

### Deployment Geography for Use:

Europe (Temu Partner EU)

## Known Risks and Mitigations:

Risk: The skill handles Temu merchant access tokens and a LinkFox account key.

Mitigation: Avoid pasting live tokens into chat or shell history, scope access to trusted users, and keep token files out of shared folders and version control.

Risk: The skill supports broad proxy calls and gateway override environment variables.

Mitigation: Use the default trusted gateway unless a reviewed deployment requires otherwise, and check the target host before setting override variables.

Risk: Promotion changes, including enrollment updates or deactivation, can affect live merchant operations.

Mitigation: Review activity IDs, goods IDs, operation types, and prices before running scripts that modify promotion state.

Risk: Local response archives may contain merchant or promotion data.

Mitigation: Store outputs in an appropriate workspace, restrict access to generated response files, and remove sensitive archives when no longer needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-temu-promotion-eu)
- [API Reference](references/api.md)
- [Temu Access Token Guide](references/access-token.md)
- [Partner EU Promotion Catalog](references/partner-eu-catalog.md)
- [Promotion API Index](references/apis/README.md)
- [Temu Partner EU Documentation](https://partner-eu.temu.com/documentation?menu_code=7289390cfd724be4a196f11ebe45a896)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, JSON, files, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full API responses are saved locally; large responses may be summarized unless inline output is requested.]

## Skill Version(s):

1.0.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
