## Description:

Generates a new-product positioning one-pager from product materials, including a positioning statement, value quadrant, required and differentiating factors, competitive difference, first content translation, and validation checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[handsomeng](https://clawhub.ai/user/handsomeng)

### License/Terms of Use:

MIT-0

## Use Case:

External product, content, and management teams use this skill to turn product briefs and follow-up answers into a concise positioning sheet for new-product planning and first content direction.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may read or update local brand archive files containing sensitive product or brand strategy.

Mitigation: Review before installing in confidential workspaces and tell the agent not to create or update archives when a no-persistence session is required.

Risk: The skill may create a first-run marker in the user's home directory.

Mitigation: Use an isolated environment or instruct the agent to skip persistence if local state is not acceptable.

Risk: The skill can produce positioning guidance that may be misleading if product evidence is incomplete.

Mitigation: Have a knowledgeable human review the positioning statement, differentiators, and validation checks before relying on the output for business decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/handsomeng/skills/ljh-dingwei)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown with structured tables and bullet lists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May optionally create or update local onboarding and brand archive files when the agent follows the artifact behavior.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter reports 0.5.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
