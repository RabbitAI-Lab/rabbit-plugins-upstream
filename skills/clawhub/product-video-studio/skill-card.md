## Description:

Turns a product photo and merchant-supplied details into a short vertical product video with spoken narration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Merchants and marketing teams use this skill to turn a product photo and verified selling points into a narrated product clip for listings, launches, and social posts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Beatra account access and paid video generation can consume credits.

Mitigation: Review the account and billing terms; approve each priced preparation step and the final video estimate before submitting.

Risk: The installation reports local installation and coarse runtime details to Beatra.

Mitigation: Review the installation registration and privacy implications before connecting an account.

Risk: The bundled client can automatically replace package files without a separate prompt.

Mitigation: Install only if you trust Beatra's update channel; disable automatic updates with the documented update command if needed.

Risk: Uninstalling the last Beatra skill can revoke the shared device connection and delete its local state.

Mitigation: Check which other Beatra skills use the connection before uninstalling and follow the documented uninstall workflow.

## Reference(s):

- [ClawHub release](https://clawhub.ai/beatra-ai/skills/product-video-studio)
- [Beatra product page](https://beatra.ai/skills/product-video-studio)
- [Commerce video workflow](artifact/references/workflow.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [Video, Text]

**Output Format:** [Narrated vertical video artifact with a text report of model, dimensions, duration, and charged credits]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One clip of up to 15 seconds; paid generation requires account credits.]

## Skill Version(s):

0.2.0 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
