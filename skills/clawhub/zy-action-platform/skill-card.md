## Description:

Connect and operate ZY Action Platform (AI Business Action System): guide verified install & DeepSeek key config, then health-check/login and, across the five products AIP/Foundry/Gotham/Apollo/Swift, run natural-language data queries, list/run automation workflows, query datasets/ontology, search intel, inspect deployments and more.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youkpan](https://clawhub.ai/user/youkpan)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and platform operators use this skill to connect to ZY Action Platform, authenticate with consent, and run data queries, workflow operations, dataset and ontology lookups, intel searches, deployment inspections, and health checks across the platform products.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated platform access can expose business data or permit operations when high-privilege credentials are used.

Mitigation: Use a dedicated read-only account for routine query and list operations, avoid admin credentials, and log out when finished.

Risk: Credentials or bearer tokens may be exposed if users put secrets into prompts or command-line arguments.

Mitigation: Preview login destinations with dry-run, avoid placing passwords or bearer tokens in prompts, and clear cached sessions after use.

Risk: Generic pass-through requests have material review concerns until path canonicalization and secret-entry issues are fixed.

Mitigation: Prefer built-in commands, avoid generic pass-through where possible, and require dry-run review plus explicit confirmation for any approved write.

## Reference(s):

- [ZY Action Platform API Quick Reference](references/api-spec.md)
- [Session Transcripts](references/examples.md)
- [ZY Action Platform download page](https://zyinfo.pro/action/)
- [ClawHub skill page](https://clawhub.ai/youkpan/skills/zy-action-platform)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries with inline shell commands and JSON-derived results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill instructs the agent to run a local Python helper, read JSON output, and summarize results without fabricating platform responses.]

## Skill Version(s):

1.1.1 (source: server release metadata; artifact frontmatter reports 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
