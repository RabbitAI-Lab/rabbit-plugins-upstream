## Description:

Helps agents use LinkFox gateway scripts and references to call Temu Global Partner promotion APIs for campaign queries, candidate goods, enrollment, operation status, and enrolled goods updates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and seller-operations agents use this skill to work with Temu Global promotion workflows through LinkFox, including querying campaigns, finding candidate goods, enrolling goods, checking operation results, and updating enrolled promotion goods.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles LinkFox and Temu seller credentials and can store Temu access tokens locally.

Mitigation: Use dedicated least-privilege credentials, avoid shared or logged environments, and review local token storage before saving access tokens.

Risk: Generic proxy helpers can provide broad seller-account API access beyond a narrow promotion task.

Mitigation: Prefer the specific promotion scripts and avoid arbitrary proxy helpers unless broad Temu API access is intended and reviewed.

Risk: Promotion enrollment and update operations can change campaign participation, prices, quantities, or deactivate activity goods.

Mitigation: Require explicit user confirmation before enrollment, update, deactivation, payment, or order actions, and verify request parameters before execution.

Risk: Onboarding and billing helpers include payment and order flows outside the core promotion workflow.

Mitigation: Run onboarding or payment-related scripts only when the user specifically requests account setup or billing action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-temu-promotion-global)
- [API reference](references/api.md)
- [Temu access token guide](references/access-token.md)
- [Authorization flow](references/authorization-flow.md)
- [Partner Global promotion catalog](references/partner-global-catalog.md)
- [Promotion API index](references/apis/README.md)
- [Temu Partner Global documentation](https://partner-global.temu.com/documentation?menu_code=7289390cfd724be4a196f11ebe45a896)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, API Calls, JSON, Files, Configuration instructions]

**Output Format:** [Markdown guidance with Python shell commands and JSON API responses written to stdout and local files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full API responses are saved under a linkfox session data directory; large responses are summarized unless --inline is used.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
