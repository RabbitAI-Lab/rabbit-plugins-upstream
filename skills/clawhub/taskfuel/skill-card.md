## Description:

Provides agents with pay-per-call APIs for media generation, transcription, data research, enrichment, travel, document tasks, and user-authorized communications.

This skill is ready for commercial/non-commercial use.

## Publisher:

[taskfuel.ai](https://clawhub.ai/user/taskfuel.ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users use taskfuel to access paid APIs when installed tools do not cover a requested task. It supports media generation, transcription, data and social research, travel information, document utilities, and user-authorized communications or bookings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Calls use the user's prepaid balance, and the skill encourages using taskfuel when other tools do not cover a task.

Mitigation: Check that a paid API is needed, quote the request, set a per-call cap and task budget, and get approval when the documented spending thresholds apply.

Risk: The installation instructions can run a remote installer.

Mitigation: Review the installer before running it.

Risk: Requests may send sensitive information to third-party providers, and some endpoints can contact people or make bookings.

Mitigation: Send sensitive inputs only to providers the user trusts, and get the user's go-ahead before sending messages, placing calls, mailing items, or booking.

## Reference(s):

- [Taskfuel ClawHub release](https://clawhub.ai/taskfuel.ai/skills/taskfuel)
- [Taskfuel website](https://taskfuel.ai)
- [Taskfuel installer](https://taskfuel.ai/install.sh)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, Guidance, Text]

**Output Format:** [Markdown instructions with inline shell command examples; API results vary by service.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Paid calls can incur per-call charges; quote requests and set a spending cap before calling.]

## Skill Version(s):

0.6.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
