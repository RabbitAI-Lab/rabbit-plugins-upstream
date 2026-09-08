## Description:

Collect Instagram profile data by username or profile URL; do not use it for post comments or Reel content.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit Dataify Instagram profile collection jobs for usernames or profile URLs, monitor completion, and retrieve final JSON results when they have a legitimate privacy-compliant reason.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can trigger external Instagram profile collection jobs using a saved Dataify API TOKEN.

Mitigation: Configure DATAIFY_API_TOKEN outside chat, review each target and expected credit cost before running, and avoid exposing the token.

Risk: Collected Instagram profile data may create privacy or policy risk if used without a legitimate basis.

Mitigation: Use the collected results only where there is a legitimate privacy-compliant reason to collect the profile data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-instagram-profiles)
- [Modes and parameters](references/modes-and-parameters.md)
- [Dataify dashboard login](https://dashboard.dataify.com/login?utm_source=skill)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Code, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON task or result output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May submit external Dataify jobs and summarize large JSON results while preserving access to raw results.]

## Skill Version(s):

1.3.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
