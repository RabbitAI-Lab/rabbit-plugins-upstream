## Description:

Helps agents research viral social content, prepare branded drafts, review posts, and schedule or publish to a user's connected social accounts through ViralHunt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rodvan](https://clawhub.ai/user/rodvan)

### License/Terms of Use:

MIT-0

## Use Case:

External users and their content teams use the skill to find trending topics, create and review branded posts, and schedule or publish them to connected social accounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automated review or approval can release posts to real social accounts without a person checking them.

Mitigation: Keep reviewer and publisher tokens separate; enable auto-approval or recurring review only for accounts where automated public posting is acceptable.

Risk: Draft-editing authority may be broader than expected for an agent with account access.

Mitigation: Use reader or writer tokens for routine work, avoid full-permission tokens unless necessary, and confirm target accounts and post changes before granting publishing authority.

## Reference(s):

- [ViralHunt API documentation](https://viralhunt.io/api)
- [ViralHunt ClawHub release](https://clawhub.ai/rodvan/skills/viralhunt)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Plain text or Markdown, including social post drafts and recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [With authorized access, can save drafts and schedule or publish posts to connected accounts.]

## Skill Version(s):

1.6.15 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
