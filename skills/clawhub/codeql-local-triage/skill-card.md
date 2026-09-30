## Description:

Helps developers reproduce a specific CodeQL alert locally, trace its data flow, test one-change variants, and verify a fix before pushing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[elisabeth15501](https://clawhub.ai/user/elisabeth15501)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security engineers use this skill to investigate a specific CodeQL finding, distinguish a reproducible false positive from a real issue, and check a proposed fix locally. It does not replace whole-repository audits or GitHub's alert workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bisection copies the target source tree and writes artifacts under <tree>/_bisect by default; repeated runs replace variant directories there.

Mitigation: Pass an explicit temporary --workdir outside the repository, such as /tmp/taint_bisect, and review generated artifacts before committing.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/elisabeth15501/skills/codeql-local-triage)
- [Running the CodeQL CLI](references/running-codeql-cli.md)
- [Sensitive-data heuristics](references/sensitive-data-heuristics.md)
- [CodeQL standard libraries](https://github.com/github/codeql)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and a variant verdict table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can describe SARIF source-to-sink paths and local fix-verification results.]

## Skill Version(s):

1.0.1 (source: SKILL.md frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
