## Description:

Partner Training turns approved partner program materials into a grounded interactive digital-human course for channel partner onboarding.

This skill is ready for commercial/non-commercial use.

## Publisher:

[personwiseai](https://clawhub.ai/user/personwiseai)

### License/Terms of Use:

MIT-0

## Use Case:

Partner program and enablement teams use this skill to create interactive courses for channel partners and resellers from approved source materials. The resulting course teaches the product story, deal flow, program rules, self-checks, and escalation paths while keeping claims grounded in supplied materials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may install or update the PersonWise CLI in the user's local environment.

Mitigation: Require explicit approval before installation or update and use only the bundled market-bound bootstrap path.

Risk: The workflow opens browser OAuth and uses a PersonWise account to create courses.

Mitigation: Use browser OAuth only, never request secrets, and pin operations to the authenticated account alias returned by the CLI.

Risk: Selected source materials may be uploaded to PersonWise to ground the course.

Mitigation: Upload only files named, attached, or explicitly selected by the user; disclose and request approval before uploading agent-discovered local files.

Risk: Creating courses can consume existing PersonWise course credits and broader access settings can make courses shareable.

Mitigation: Treat a course-creation request as authorization only for the requested course count, never buy credits automatically, and default new courses to private unless the user requests link access or publication.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/personwiseai/skills/personwise-partner-training)
- [Publisher Profile](https://clawhub.ai/user/personwiseai)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces instructions for creating a PersonWise digital-human course from user-approved materials; course artifacts are created through the PersonWise CLI and service.]

## Skill Version(s):

2.1.9 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
