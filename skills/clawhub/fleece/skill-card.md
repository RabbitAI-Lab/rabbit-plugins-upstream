## Description:

Fleece is a credit card research and redemption CLI for looking up rewards rates, fees, bonuses, credits, transfer partners, point valuations, application rules, lounge access, travel protections, wallet gaps, ROI estimates, recommendations, merchant category codes, and award flight or hotel searches.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenyuan99](https://clawhub.ai/user/chenyuan99)

### License/Terms of Use:

MIT

## Use Case:

Developers, agents, and credit card users use Fleece to research US credit card rewards, compare cards, estimate wallet gaps and ROI, and generate award travel search URLs. The skill can guide CLI use, local profile setup, and JSON-based workflows for card and redemption analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release security summary reports that the artifact includes broader iOS, wallet, location, Gmail, and safety-filter-bypass behavior beyond the core CLI.

Mitigation: Install only the components needed for the intended workflow, and review the iOS, wallet, location, Gmail, and agent-instruction files before broad multi-agent installation or app builds.

Risk: The CLI can store card and spending profile data locally in fleece.db.

Mitigation: Use the local profile feature only when comfortable with local storage of card and spending details, and avoid entering full card numbers or other sensitive credentials.

Risk: Live research sends relevant query context to Brave Search when BRAVE_API_KEY-backed commands are used.

Mitigation: Configure BRAVE_API_KEY only when external search is acceptable, and avoid including sensitive personal or account information in search-backed queries.

Risk: The bundled Gmail spend skill can analyze purchase and travel emails to estimate spending behavior.

Mitigation: Keep Gmail access read-only, report aggregates instead of full message content, and require explicit user confirmation before writing Fleece profile updates.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenyuan99/skills/fleece)
- [Fleece website](https://getfleece.io/)
- [fleece-cli on PyPI](https://pypi.org/project/fleece-cli/)
- [PointsYeah](https://www.pointsyeah.com/)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON]

**Output Format:** [Markdown guidance with CLI command examples and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Most CLI commands support --json; live research commands may require BRAVE_API_KEY and profile-aware commands can use local fleece.db data.]

## Skill Version(s):

1.6.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
