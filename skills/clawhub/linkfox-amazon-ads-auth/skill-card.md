## Description:

Helps agents generate Amazon Ads OAuth authorization URLs, list authorized advertising profiles, refresh authorization status, and guide LinkFox credential or billing onboarding when needed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, agencies, and developers use this skill to connect Amazon Ads accounts through LinkFox, identify the correct profileId for downstream advertising workflows, and check or refresh authorization status.

### Deployment Geography for Use:

Global; Amazon Ads operations are scoped to the skill's NA, EU, and FE region options.

## Known Risks and Mitigations:

Risk: The skill handles LinkFox API credentials and Amazon Ads authorization data.

Mitigation: Install only in trusted agent environments, keep API keys private, and avoid exposing OAuth links or authorization output on shared machines.

Risk: The security review notes broad LinkFox account, API key, billing, feedback, and persistence behavior that deserves manual review.

Mitigation: Review the LinkFox onboarding and billing flow before use, and confirm that these account-management behaviors are acceptable for the deployment.

Risk: Base-url environment variables can redirect requests away from the normal LinkFox gateway.

Mitigation: Keep LINKFOX_TOOL_GATEWAY and related base-url variables pointed only at trusted LinkFox hosts.

Risk: Saved response files may retain sensitive authorization or account metadata.

Mitigation: Review and clean locally saved LinkFox response files according to the user's data-retention requirements.

## Reference(s):

- [API Reference](artifact/references/api.md)
- [Onboarding Reference](artifact/references/onboarding.md)
- [Amazon Ads Console](https://advertising.amazon.com/)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON responses, saved response files, authorization URLs, and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Large responses may be summarized unless inline output is requested; token-status helpers are intended to show status metadata instead of raw tokens.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
