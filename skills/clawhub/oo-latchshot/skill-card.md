## Description:

Latchshot lets an agent operate the Latchshot connector through the OOMOL oo CLI to render public web pages as PNG, JPEG, or PDF artifacts and read usage information.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to capture public web pages through Latchshot and retrieve account usage details through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Page capture sends target URLs to Latchshot/OOMOL and uploads rendered artifacts to transit storage.

Mitigation: Use capture_page only for public URLs and content that is appropriate to send to the external rendering service.

Risk: The artifact includes remote installer commands such as curl|bash and irm|iex.

Mitigation: Do not run installer commands automatically; use a verified package source or manually inspect the installer before execution.

Risk: The security summary notes that capture_page is under-disclosed as read-like despite producing uploaded artifacts.

Mitigation: Review the target URL, output format, and storage implications before invoking capture_page.

## Reference(s):

- [Latchshot homepage](https://latchshot.fly.dev)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-latchshot)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return Latchshot JSON responses and links to rendered PNG, JPEG, or PDF artifacts.]

## Skill Version(s):

1.0.2 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
