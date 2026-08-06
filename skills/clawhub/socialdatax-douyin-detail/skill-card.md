## Description:

Provides SocialDataX-powered Douyin work detail lookups for videos and image/text posts, including content details, interaction metrics, and media metadata.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and content researchers use this skill to retrieve structured Douyin work details from an aweme ID or content URL through SocialDataX. It supports review of returned content, author and publish metadata, interaction counts, images, video, music, and media summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill invokes the external socialdatax-skills npm package and SocialDataX API for Douyin detail lookups.

Mitigation: Install and run it only when SocialDataX-backed Douyin detail lookup is intended, and review the command before execution.

Risk: Detail calls require SOCIALDATAX_API_KEY in the runtime environment.

Mitigation: Provide the API key only through the runtime environment and use the official SocialDataX access page for key management.

Risk: Optional media download commands can write files to local output paths.

Mitigation: Use explicit output files or directories and review returned media URLs before saving content locally.

## Reference(s):

- [SocialDataX AI API access](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/socialdatax-douyin-detail)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with CLI commands and JSON response summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SOCIALDATAX_API_KEY for detail API calls; optional media saving writes only to requested local paths.]

## Skill Version(s):

0.1.16 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
