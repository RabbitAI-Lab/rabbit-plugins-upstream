## Description:

Analyzes aquarium pet videos or video URLs through a vendor service and returns health observations, potential disease warnings, and care suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Aquarium owners and caretakers use the skill to review videos of fish and other aquatic pets for possible health concerns and to retrieve prior reports. Its findings are informational and do not replace a veterinarian's diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Aquarium videos or video URLs are sent to a vendor service for analysis.

Mitigation: Share media only with the owner's consent and review the vendor's data handling before use.

Risk: The skill may create or reuse a service identity and store authentication tokens in the workspace.

Mitigation: Use a trusted workspace, restrict access to stored credentials, and review account creation before running the skill.

Risk: Broad history triggers may query cloud report history unexpectedly.

Mitigation: Confirm the user's intent before requesting historical reports.

Risk: The aquarium analysis command contains an autism-analysis scenario mismatch.

Mitigation: Confirm the requested analysis type and review the result before relying on the report.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/smyx-sunjinhui/skills/smyx-aquarium-analysis)
- [Aquarium analysis API reference](references/api_doc.md)
- [Skill introduction](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Text or JSON health reports and Markdown links to historical reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include health observations, warnings, care suggestions, and report links.]

## Skill Version(s):

1.0.14 (source: ClawHub release metadata; bundled SKILL.md states 1.0.17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
