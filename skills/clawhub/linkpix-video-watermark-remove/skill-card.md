## Description:

Removes visible watermarks, logos, and corner marks from videos through the LinkPix qhkit video-edit workflow while preserving clear video quality.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and creators use this skill to submit up to 10 videos for watermark or logo removal, poll for completion, and receive processed video URLs. It is intended for authorized media cleanup and secondary creation workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic global npm installation and latest-version upgrade paths for qhkit can create supply-chain and persistence risk.

Mitigation: Install qhkit only from trusted sources, prefer a contained or local install over a global install, and review or pin package versions before upgrading.

Risk: The workflow uploads selected videos to the qhkit service and requires an API token.

Mitigation: Process only media the user owns or is authorized to modify, keep tokens out of shared logs and prompts, and rotate credentials if exposure is suspected.

Risk: Removing watermarks from third-party copyrighted content can create infringement risk, especially for commercial reuse.

Mitigation: Use the skill only for authorized content and remind users to confirm rights before distributing or monetizing edited videos.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-video-watermark-remove)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [qhkit API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON CLI arguments]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include task IDs, polling status, processed video URLs, credit usage, and user-facing CLI error messages.]

## Skill Version(s):

0.1.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
