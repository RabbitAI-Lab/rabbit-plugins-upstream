## Description:

Analyzes pet videos or images for behaviors such as scratching, chewing, and separation anxiety, returning reports and guidance for pet owners.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and caregivers use the skill to review pet behavior from videos or images, receive a structured report, and retrieve previous cloud reports. Results are informational and do not replace professional advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet photos, videos, or video URLs are sent to external lifeemergence.com services for analysis.

Mitigation: Share only content you are comfortable sending to that service; review its data handling before use.

Risk: The skill can silently create or reuse an account identity and store authentication tokens locally.

Mitigation: Review the identity and local token-storage behavior before installing or running the skill.

Risk: Cloud report history may be retrieved under the reused identity.

Mitigation: Use a suitable identity and review access to its report history before requesting past reports.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-pet-behavior-detection-analysis)
- [Skill API documentation](references/api_doc.md)
- [Pet behavior skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Structured analysis report or Markdown history table; JSON output is available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes behavior findings, recommendations, and report links; can save output to a file]

## Skill Version(s):

1.0.14 (source: ClawHub release; bundled SKILL.md lists 1.0.19)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
