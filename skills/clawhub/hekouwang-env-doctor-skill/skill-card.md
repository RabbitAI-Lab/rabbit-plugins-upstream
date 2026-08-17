## Description:

Scans macOS and Linux developer-tool storage, classifies directories as data, cache, or leftover tools, and guides users through evidence-based cleanup with an opt-in cleaner.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huiyonghkw](https://clawhub.ai/user/huiyonghkw)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to inspect local development-environment disk usage, distinguish reusable data from rebuildable caches and abandoned tool installs, and decide what to clean with explicit review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The cleaner can remove whitelisted cache or old tool directories after confirmation.

Mitigation: Run the read-only scan first, prefer clean.sh --dry-run before real cleanup, and review every selected item before confirming.

Risk: Misclassifying user data as cleanup material could cause data loss.

Mitigation: Follow the data/cache/leftover rules, keep data-class entries locked out of selection, and mark conflicting signals as uncertain instead of recommending deletion.

Risk: Removing an old version manager directory can leave broken shell initialization lines.

Mitigation: Warn users to review and clean related shell configuration lines after directory removal; do not edit shell configuration automatically.

## Reference(s):

- [Project homepage](https://github.com/huiyonghkw/hekouwang-env-doctor-skill)
- [Safety boundaries](references/safety.md)
- [Classification rules](references/rules.md)
- [Report workflow](references/report.md)
- [Doctor suite overview](references/doctor-suite.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown reports with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Cleanup guidance is staged for user review; destructive actions are routed through the interactive cleaner rather than generated as agent-executed commands.]

## Skill Version(s):

1.2.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
