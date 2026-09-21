## Description:

Lazy senior dev mode for any coding task (write, refactor, fix, review): YAGNI, stdlib first, no unrequested abstractions. Not for non-coding requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dietrichgebert](https://clawhub.ai/user/dietrichgebert)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and coding agents use ponytail to bias coding tasks toward minimal, maintainable changes: reuse existing code, prefer standard library and native features, avoid unrequested abstractions, and keep explanations concise.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill persistently changes coding posture during a session and may produce narrower solutions or shorter explanations than expected.

Mitigation: Use it when a minimalist coding style is desired, and disable it with the documented phrases when broader design exploration, expansive explanations, or normal behavior is needed.

Risk: The skill encourages minimalism, which could be inappropriate for security-heavy analysis, trust-boundary validation, or other tasks that require deeper review.

Mitigation: Do not simplify away validation, error handling, security measures, accessibility basics, or explicitly requested work; disable the skill for tasks needing broader analysis.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dietrichgebert/skills/ponytail)
- [Project homepage](https://github.com/DietrichGebert/ponytail)
- [Publisher profile](https://clawhub.ai/user/dietrichgebert)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance, Markdown]

**Output Format:** [Markdown with code blocks and concise prose]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Emphasizes short working diffs, minimal explanations, and a small runnable check for non-trivial logic.]

## Skill Version(s):

4.9.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
