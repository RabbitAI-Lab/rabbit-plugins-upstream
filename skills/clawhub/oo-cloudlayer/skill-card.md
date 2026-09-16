## Description:

cloudlayer.io lets agents operate cloudlayer.io through the OOMOL-connected oo CLI for reading account data, inspecting jobs and assets, and creating PDF generation jobs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate PDFs from HTML, templates, or public URLs and to inspect cloudlayer.io account usage, jobs, and generated assets through an authenticated OOMOL connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup can encourage directly executing remote installer scripts.

Mitigation: Use official signed releases when available, or download, inspect, and verify the installer before running it.

Risk: PDF job creation actions can create paid or persistent account-side work.

Mitigation: Confirm the exact payload and expected effect with the user before running any write action.

Risk: Commands operate through an authenticated OOMOL-connected cloudlayer.io account.

Mitigation: Run only the requested action, avoid exposing raw credentials, and fall back to setup steps only after an authentication or connection error.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-cloudlayer)
- [cloudlayer.io homepage](https://cloudlayer.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce oo CLI commands that call the cloudlayer connector; write actions require user confirmation before execution.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
