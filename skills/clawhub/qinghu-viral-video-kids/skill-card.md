## Description:

This skill helps agents use Qinghu AI's LinkPix workflow to create children's apparel marketing videos by transferring motion from a reference video to a child model image.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External marketers, storefront operators, and agents use this skill to prepare Qinghu LinkPix workflow runs for children's clothing short videos. It guides cost estimation, submission, status polling, and delivery for authorized reference videos and child model images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs and uses a mutable third-party qhkit CLI.

Mitigation: Review the package before installing, prefer a pinned or isolated qhkit install, and avoid elevated or global installs where possible.

Risk: The qhkit CLI uploads supplied video and image files to Qinghu's service using the user's token.

Mitigation: Use only authorized media, confirm guardian authorization for children's images, and avoid uploading sensitive or unapproved content.

Risk: The workflow is paid and can consume Qinghu credits or require subscription access.

Mitigation: Run an estimate with the exact media before generation, report the quote to the user, and wait for confirmation before submitting the job.

Risk: Online workflow fields and generated-video behavior can change after the documented snapshot.

Mitigation: Run the live options command before preparing parameters and rely on returned field labels rather than stale examples.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-viral-video-kids)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Text]

**Output Format:** [Markdown guidance with inline shell commands and JSON parameter examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide an agent through a qhkit CLI workflow that uploads local media and returns JSON status plus generated media URLs.]

## Skill Version(s):

0.1.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
