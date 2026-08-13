## Description:

Detects whether anyone has fallen within a specified target area, using image or short video analysis for home-care and nursing-home safety monitoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users such as caregivers, family members, and safety-monitoring operators use this skill to screen images or short clips for possible falls and related elderly-care safety risks. Results are safety references and should be confirmed by a person before emergency or care decisions are made.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fall-detection images, short videos, supplied URLs, user-linked identifiers, and report history are sent to the lifeemergence.com cloud service.

Mitigation: Use only when users and operators accept that cloud processing path, and review retention, account-linking, and deletion expectations before using sensitive home-care or nursing-home footage.

Risk: The skill silently creates or reuses a user identity and stores reusable authentication tokens in the workspace data directory.

Mitigation: Run it in a controlled workspace, limit access to local data directories, and rotate or remove stored tokens when the workspace is shared, retired, or no longer trusted.

Risk: Fall analysis is a safety reference and may be incorrect or incomplete.

Mitigation: Require human confirmation and established emergency procedures for suspected falls or other safety-critical outcomes.

## Reference(s):

- [Fall Detection API Documentation](references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-fall-detection-image-analysis)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown and JSON-style structured reports with optional shell command examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return fall-detection analysis, risk notes, recommendations, report links, saved output files, or history tables.]

## Skill Version(s):

1.0.11 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
