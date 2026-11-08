## Description:

Run website agent readiness audits (AEO, llms.txt, structured data, AI crawler access), preview branch audits, changed-page sitemap audits, local/private preview audits with explicit opt-in, sitemap origin rewriting, static-output audits, regression comparisons, site fixes, schema validation, and llms.txt generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arberx](https://clawhub.ai/user/arberx)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to assess website readiness for AI agents and search, validate structured data, compare audit results, and generate or improve AI-readable site files. It can also guide targeted site fixes after an audit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan flagged that the fix workflow may exceed its declared write scope; scan coverage was incomplete, so unreported behavior is not established as safe.

Mitigation: Review the skill’s write permissions and fix workflow before installing, and check whether the MCP server version can be pinned.

## Reference(s):

- [Agent Readiness on ClawHub](https://clawhub.ai/arberx/skills/agent-readiness)
- [Canonry](https://canonry.ai)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Shell commands, Files, Guidance]

**Output Format:** [JSON or Markdown audit reports, shell commands, and website text files such as llms.txt, llms-full.txt, and robots.txt]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Audit detail varies by selected mode and flags.]

## Skill Version(s):

8.0.1 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
