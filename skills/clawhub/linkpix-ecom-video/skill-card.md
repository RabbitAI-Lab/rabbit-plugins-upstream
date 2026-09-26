## Description:

Routes e-commerce video requests to LinkPix qhkit workflows for product-showcase videos, promotional shorts, review-style videos, scripts, storyboards, and multi-image video generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and agents use this skill to choose LinkPix/qhkit commands and parameters for generating e-commerce videos from product prompts, images, or draft storyboards. The skill supports setup, cost estimation, job submission, status polling, and delivery guidance for qhkit video outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can install and invoke the qhkit CLI from the @iqinghu/qhkit npm package.

Mitigation: Install only when LinkPix/qhkit video generation is intended, review the npm package source and trust posture, and avoid unpinned npx use where possible.

Risk: The qhkit workflow uses an API token and may upload local images or videos to the service.

Mitigation: Protect qhkit credentials and confirm that any provided media is appropriate to upload before submitting a generation task.

Risk: Video generation can spend service credits and submitted tasks may not be cancelable.

Mitigation: Run supported estimate commands or confirm expected cost before generation, tell the user the task ID after submission, and preserve it for status checks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-ecom-video)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with inline bash commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include qhkit task IDs, polling guidance, generated media URLs, and credit estimates when an agent executes the CLI.]

## Skill Version(s):

0.1.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
