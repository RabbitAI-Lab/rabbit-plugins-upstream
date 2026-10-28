## Description:

Orchestrates turning a supplied livestream recording into user-reviewed, editable rough-cut clip projects.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gitruck](https://clawhub.ai/user/gitruck)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and video editors use this skill to turn a supplied livestream recording into editable clip projects, review a consolidated list of candidate highlights, and choose which clips to develop further.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Livestream recordings are processed by the provider's cloud service.

Mitigation: Use recordings you are comfortable sending to the provider.

Risk: Cloud processing can incur charges.

Mitigation: Review current pricing and the recording's audio duration before submission.

Risk: An exposed API key could allow unauthorized access.

Mitigation: Protect the GITRUCK_API_KEY and avoid sharing it in chat or logs.

Risk: Projects may lose access to media if their input segments are removed.

Mitigation: Retain the input segments for as long as the editable projects are needed.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/gitruck/skills/gtrk-live-slicing)
- [Gitruck CLI integration homepage](https://github.com/Gitruck/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown guidance with clip-selection tables and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides creation of editable rough-cut clip projects through gtrk; the agent provides the selection list and workflow guidance.]

## Skill Version(s):

1.3.9 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
