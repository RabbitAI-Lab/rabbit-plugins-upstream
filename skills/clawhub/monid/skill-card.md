## Description:

Monid helps agents discover, inspect, and run third-party tools and APIs for web scraping, data retrieval, enrichment, search, media generation, and related tasks through the Monid CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[monid](https://clawhub.ai/user/monid)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to decide when Monid is appropriate, discover endpoints, inspect input schemas, run and poll jobs, manage API keys, and handle cost-aware workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Monid can initiate paid third-party data runs that spend the user's Monid balance.

Mitigation: Confirm before paid runs, start with small result limits, inspect endpoint pricing and cost outputs, and check balance when budget matters.

Risk: Monid requires API keys that could be exposed if pasted into chat or stored carelessly.

Mitigation: Prefer user-entered secrets, treat API keys as confidential, verify configured keys with `monid keys list`, and remove unused keys.

Risk: The setup flow can update the CLI and replace the installed skill from a remote source.

Mitigation: Review the updated skill and installed CLI version before enabling or using the release.

Risk: Remote file workflows can upload local files and create signed URLs accessible to external services.

Mitigation: Require explicit approval before uploads or signed URL generation, limit TTLs, and remove remote files after use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/monid/skills/monid)
- [Monid skill source](https://monid.ai/SKILL.md)
- [Monid app](https://app.monid.ai)
- [Monid API keys](https://app.monid.ai/access/api-keys)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include endpoint schemas, run IDs, saved result file paths, costs, and balance guidance when relevant.]

## Skill Version(s):

0.1.7 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
