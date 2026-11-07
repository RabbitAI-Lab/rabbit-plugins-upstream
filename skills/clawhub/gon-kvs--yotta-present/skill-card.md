## Description:

元呈 yotta-present is a local presentation layer that helps agents choose an output form and render AI results as copyable Markdown, plain text, JSON, or optional local SVG charts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gon-kvs](https://clawhub.ai/user/gon-kvs)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users use this skill to standardize final AI responses into readable, reusable presentation formats such as conclusion cards, tables, checklists, reports, and charts. It is useful when an agent needs local, offline rendering with platform-specific Markdown or plain-text output.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can become a persistent default output layer for future agent responses.

Mitigation: Use the CLI for one-off rendering, and approve mcpServers or permanent-memory writes only when cross-session behavior is intended.

Risk: SVG or output file paths can overwrite user-writable files.

Mitigation: Keep output paths user-selected or preapproved, and do not let untrusted prompts choose write locations.

Risk: Unpinned npx installation can introduce supply-chain uncertainty in sensitive environments.

Mitigation: Use reviewed local installs or pinned package versions for controlled deployments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gon-kvs/skills/yotta-present)
- [Standard content object schema](references/schema.md)
- [FAQ and troubleshooting](references/faq.md)
- [Presentation templates](references/templates.json)

## Skill Output:

**Output Type(s):** [text, markdown, json, code, shell commands, configuration, guidance]

**Output Format:** [Copyable Markdown or plain text, optional JSON response, and optional local SVG output for chart forms.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Platform-adaptive rendering with channel selection, optional length limits, and local offline processing.]

## Skill Version(s):

0.3.0 (source: frontmatter, package.json, changelog, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
