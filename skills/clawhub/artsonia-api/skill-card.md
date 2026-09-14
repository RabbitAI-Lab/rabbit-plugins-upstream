## Description:

Provides curl-based recipes for authorized Artsonia parent accounts to sign in, read student art portfolio data, download artwork images, and perform selected account actions without running the Artsonia MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, and authorized Artsonia account holders use this skill to script curl access to Artsonia member pages for student portfolios, comments, fans, feedback, profile data, image downloads, and carefully verified account updates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can expose sensitive Artsonia student and family data, including private artwork images.

Mitigation: Install and use it only for Artsonia accounts and student data you are authorized to access, and treat response files, downloaded images, and command output as sensitive.

Risk: Cookie jars and temporary HTML files may retain authenticated session data or personal information on disk.

Mitigation: Store cookies and response files in owner-only locations, avoid shared directories, and delete temporary files when the task is complete.

Risk: Write actions and fan invites can make live account changes or send real invitation emails.

Mitigation: Require deliberate confirmation before running write commands, use only authorized recipient addresses, and re-read the affected page to verify the actual result.

Risk: The parser workflow depends on an external local repository and npm build steps.

Mitigation: Review or pin the parser repository before running npm commands, especially in commercial or shared environments.

## Reference(s):

- [Endpoint recipes](references/endpoints.md)
- [Artsonia](https://www.artsonia.com)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/artsonia-api)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command and JavaScript snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires authorized Artsonia credentials; commands may create local cookie jars and temporary HTML or image files.]

## Skill Version(s):

0.12.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
