## Description:

This skill uses OOMOL's HTML to Image connector and oo CLI to capture public webpage screenshots or convert raw HTML and optional CSS into hosted image URLs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to produce webpage screenshots or image renderings from public URLs or supplied HTML/CSS through a connected HTML to Image account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that run downloaded scripts.

Mitigation: Install the oo CLI only after independently verifying the installer source and integrity, and avoid curl-to-bash or irm-to-iex flows unless the source is trusted.

Risk: HTML, public URLs, and rendered outputs are sent to a connected external service and may create hosted image outputs.

Mitigation: Do not submit private HTML, internal URLs, credentials, or sensitive page content unless the user accepts that external processing and hosted output behavior.

Risk: The skill depends on OOMOL authentication, an active HTML to Image connection, service scopes, and available billing credit.

Mitigation: Use first-time setup and recovery steps only after a related command failure, and verify action schemas before execution.

## Reference(s):

- [HTML to Image homepage](https://html2img.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-html-to-image)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns generated screenshot or image URLs through the connected external service.]

## Skill Version(s):

1.0.3 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
