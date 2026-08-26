## Description:

Unload your cognitive baggage. Drop ideas anywhere, find the signal later.

This skill is ready for commercial/non-commercial use.

## Publisher:

[highnoonoffice](https://clawhub.ai/user/highnoonoffice)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and OpenClaw users use this skill to turn a personal idea ledger into structured atoms, LLM-generated clusters, and a React/D3 visualization of patterns, tensions, emerging signals, and absences.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles private notes and message history.

Mitigation: Use a dedicated second-brain inbox or ledger and avoid importing work or third-party messages without consent.

Risk: The atom corpus may be sent through a configured LLM route.

Mitigation: Keep the OpenClaw gateway host on localhost unless you intentionally trust the remote endpoint, and review the configured LLM provider's logging and retention behavior.

Risk: Automated ingestion can collect more source material than intended.

Mitigation: Disable scheduled ingestion until source limits and a deletion process are clear.

Risk: Security evidence marks the release as requiring review before installation.

Mitigation: Review the skill before installing and scan it before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/highnoonoffice/skills/second-brain-visualizer)
- [Project homepage](https://github.com/highnoonoffice/hno-skills)
- [Setup Guide](references/setup.md)
- [Install Guide](references/install.md)
- [Ingestion Guide](references/ingestion.md)
- [Parser Script](references/parser.js)
- [Clustering Script](references/cluster.js)
- [Visualizer Component](references/component.tsx)
- [Sample Atom Ledger](references/sample-ledger.md)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JavaScript and TypeScript code, shell command snippets, and JSON output schemas.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local atom and cluster JSON artifacts for use by a dashboard component; LLM routing depends on the user's OpenClaw gateway configuration.]

## Skill Version(s):

1.6.3 (source: server release metadata; artifact frontmatter reports 1.6.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
