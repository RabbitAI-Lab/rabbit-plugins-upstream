## Description:

MotuArt Color Engine helps agents process portrait images through MotuArt's hosted HTTP API for color grading, skin-tone correction, identity-preserving smoothing, mask export, approved clothing replacement, AI headshots, and ID/passport/headshot/avatar production.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chancipher](https://clawhub.ai/user/chancipher)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to run MotuArt Color Engine workflows for portrait grading, retouching, mask export, approved outfit replacement, AI headshot generation, ID-photo cropping, compliance checks, upload optimization, and print-sheet preparation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive portrait, headshot, or ID-photo images may be uploaded to MotuArt's remote service.

Mitigation: Use explicit invocation and user confirmation before uploads, and confirm the endpoint, account, privacy, retention, and credit expectations before processing sensitive images.

Risk: The skill requires an API key for private processing endpoints.

Mitigation: Store the key in the user's environment, send it only as an API authentication header, and request only the scopes needed for the selected workflow.

Risk: Processing calls can consume account credits.

Mitigation: Confirm credit expectations before processing and surface insufficient-credit responses instead of retrying unchanged requests.

## Reference(s):

- [MotuArt Color Engine API Reference](references/api.md)
- [AI Headshots API](references/headshots-api.md)
- [MotuArt Color Engine Crop Specs Overview](references/crop-specs.md)
- [MotuArt Color Engine Styles Overview](references/styles.md)
- [MotuArt Color Engine Developers](https://mce.motu.art/developers)
- [ClawHub Skill Page](https://clawhub.ai/chancipher/skills/motu-color-engine)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, files, guidance]

**Output Format:** [Markdown guidance with shell commands and script-produced files such as images, masks, JSON reports, and workflow state.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call a remote API, create local output files, and require an API key with task-specific scopes.]

## Skill Version(s):

1.0.9 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
