## Description:

Reviews an existing YouTube thumbnail, social media cover, article cover, or podcast cover, identifies visual hook, hierarchy, title fit, readability, and crop resilience, then produces practical improvement directions and optional visual candidates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and publishing teams use this skill to review existing cover or thumbnail designs before publication, optionally compare the design against public same-topic results, and prepare confirmed Beatra image-generation requests for candidate improvements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can upload selected cover files and contextual publication details to Beatra.

Mitigation: Review the selected file and prompt context before use, and avoid submitting confidential or sensitive material unless that use is approved.

Risk: The skill can spend Beatra credits after confirmations for baseline lookups and image-generation work.

Mitigation: Require the documented per-call confirmation, keep the frozen request details, and record returned task IDs, terminal status, and net charged credits.

Risk: The skill stores a shared Beatra token locally.

Mitigation: Review the authorization scope before installing, protect the local credential file, and use the documented disconnect or uninstall path when access is no longer needed.

Risk: The bundled client silently checks for and installs package updates by default.

Mitigation: Use the documented auto-update controls when change control is required, and rely on the package's fixed Beatra discovery and CDN verification before replacement.

## Reference(s):

- [ClawHub listing](https://clawhub.ai/beatra-ai/skills/cover-performance-preflight)
- [Beatra skill page](https://beatra.ai/skills/cover-performance-preflight)
- [Cover preflight workflow](references/workflow.md)
- [Reading the same-topic baseline](references/baseline-lookup.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Tasks and results](references/tasks-and-results.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with command snippets and task or artifact identifiers when remote work is confirmed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include qualitative preflight findings, paid-call confirmation details, Beatra task IDs, artifact links, observed dimensions, resolved model, and net charged credits.]

## Skill Version(s):

0.1.3 (source: server release evidence and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
