## Description:

Audit AI-generated code before shipping. Static + AST scan for hardcoded secrets, SQL injection, eval/exec, shell injection, unsafe deserialization and TLS issues, with severity-capped 0-100 scoring and SARIF/JSON/Markdown reports. Optional autofix - every current fix changes behavior and requires the explicit --fix-unsafe opt-in; baseline export for legacy code. Zero-dependency Python CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thiennhant95](https://clawhub.ai/user/thiennhant95)

### License/Terms of Use:

MIT

## Use Case:

Developers use vibecheck to audit AI-generated or other code before merging or shipping. It reports pattern-based security and quality findings and can gate CI with score and severity thresholds.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan reports a benign result with medium confidence and advises reviewing the installation mechanism for this third-party skill.

Mitigation: Review the skill contents and its declared file and environment access before installing it through ClawHub.

Risk: The scanner uses static analysis with documented blind spots, including no cross-file data-flow analysis, so some issues can go undetected.

Mitigation: Use its results as a pre-merge aid alongside code review or broader security analysis.

Risk: Optional autofixes change code behavior and write changes within the scanned root.

Mitigation: Preview with --fix-dry-run, review the proposed diff, and use --fix with --fix-unsafe only when the changes are intended.

## Reference(s):

- [Project page (listed in package documentation)](https://github.com/thiennhant95/vibecheck)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown, JSON, SARIF]

**Output Format:** [Text, Markdown, JSON, or SARIF security and quality reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include a 0–100 score, severity, and evidence; behavior-changing autofixes require explicit opt-in.]

## Skill Version(s):

1.0.11 (source: release evidence, SKILL.md, vibecheck.py)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
