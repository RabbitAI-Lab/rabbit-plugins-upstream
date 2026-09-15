## Description:

HTML to Image helps agents capture public webpage screenshots or convert raw HTML and optional CSS into generated image URLs through the OOMOL html_to_image connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to ask an agent to produce webpage screenshots or image outputs from HTML without handling HTML to Image API credentials directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted HTML, CSS, public URLs, and rendered page content may be processed by third-party services.

Mitigation: Use the skill only for content appropriate for OOMOL and HTML to Image processing; avoid secrets, private pages, authenticated URLs, and personal data unless that processing is explicitly intended.

Risk: Installer snippets fetch and execute remote scripts for the oo CLI.

Mitigation: Prefer a verified, versioned installation method and review installation sources before running setup commands.

Risk: Generated screenshots or image URLs may expose sensitive rendered content if private inputs are provided.

Mitigation: Limit inputs to public or approved content and review generated URLs before sharing them.

## Reference(s):

- [HTML to Image homepage](https://html2img.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [HTML to Image skill page](https://clawhub.ai/oomol/skills/oo-html-to-image)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent output may include generated screenshot URLs, generated image URLs, connector schema guidance, setup recovery steps, and execution identifiers returned by the connector.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
