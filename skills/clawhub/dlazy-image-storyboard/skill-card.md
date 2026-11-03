## Description:

A professional storyboard skill for film, advertising, short video, and educational narrative scenarios, built around a strict 'plan first, render later' flow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Filmmakers, advertisers, short-video creators, and educators use it to turn creative briefs into structured cinematic or narrative storyboards, review character and script plans, then generate panels and assemble print or PDF layouts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media are sent to dLazy services for generation, and use may incur charges.

Mitigation: Use the service only if you trust dLazy with those prompts and files; review media before upload and account for generation charges.

Risk: The API key is stored in the local dLazy CLI configuration, and the exact external CLI package was not audited in this review.

Mitigation: Protect the stored key and rotate or revoke it when needed. Review the package version before installation; the release metadata pins @dlazy/cli@1.2.3.

## Reference(s):

- [dLazy CLI project page](https://github.com/dlazy-ai/cli)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Images, Image URLs]

**Output Format:** [Markdown storyboard plans and panel prompts, CLI command examples, and generated image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [User confirmation gates structure the workflow; image generation uses an authenticated dLazy account and may incur charges.]

## Skill Version(s):

1.3.39 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
