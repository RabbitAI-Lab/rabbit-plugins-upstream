## Description:

Supports Temu Global fulfillment workflows for Buy-Shipping labels, cooperative warehouse fulfillment, self-fulfilled shipping, and tracking through 23 LinkFox gateway API wrappers, excluding Scan Form workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Temu sellers, fulfillment operators, and developers use this skill to create, update, confirm, cancel, retrieve, and track Temu Global fulfillment shipments through LinkFox gateway scripts and API guidance.

### Deployment Geography for Use:

Global, for Temu Global fulfillment workflows outside the US and EU variants covered by separate skills.

## Known Risks and Mitigations:

Risk: A third-party LinkFox gateway receives Temu fulfillment data, LinkFox API keys, and Temu access tokens.

Mitigation: Install only when this data flow is acceptable, treat all tokens like passwords, and limit token sharing to the intended Temu store and workflow.

Risk: The skill can create, confirm, update, or cancel shipment and fulfillment records.

Mitigation: Require explicit human confirmation before actions that change shipment, pickup, cooperative warehouse, billing, or payment state.

Risk: Full fulfillment responses are saved locally and may include operational or credential-adjacent data.

Mitigation: Review files written under linkfox session data paths, control local file access, and remove retained responses when they are no longer needed.

Risk: Temu access tokens may be stored locally and some helper output can reveal token material if used without masking.

Mitigation: Prefer masked token listing, protect ~/.linkfox token files, and rotate any token that may have been exposed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-temu-fulfillment-global)
- [Temu Partner Global Fulfillment Documentation](https://partner-global.temu.com/documentation?menu_code=7289390cfd724be4a196f11ebe45a896)
- [API Reference](references/api.md)
- [Partner Global Catalog](references/partner-global-catalog.md)
- [Temu Access Token Authorization](references/access-token.md)
- [Authentication and Billing Onboarding](references/onboarding.md)
- [Endpoint Reference Index](references/apis/README.md)

## Skill Output:

**Output Type(s):** [API Calls, Files, Shell commands, Configuration instructions, Guidance]

**Output Format:** [JSON responses saved to local files with stdout JSON or summaries, plus Markdown guidance and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full responses are persisted under a linkfox date/session data path; responses over 8 KB are summarized unless --inline is used.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
