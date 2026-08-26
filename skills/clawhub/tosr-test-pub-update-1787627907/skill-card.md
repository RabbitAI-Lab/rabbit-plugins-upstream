## Description:

Automated test skill that verifies the full skill lifecycle, including publish, inspect, update, and delete operations through the ClawHub REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yinwuzhe](https://clawhub.ai/user/yinwuzhe)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and release maintainers use this skill as a ClawHub lifecycle test artifact for verifying publish, inspection, update, and delete behavior. It is intended for controlled test contexts because the described workflow changes real remote skill state.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The intended lifecycle workflow can make real remote state-changing API calls, including deletion.

Mitigation: Run only in a dedicated test context with disposable credentials and confirm the target slug before any delete operation.

Risk: A failed test run may leave an ephemeral skill visible on ClawHub.

Mitigation: Inspect the resolved skill page and remove the test skill after validation if cleanup did not complete.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/yinwuzhe/skills/tosr-test-pub-update-1787627907)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands]

**Output Format:** [Markdown guidance describing API lifecycle operations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No executable payload is included in the artifact.]

## Skill Version(s):

0.2.0 (source: server release metadata and artifact SKILL.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
