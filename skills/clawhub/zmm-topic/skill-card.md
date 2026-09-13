## Description:

詹明明·今天拍什么 helps a short-video creator evaluate and shape topics through interactive supply-demand checks, benchmark signals, first-party evidence, topic tension, and fit checks instead of generating a one-click topic list.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and agents assisting a single-person knowledge creator use this skill to diagnose whether a proposed short-video topic is worth making, generate evidence-backed candidates, or turn a flat topic into versions with tension before handing off to scripting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Mutable local vault rules and local scripts can change the skill's behavior after installation.

Mitigation: Install only in a private, trusted workspace and review the referenced vault rules and Python scripts before use.

Risk: Feedback, topic memory, and pipeline updates may persist user decisions or private content.

Mitigation: Require explicit confirmation before memory or pipeline writes and redact sensitive material before storage.

Risk: Processing private recordings or group conversations can expose personal or confidential information.

Mitigation: Process recordings only with consent and redaction, and avoid using private conversations as evidence without review.

Risk: Shell-form command execution with user-provided keywords can introduce command-injection risk.

Mitigation: Avoid shell-form execution with user keywords; prefer reviewed scripts with fixed arguments and explicit quoting.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/zmm-topic)
- [Publisher profile](https://clawhub.ai/user/iamzifei)
- [常识缺口法](references/常识缺口法.md)
- [找拉力](references/找拉力.md)
- [规则卡](references/规则卡.md)
- [议程与合集](references/议程与合集.md)
- [选题三路](references/选题三路.md)
- [Mode C evaluation sample result](evals/results/sample-01-v0.3.0.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands]

**Output Format:** [Markdown with structured topic diagnostics, candidate topics, evidence notes, numbered choices, and occasional inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires human review for topic selection, local data use, and any persistent memory or pipeline updates.]

## Skill Version(s):

0.2.9 (source: server release evidence; artifact frontmatter lists 0.4.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
