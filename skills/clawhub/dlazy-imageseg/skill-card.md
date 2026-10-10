## Description:

Separates image foregrounds from backgrounds and returns a transparent-background image URL for product photos, portraits, and compositions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to remove image backgrounds for product imagery, character cutouts, and visual compositions through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Images supplied to the CLI may be uploaded to dLazy for processing.

Mitigation: Obtain permission before submitting sensitive images and review dLazy's data handling.

Risk: Authentication may save a dLazy API key locally.

Mitigation: Protect the local credential and rotate or revoke it if exposed.

Risk: The documented image option and example command disagree.

Mitigation: Check `dlazy imageseg -h` before invoking the CLI.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-imageseg)
- [dLazy CLI source (skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Image URLs]

**Output Format:** [Markdown instructions and JSON result with a hosted image URL]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save the resulting image locally or return an asynchronous task ID.]

## Skill Version(s):

1.3.27 (source: ClawHub release evidence; artifact frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
