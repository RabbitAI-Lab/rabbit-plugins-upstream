## Description:

Generate or edit images, video, audio, and 3D assets with Luxin, with hosted media links and job and cost details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[danielgwilson](https://clawhub.ai/user/danielgwilson)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and developers use Luxin to create or edit image, video, audio, and 3D media, then retrieve hosted media links and job details. It is useful when a task needs a chosen media model or a cost estimate before generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The refresh workflow can update unrelated installed skills and introduce changing code and guidance.

Mitigation: Restrict updates to Luxin and inspect the proposed changes before applying them.

Risk: Media URLs are public, so confidential media could be exposed.

Mitigation: Avoid uploading or generating confidential media for use with public URLs.

Risk: Media generation and wallet payments can incur costs.

Mitigation: Use a reviewed CLI version and set spending limits before authorizing wallet payments.

## Reference(s):

- [Luxin CLI documentation](https://luxin.sh/cli.md)
- [Luxin LLM contract](https://luxin.sh/llms.txt)
- [Luxin skill guidance](https://luxin.sh/skill.md)
- [Luxin hosted API](https://api.luxin.sh)

## Skill Output:

**Output Type(s):** [Image, video, audio, and 3D media assets, Hosted media URLs, JSON job and cost details, Usage guidance]

**Output Format:** [Hosted media files and URLs with JSON metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may include a recoverable job ID, asset IDs, and a cost receipt.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
