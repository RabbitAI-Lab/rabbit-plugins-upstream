## Description:

Guides agents in accessing Artsonia student artwork, comments, fans, feedback, and downloads through authenticated shell requests without running an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Parents or authorized account holders and developers use the skill to inspect student artwork and related account information or perform requested account actions through shell commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Accessing or redistributing private student artwork and account details without authorization.

Mitigation: Use only accounts and student content you are authorized to access; avoid bulk downloads and redistribution of private material.

Risk: Write commands can post comments, send real invitation emails, mark all feedback read, or alter profile notification settings.

Mitigation: Require explicit approval for each intended change and recheck the affected page afterward; a redirect alone does not confirm success.

Risk: A stored session cookie can expose account access to other local users.

Mitigation: Keep the cookie jar under restrictive file permissions and delete it after use on shared systems.

## Reference(s):

- [Artsonia endpoint recipes](references/endpoints.md)
- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/artsonia-api)
- [Artsonia](https://www.artsonia.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide authorized reads, artwork downloads, and explicit account changes.]

## Skill Version(s):

1.2.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
