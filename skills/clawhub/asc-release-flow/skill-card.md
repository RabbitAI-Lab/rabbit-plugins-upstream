## Description: <br>
End-to-end release workflows for TestFlight and App Store using asc publish, builds, versions, and submit commands. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rudrankriyam](https://clawhub.ai/user/rudrankriyam) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers releasing iOS apps use this skill to select asc CLI commands for uploading builds, distributing through TestFlight, and submitting App Store versions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Release credentials could grant broader App Store Connect access than the task requires. <br>
Mitigation: Scope ASC_* credentials to the specific apps and release permissions needed before installing or using the skill. <br>
Risk: Suggested upload, distribution, or submission commands can affect real TestFlight and App Store releases. <br>
Mitigation: Review commands and target app, build, group, and version values before upload or submission. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/rudrankriyam/skills/asc-release-flow) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Provides command sequences and optional flags for TestFlight and App Store release flows.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
