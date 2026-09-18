## Description:

Breaks down the titles, bullets, images, and review evidence from user-provided or authorized competitor product pages, organizing reusable page structure and risks without claiming real sales, inventory, advertising, order, or return-rate conclusions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External users and operators use this skill to analyze the structure and supporting evidence of provided or authorized Amazon product and competitor pages. It is intended for static product-page teardown and comparison, not for proving bestseller status or making claims about live sales, inventory, ads, orders, profit, or return rates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores an ARI API key locally and contacts ari.funewa.com.

Mitigation: Review installation and authorization before use, protect the local API key, and use the documented setup, configure, check, and version commands only as needed.

Risk: The skill can spend ARI credits after confirmation.

Mitigation: Require a quote and explicit user confirmation before running paid collection or analysis, and reuse the quoted requestId rather than rerunning interrupted work.

Risk: The bundled CLI can be manually invoked with workflow or focus values outside the advertised fixed teardown workflow.

Mitigation: Use the documented fixed page_compare/teardown workflow and review command invocations against skill-defaults.json before execution.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/funewa/skills/bestseller-teardown)
- [Amazon best seller teardown operation workflow](artifact/references/operation-workflow.md)
- [Amazon best seller teardown API reference](artifact/references/reference.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with concise prose and inline shell commands when advanced CLI usage is needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key. Paid collection or analysis must be quoted first and run only after explicit user confirmation; outputs are limited to the provided or authorized page evidence and collected samples.]

## Skill Version(s):

1.4.13 (source: server release evidence, _meta.json, CHANGELOG, and CLI VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
