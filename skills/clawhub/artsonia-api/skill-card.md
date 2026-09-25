## Description:

Access Artsonia student-art portfolios, comments, fans, teacher feedback, artwork downloads, and account pages from a shell using curl and documented endpoint recipes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technically proficient Artsonia account holders use this skill to script authorized reads, downloads, and carefully confirmed account actions without running the Artsonia MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access sensitive Artsonia student, portfolio, fan, feedback, profile, and artwork data.

Mitigation: Use it only with authorization for the relevant Artsonia account and students, treat all outputs as sensitive, and delete session files and downloaded data when finished.

Risk: Cookie jars, fetched pages, and downloaded images may expose private account or student information.

Mitigation: Store session cookies and output files in protected locations, avoid sharing them, and remove them after the task is complete.

Risk: The skill includes write actions such as comments, fan invitations, feedback marking, and profile updates.

Mitigation: Require explicit confirmation of the exact action, target, and data before any write, then re-read the affected page to verify the result.

Risk: Private artwork images may be downloadable from unauthenticated CDN URLs, which creates bulk-collection and redistribution risk.

Mitigation: Avoid bulk or private artwork downloads unless the user confirms authorization and a legitimate need.

## Reference(s):

- [Artsonia endpoint recipes](references/endpoints.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/artsonia-api)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands, curl examples, endpoint paths, and parsing recipes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes session setup, endpoint-specific commands, output parsing examples, and verification guidance for write actions.]

## Skill Version(s):

1.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
