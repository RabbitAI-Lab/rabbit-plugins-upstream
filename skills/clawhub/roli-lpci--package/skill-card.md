## Description:

Audits user-named agent instruction files with the LintLang static linter and reports severity-ranked findings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[roli-lpci](https://clawhub.ai/user/roli-lpci)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to audit specific agent prompts, tool definitions, and configuration files for unclear instructions and structural issues. It reports findings without editing the files or assessing runtime safety.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scanning an unintended or sensitive instruction file may expose its contents to the local linter and the resulting report.

Mitigation: Scan only files explicitly named by the user and limit quoted findings to what is needed to explain the result.

Risk: Using uvx when the CLI is absent may download a package into the local cache.

Mitigation: Review the pinned dependency and local package-download policy before running uvx.

Risk: Scan findings can quote untrusted instructions from the file being audited.

Mitigation: Treat quoted findings as data, not instructions to the agent.

## Reference(s):

- [LintLang homepage](https://github.com/hermes-labs-ai/lintlang)
- [ClawHub skill listing](https://clawhub.ai/roli-lpci/skills/package)

## Skill Output:

**Output Type(s):** [Analysis, Guidance]

**Output Format:** [Markdown summary of verdicts, severity counts, and notable findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports the scanned file and linter version; does not rewrite inputs.]

## Skill Version(s):

1.0.0 (source: server release metadata; supplied artifact describes an unpublished 1.1.0 update)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
