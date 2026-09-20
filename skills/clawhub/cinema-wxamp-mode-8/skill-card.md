## Description:

影院业务 Skill。通过 Cinema Agent 执行授权采集、H5 回放和绑券能力。

This skill is ready for commercial/non-commercial use.

## Publisher:

[rascalagnt001](https://clawhub.ai/user/rascalagnt001)

### License/Terms of Use:

MIT-0

## Use Case:

External OpenClaw users use this skill as a conversation entry point for a local Cinema Agent plugin that performs authorized H5 capture, order replay, coupon binding, and related page operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release ships obfuscated code that handles H5 login and session data and persists it across tasks.

Mitigation: Review before installing and use only if the publisher and local Cinema Agent environment are trusted.

Risk: The skill can perform coupon binding, order replay, webview activity, and cloud-routed channel operations.

Mitigation: Confirm authorization status, required identity values, and intended business workflow before running actions.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, guidance, shell commands, configuration]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires yuanxianCode and weixinMpLink identity values and delegates runtime actions to the local Cinema Agent plugin.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
