## Description:

Guides a four-step PikPak workflow to submit a magnet link for cloud download, check completion, download the file locally, and propose manual cloud cleanup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pipiguai87-alt](https://clawhub.ai/user/pipiguai87-alt)

### License/Terms of Use:

MIT-0

## Use Case:

People with a PikPak account use this skill to move user-authorized magnet downloads to local storage and review a proposed cloud cleanup command after confirming the local file.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitting an unintended or unauthorized link can create an unwanted cloud download and consume account quota.

Mitigation: Confirm authorization, the link, and available account quota before submission.

Risk: Downloading to the wrong location or removing the cloud copy before checking the local file can cause lost or misplaced content.

Mitigation: Confirm the destination and inspect the downloaded file before reviewing and manually executing any cleanup command.

## Reference(s):

- [PikPak Magnet Pipeline on ClawHub](https://clawhub.ai/pipiguai87-alt/skills/pikpak-magnet-pipeline)
- [PikPak CLI installation](https://mypikpak.com/cli)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [JSON task and download status, with plain-text cleanup commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Steps can be run separately; cleanup commands require manual execution.]

## Skill Version(s):

1.0.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
