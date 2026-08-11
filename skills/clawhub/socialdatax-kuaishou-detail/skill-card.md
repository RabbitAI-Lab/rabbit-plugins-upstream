## Description:

This skill helps agents retrieve and summarize Kuaishou/Kwai work details, interaction metrics, and content-analysis fields through SocialDataX.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect a Kuaishou work by photo ID or URL and return factual fields such as title, author, publish time, interaction counts, images, and media details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Kuaishou URLs, IDs, and requested detail data are sent to SocialDataX using the user's SOCIALDATAX_API_KEY.

Mitigation: Install and use the skill only when the user is comfortable providing that API key and sharing those Kuaishou inputs with SocialDataX.

Risk: Optional media download commands can save files to local output paths selected by the user.

Mitigation: Review the requested output path before running download commands and avoid saving media into sensitive directories.

## Reference(s):

- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/socialdatax-kuaishou-detail)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SOCIALDATAX_API_KEY for detail requests; optional media download commands write to user-selected local paths.]

## Skill Version(s):

0.1.17 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
