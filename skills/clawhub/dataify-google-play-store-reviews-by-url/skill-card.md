## Description:

Collects Google Play app reviews from a known Play Store app URL; it is not intended for app discovery, rankings, or general Google Play search.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and data operators use this skill to collect Google Play review or app-information data from known Play Store app URLs through Dataify and return the completed collection result.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses DATAIFY_API_TOKEN and could expose credentials if users paste or print the token.

Mitigation: Configure the token through the environment, verify only that it exists, and never include the token value in chat or generated commands.

Risk: Requests may spend Dataify credits and send the target URL and selected parameters to Dataify.

Mitigation: Use the skill only for intended Google Play review or app-information collection from known URLs, and confirm any high-volume or scope-changing choices before submission.

Risk: The skill is scoped to known Play Store app URLs and may be misleading if used for discovery, rankings, or broad Google Play search.

Mitigation: Ask for a specific Play Store app URL and avoid using documentation examples as substitute user input.

## Reference(s):

- [Tool parameter catalog](references/tool-params.json)
- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-google-play-store-reviews-by-url)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance, JSON]

**Output Format:** [Markdown with shell commands and JSON results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May submit Dataify Builder tasks, wait for asynchronous completion, and summarize large JSON payloads while preserving access to the raw result.]

## Skill Version(s):

1.3.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
