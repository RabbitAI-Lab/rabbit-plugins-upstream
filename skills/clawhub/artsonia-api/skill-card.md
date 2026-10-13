## Description:

Guides agents in accessing Artsonia student portfolios, comments, fans, feedback, and artwork through authenticated curl requests without running the Artsonia MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and authorized Artsonia account holders use this skill to retrieve student artwork and account information or manage comments, fan invitations, feedback, and notification settings with curl.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private student artwork may be accessible through direct image links and bulk downloads.

Mitigation: Access only accounts and artwork you are authorized to use; avoid bulk or private downloads without explicit permission.

Risk: Form submissions can change live account state or send invitation emails.

Mitigation: Review each POST before sending it, use only authorized recipients, and verify changes against the affected page.

Risk: Login credentials, session cookies, and downloaded pages can expose account or student information.

Mitigation: Use a trusted machine, protect the cookie jar and temporary files, and clear them when finished.

## Reference(s):

- [Artsonia endpoint recipes](references/endpoints.md)
- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/artsonia-api)
- [Artsonia](https://www.artsonia.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with curl and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Authenticated reads and live form submissions; artwork download commands can create image files.]

## Skill Version(s):

1.3.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
