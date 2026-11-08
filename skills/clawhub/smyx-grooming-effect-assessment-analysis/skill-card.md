## Description:

Assesses post-grooming pet images or videos for remaining mats, dandruff coverage, and coat smoothness, then returns a grooming score and targeted re-grooming suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and grooming professionals use the skill to review post-grooming pet images or videos, assess mats, dandruff, and coat smoothness, and receive a score with re-grooming suggestions. The results are visual grooming assessments, not medical advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected images or videos are sent off-device for remote analysis, and backend retention and deletion practices are not established by the supplied artifacts.

Mitigation: Wait for the identified fixes before installing. If testing, use an isolated workspace and non-sensitive media.

Risk: The skill automatically registers a remote account and stores credentials persistently, with safeguards needing improvement.

Mitigation: Wait for fixes to credential destination checks and token storage before installing.

Risk: The skip-analysis option still processes media, and remote use may incur charges.

Mitigation: Wait for a fix to the skip-analysis behavior and account for possible usage charges before testing.

## Reference(s):

- [API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, Text, JSON]

**Output Format:** [Structured grooming assessment report with score, observations, suggestions, and report link; JSON detail is available.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Visual assessment only; does not provide medical diagnosis or treatment advice.]

## Skill Version(s):

1.0.15 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
