## Description:

Helps sellers use Qinghu AI and qhkit to analyze reference short-form videos, rewrite scripts around their products, and generate Vidu Q3-style commercial videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers and marketing teams use this skill to adapt viral short-form video structures into product-focused Vidu Q3 video generation workflows. It guides agents through reference-video analysis, script rewriting, user confirmation, paid credit estimation, task submission, polling, and delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks the agent to install or upgrade unpinned npm tooling.

Mitigation: Approve exact qhkit/npm commands and versions before installation or upgrade; prefer pinned versions in controlled environments.

Risk: The workflow may collect a Qinghu API token and submit paid video-generation jobs.

Mitigation: Configure the token through a secure local secret or environment variable and require explicit approval of model, duration, inputs, and estimated credits before generation.

Risk: Media assets and prompts are uploaded to Qinghu for processing.

Mitigation: Use only media the user is permitted to upload and avoid confidential or rights-restricted source material.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-vidu-q3-clone)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON command payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides paid Qinghu video-generation jobs and returns task status, generated video links, and credit information when available.]

## Skill Version(s):

0.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
