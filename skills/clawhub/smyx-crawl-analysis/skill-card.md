## Description:

Analyzes reptile pet videos from local files or URLs to provide health observations, potential disease warnings, and a report link.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and caretakers use the skill to review reptile videos for health concerns, receive care guidance, and retrieve prior reports. Its observations do not replace a veterinarian's diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploaded pet media and report history are linked to an automatically managed cloud identity, with account tokens stored locally.

Mitigation: Install only if this data handling is acceptable; review or disable the local token and user database behavior in privacy-sensitive workspaces.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/smyx-sunjinhui/skills/smyx-crawl-analysis)
- [Health analysis API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [JSON or Markdown health report with a report link]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Basic, standard, or JSON detail; optionally saved to a file.]

## Skill Version(s):

1.0.16 (source: ClawHub release metadata; bundled SKILL.md lists 1.0.20)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
