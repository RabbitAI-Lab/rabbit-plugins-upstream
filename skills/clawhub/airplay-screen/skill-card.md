## Description:

Sets up a local AirPlay receiver so an agent can view, follow, read, or save an iPhone or iPad screen mirrored by the user.

This skill is ready for commercial/non-commercial use.

## Publisher:

[feedthedogs](https://clawhub.ai/user/feedthedogs)

### License/Terms of Use:

MIT-0

## Use Case:

External users can mirror an iPhone or iPad to a local receiver so an agent can inspect screen content, follow changes, read text, or save a screenshot.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Mirrored screen content may contain private information and may be processed by the configured AI service.

Mitigation: Mirror only content you are comfortable sharing with that service, use a trusted local network, and stop mirroring when finished.

Risk: Setup installs third-party software and may download several gigabytes; saved screenshots and setup files remain until removed.

Mitigation: Review the setup downloads, and remove saved screenshots and temporary setup files when they are no longer needed.

## Reference(s):

- [airplay-mcp project](https://github.com/feedthedogs/airplay-mcp)
- [UxPlay](https://github.com/FDH2/UxPlay)
- [ipsw](https://github.com/blacktop/ipsw)

## Skill Output:

**Output Type(s):** [Text, Files, Guidance]

**Output Format:** [Screen descriptions and extracted text, with an optional saved screenshot file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can inspect successive frames and save a full-resolution screen image.]

## Skill Version(s):

0.1.4 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
