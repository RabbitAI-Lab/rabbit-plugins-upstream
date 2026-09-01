## Description:

Helps agents generate YouTube-oriented product marketing videos through Qinghu/LinkPix qhkit, including model selection, media upload, task submission, status polling, and result delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, brand marketing teams, ad creative teams, and agents use this skill to prepare YouTube product videos, ads, brand channel content, and affiliate or independent-site marketing videos with LinkPix/qhkit workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may upload user-selected product media to Qinghu/LinkPix services.

Mitigation: Confirm that the user intends to use qhkit and understands which media will be uploaded before submission.

Risk: Video generation can consume paid credits once a task is submitted.

Mitigation: Run the available estimate step, disclose expected credit use, and wait for explicit user approval before any paid generation request.

Risk: The skill depends on installing and configuring the third-party qhkit CLI and API credentials.

Mitigation: Install qhkit only when needed, use the official package source or documented fallback, and request an API key only through the Qinghu account workflow.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/autoagc/skills/linkpix-youtube-viral-video)
- [qhkit npm Package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API Key Dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Qinghu API Key Guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API calls]

**Output Format:** [Markdown with inline shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include qhkit command parameters, estimated credit use, task IDs, status results, and generated video URLs.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
