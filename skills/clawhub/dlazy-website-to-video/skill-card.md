## Description:

website to video, url to video, landing page to video, link to ad, web promo video — capture the site, derive brand, storyboard, voiceover, build, validate on a Remotion template. Use when the user gives a URL (or just pastes a link) and wants a promo, social ad, or product demo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

People creating product, marketing, or social media videos can provide a website URL and use the dLazy website-to-video workflow to make a promotional video or product demo. They can continue work in a project and optionally attach reference files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The CLI stores an API key locally after login.

Mitigation: Use a revocable key, or provide the documented environment variable instead of saving the key; rotate or revoke the key when needed.

Risk: Files attached to a request are uploaded to dLazy media storage.

Mitigation: Attach only files you intend to share with the hosted service.

Risk: Hosted video generation is subject to service data-retention terms and credit costs.

Mitigation: Review the service’s retention terms and expected credit costs before using the workflow.

## Reference(s):

- [dLazy website](https://dlazy.com)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [CLI repository (linked in skill metadata)](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Video files, Text]

**Output Format:** [Generated promotional video assets and text responses delivered through the CLI]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project-scoped sessions; optional attached files are uploaded to the hosted service.]

## Skill Version(s):

1.3.35 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
