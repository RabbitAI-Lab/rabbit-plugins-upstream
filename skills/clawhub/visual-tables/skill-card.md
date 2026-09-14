## Description:

Render comparison tables a human reads at a glance instead of parsing: color and bar length carry the comparison, and text confirms it.

This skill is ready for commercial/non-commercial use.

## Publisher:

[globalcaos](https://clawhub.ai/user/globalcaos)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill to present multi-attribute comparisons such as search results, product options, benchmarks, server health, candidates, or quotes as scannable HTML-rendered tables in chat.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Rendered table fields can include raw HTML when values come from webpages, search results, user submissions, or other untrusted sources.

Mitigation: Pass only trusted or sanitized HTML into the renderer, and escape user-controlled table content before rendering.

Risk: The documented browser preview command uses a no-sandbox Chrome flag.

Mitigation: Avoid the no-sandbox flag where possible, or run preview rendering in a sandboxed browser or isolated container.

## Reference(s):

- [Designing a table someone can read at a glance](references/designing-a-table.md)
- [Visual Tables on ClawHub](https://clawhub.ai/globalcaos/skills/visual-tables)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, guidance]

**Output Format:** [Markdown with html-render fenced HTML, JavaScript snippets, and occasional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js for the bundled renderer example; no network or credentials are required by the skill evidence.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
