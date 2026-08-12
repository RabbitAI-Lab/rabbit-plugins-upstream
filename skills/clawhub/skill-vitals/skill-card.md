## Description:

skill-vitals helps agents audit installed Agent Skills for trigger failures, context cost, stale or shadowed skills, and supply-chain security issues.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gold3bear](https://clawhub.ai/user/gold3bear)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to audit installed skill libraries, identify why skills fail to trigger, compare context cost with real usage, and decide what to keep, fix, split, or remove.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Raw scan JSON can expose absolute paths, usernames, skill names, and full skill descriptions.

Mitigation: Use the documented --redact and --redact-names options before sharing scan output outside the local environment.

Risk: The optional log-probing script can inspect local session and history directories.

Mitigation: Run log probing only after confirming which directories will be inspected, and prefer the normal skillUsage path when available.

Risk: Security scan findings are heuristic and can include both false positives and false negatives.

Mitigation: Review flagged lines manually and do not treat a clean scan as a substitute for a security audit.

Risk: The server security guidance notes a reliability issue where scan.py may crash when ~/.claude.json is absent.

Mitigation: Verify standalone operation on the target host before relying on results, especially outside Claude Code environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gold3bear/skills/skill-vitals)
- [Publisher profile](https://clawhub.ai/user/gold3bear)
- [Project homepage](https://github.com/gold3bear/skill-vitals)
- [Snyk ToxicSkills research](https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub/)
- [Microsoft SkillOpt](https://github.com/microsoft/SkillOpt)

## Skill Output:

**Output Type(s):** [Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown health report with optional JSON scan artifacts and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include local file paths, skill names, descriptions, usage counts, and scanner findings; redaction options are documented for sharing outputs.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
