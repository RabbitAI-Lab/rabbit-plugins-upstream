## Description:

Cloudflare Browser Run helps agents render URLs or raw HTML through an OOMOL-connected Cloudflare Browser Run account and return HTML, Markdown, links, selected elements, or structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to access Cloudflare Browser Run through the OOMOL oo CLI, inspect action schemas, render pages or raw HTML, and extract content as HTML, Markdown, links, elements, or JSON.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup can involve installing the oo CLI, signing in, and connecting Cloudflare credentials through OOMOL.

Mitigation: Install and connect only when needed, review setup URLs before use, and avoid repeating login or connection steps unless an auth or connection error requires it.

Risk: Rendering private or sensitive pages can expose page content through the connected Browser Run workflow.

Mitigation: Review target URLs and payloads before rendering sensitive pages, and use only accounts and scopes intended for the task.

## Reference(s):

- [Cloudflare Browser Run documentation](https://developers.cloudflare.com/browser-run/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include rendered HTML, Markdown, extracted JSON, discovered links, selected HTML elements, or account listings returned by the connector.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
