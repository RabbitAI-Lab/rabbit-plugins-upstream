## Description:

Helps developers trace local CodeQL alerts to their source, test one-change variants, and verify whether a fix clears the alert.

This skill is ready for commercial/non-commercial use.

## Publisher:

[elisabeth15501](https://clawhub.ai/user/elisabeth15501)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security engineers use this skill to inspect SARIF data flows, investigate the cause of a single CodeQL alert, and check a proposed fix locally before pushing changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local analysis reads and copies the selected source tree and writes temporary artifacts, which may expose sensitive repository content.

Mitigation: Select a narrow --tree and an explicit --workdir for sensitive repositories; review and clean up temporary artifacts.

Risk: Optional CodeQL runs may execute a local binary and download query components from GitHub.

Mitigation: Verify the CodeQL binary and source in controlled environments, or use the local pre-screen and SARIF reader without CodeQL.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/elisabeth15501/skills/codeql-local-triage)
- [Running CodeQL CLI](artifact/references/running-codeql-cli.md)
- [Sensitive-data heuristics](artifact/references/sensitive-data-heuristics.md)
- [CodeQL standard libraries](https://github.com/github/codeql)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Shell commands]

**Output Format:** [Markdown with shell commands and optional JSON diagnostics]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [SARIF source-to-sink paths, variant comparison, and fix-verification guidance]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
