## Description:

Publishes HTML and Markdown pages and shares PDF, Word, and PowerPoint documents through ShareOne links, with options for access controls, comments, and updates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beep879](https://clawhub.ai/user/beep879)

### License/Terms of Use:

MIT

## Use Case:

Developers and other agent users can publish pages and documents as shareable links, manage access settings, and handle feedback on supported pages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated requests may be redirected to untrusted destinations.

Mitigation: Use links from known ShareOne domains and avoid settings or collaborator actions on arbitrary URLs.

Risk: An API key can grant owner-level access to published content and settings.

Mitigation: Install only if you trust the publisher; prefer limited or revocable ShareOne API keys.

Risk: Destructive delete actions lack enforced confirmation.

Mitigation: Manually confirm each delete request before allowing the agent to proceed.

## Reference(s):

- [ShareOne website](https://shareone.vip)
- [ShareOne ClawHub release](https://clawhub.ai/beep879/skills/shareone)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Text or Markdown with share links and operation results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include a public share URL, access settings, and status or error details.]

## Skill Version(s):

1.3.6 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
