## Description:

Keelwright helps AI coding agents run autonomous coding loops with machine-enforced safety gates, an autonomy dial, circuit breakers, web-defense checks, and plain-language reporting for users who cannot review every generated line of code.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ratingtesting](https://clawhub.ai/user/ratingtesting)

### License/Terms of Use:

MIT No Attribution

## Use Case:

External users, developers, and non-developer builders use Keelwright to guide AI coding agents through autonomous implementation sessions while checking for common security, correctness, dependency, loop-control, and reporting failures.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent to write local state files, run shell or Python commands, perform network checks, and affect production workflows.

Mitigation: Review the skill before installation, use it only in repositories where broad agent automation is acceptable, and disable or rewrite bootstrap, update-check, persistence, weekly self-improvement, and rollback behavior unless explicitly wanted.

Risk: Local progress, attack-log, and memory files can be accidentally committed or treated as durable project artifacts.

Mitigation: Keep attack logs and L4 memory files out of commits, add local scratch files to ignore rules, and delete or rotate them when they are no longer needed.

Risk: Optional import checks or installs can execute commands in an environment the user has not vetted.

Mitigation: Do not run import --run-checks or optional installation steps unless the package and execution environment are trusted.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ratingtesting/skills/keelwright)
- [Publisher profile](https://clawhub.ai/user/ratingtesting)
- [ClawDIS author profile](https://github.com/ratingtesting)
- [README](README.md)
- [Security gates](references/security-gates.md)
- [Circuit breaker](references/circuit-breaker.md)
- [Web Guard](references/web-guard.md)
- [QA results](qa-results/README.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline code blocks, shell commands, checklists, and file-based evidence instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct the agent to create or update local evidence, progress, attack-log, and verification files when the user has opted into the relevant workflow.]

## Skill Version(s):

1.6.4 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
