## Description:

This skill helps agents manage Shopee store videos and video analytics through LinkFox-wrapped Shopee Open API Video endpoints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce operators and developers use this skill to publish, inspect, edit, delete, and analyze Shopee store videos for already authorized stores.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can publish, edit, or delete Shopee store video content.

Mitigation: Confirm any publishing, editing, or deletion action with the store owner before executing it.

Risk: Full API responses may be saved locally and can contain store or analytics data.

Mitigation: Store outputs in an approved workspace, limit sharing, and periodically remove saved response files that are no longer needed.

Risk: The skill may guide LinkFox account login, API key handling, billing, or payment flows.

Mitigation: Do not share OTPs or API keys casually, and review payment or billing actions before proceeding.

Risk: Environment URL overrides can redirect requests away from the expected LinkFox gateway.

Mitigation: Keep LINKFOX_* URL overrides unset unless the target endpoint is trusted.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-shopee-store-video)
- [Shopee video API index](https://open.shopee.com/documents/v2/v2.video.get_cover_list?module=129&type=1)
- [API reference](references/api.md)
- [Onboarding and account setup](references/onboarding.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance, shell command examples, JSON API responses, and saved JSON response files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full API responses are saved locally; large responses are summarized unless inline output is requested.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
