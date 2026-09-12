## Description:

This skill helps agents use Qinghu AI's qhkit CLI to estimate, generate, monitor, and deliver ecommerce video ad assets from product prompts and images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, marketers, and agent users use this skill to create batches of paid-social and information-feed video ad assets from product information and uploaded media. The skill is also used to estimate credit cost, poll generation status, and return completed video URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill directs agents to install and run the mutable external qhkit CLI.

Mitigation: Confirm the exact @iqinghu/qhkit package version and npm registry before installation or upgrade, and avoid running npm with elevated privileges.

Risk: Video generation may upload user-provided product images or other media.

Mitigation: Provide only the media files needed for the specific ad generation task and avoid unnecessary sensitive or proprietary assets.

Risk: Generation can spend Qinghu service credits.

Mitigation: Run qhkit video estimate when supported and require explicit user approval before submitting any credit-spending generation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-video-ad-assets)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with bash commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include qhkit task IDs, polling status, generated video URLs, and credit estimates or charges when returned by the CLI.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
