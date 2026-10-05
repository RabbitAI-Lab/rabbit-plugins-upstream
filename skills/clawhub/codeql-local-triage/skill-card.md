## Description:

Helps developers reproduce a single CodeQL alert locally, trace its data flow, isolate the cause with controlled variants, and verify a fix.

This skill is ready for commercial/non-commercial use.

## Publisher:

[elisabeth15501](https://clawhub.ai/user/elisabeth15501)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security engineers use this skill to investigate an individual CodeQL alert, distinguish a plausible false positive from a reproducible finding, and check a proposed fix before pushing it.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local source paths supplied to the scripts are read and copied for analysis; variant runs can overwrite their working directory.

Mitigation: Review the paths provided and use a disposable --workdir for variant runs.

Risk: CodeQL CLI or query-pack downloads may involve separately sourced software and network access.

Mitigation: Review any CodeQL CLI downloads separately and use a locally installed CLI when appropriate.

Risk: The name-based prefilter does not establish whether a finding is a real vulnerability or provide a complete security audit.

Mitigation: Confirm the baseline and variant results with CodeQL, inspect the data flow, and verify the fix with the target query.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/elisabeth15501/skills/codeql-local-triage)
- [CodeQL CLI setup and verification](artifact/references/running-codeql-cli.md)
- [Sensitive-data heuristics](artifact/references/sensitive-data-heuristics.md)
- [Troubleshooting FAQ](artifact/references/faq.md)
- [CodeQL Standard Libraries (upstream definitions)](https://github.com/github/codeql)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Shell commands]

**Output Format:** [Markdown with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Focused on one alert and its local reproduction; does not dismiss or close alerts.]

## Skill Version(s):

1.0.4 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
