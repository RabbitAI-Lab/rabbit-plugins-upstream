## Description:

Creates original brand jingles, ad songs, and audio-logo stings from a campaign brief, then generates reviewable music candidates in the requested styles and lengths.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing teams and creators use this skill to draft and generate original music candidates for ads, brand themes, sonic logos, podcast intros, radio spots, and event openings. Review the requested account access and generation costs before connecting or commissioning paid output.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package requires broader Beatra account authorization than its audio workflow appears to need and rejects an audio-only grant.

Mitigation: Review the authorization request before connecting and proceed only if the broader access is acceptable; revoke the device in Beatra Console when shared access is no longer wanted.

Risk: Music and speech generation consume credits, and campaign material is sent to Beatra for processing; installation analytics have no opt-out.

Mitigation: Confirm generation costs in advance, share only campaign material you are permitted to send to Beatra, and account for installation analytics before installing.

## Reference(s):

- [Brand jingle workflow](artifact/references/workflow.md)
- [Updates and security](artifact/references/updates-and-security.md)
- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/brand-jingle-studio)
- [Beatra skill information](https://beatra.ai/skills/brand-jingle-studio)

## Skill Output:

**Output Type(s):** [Audio, Text]

**Output Format:** [Reviewable generated audio candidates with text hooks, lyrics, prompts, and delivery notes; audio details depend on the returned artifact.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generation is paid; requested length is approximate. A spoken tagline and instrumental bed are separate artifacts and are not mixed by this skill.]

## Skill Version(s):

0.2.1 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
