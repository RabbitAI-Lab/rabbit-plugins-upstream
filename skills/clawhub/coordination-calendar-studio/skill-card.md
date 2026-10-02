## Description:

Normalizes a supplied calendar event into an event digest and creates a local coordination calendar entry.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

People coordinating meetings can turn a supplied calendar event into a normalized event digest, then generate an ICS entry for local use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Supplied calendar event contents may be sensitive.

Mitigation: Provide only event details you are comfortable sharing with the skill.

Risk: The downstream operation writes a generated ICS file locally.

Mitigation: Choose an appropriate output directory and review the file before sharing it.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/wxt-ai/skills/coordination-calendar-studio)
- [ClawHub publisher profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [JSON, Calendar files]

**Output Format:** [JSON event digest or calendar artifact with ICS content; optional local ICS file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Upstream returns an event digest; downstream writes an ICS file to a caller-selected directory. No calendar-account sync.]

## Skill Version(s):

3.0.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
