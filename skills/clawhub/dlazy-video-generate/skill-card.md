## Description:

Automatically selects a dLazy video model to generate videos from text or reference media, including image animation, frame-guided clips, digital-human video, and lip-sync.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use the skill to create short videos from prompts, images, or other reference media, and to generate digital-human or lip-synced videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media are sent to dLazy hosted services, and generation may incur usage charges.

Mitigation: Avoid uploading sensitive files and review applicable service terms and costs before generating.

Risk: The dLazy API key is stored in local CLI configuration when using the login flow.

Mitigation: Protect access to the key and rotate or revoke it from the dLazy dashboard if needed.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/dlazyai/skills/dlazy-video-generate)
- [dLazy service](https://dlazy.com)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [CLI source link (skill metadata)](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Generated video media, Hosted video URLs, JSON result summaries]

**Output Format:** [Video media with a JSON result envelope]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Available media, duration, and quality depend on the selected model and request.]

## Skill Version(s):

1.4.36 (source: server-resolved release metadata; artifact frontmatter lists 1.4.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
