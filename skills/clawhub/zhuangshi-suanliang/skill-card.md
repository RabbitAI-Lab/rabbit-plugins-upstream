## Description:

Turns room schedules, finishes, construction methods, node details, and reviewed CAD measurement candidates into decoration budget estimates and material plans, with assumptions and items to verify.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lisong2003-lgtm](https://clawhub.ai/user/lisong2003-lgtm)

### License/Terms of Use:

CC-BY-NC-SA-4.0

## Use Case:

Estimators, site engineers, and construction teams can draft interior finish quantity estimates and material plans from room schedules and reviewed inputs, then check calculations, pricing assumptions, and missing details before procurement or commercial decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup may execute dependency bootstrap code despite the documented opt-out.

Mitigation: Review the setup behavior before installing or triggering dependency bootstrap; table-only calculations do not invoke this installer.

Risk: Imported method codes and estimates may need project-specific correction, and the CAD dependency and shared synchronization code are outside this package.

Mitigation: Review imported methods and estimates against project documents and independently review the CAD dependency and synchronization components before relying on them.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/lisong2003-lgtm/skills/zhuangshi-suanliang)

## Skill Output:

**Output Type(s):** [Files, Spreadsheets, CSV, Markdown]

**Output Format:** [Excel workbook (.xlsx), CSV files, and a Markdown report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Review-ready estimates include calculations, assumptions, evidence, and items needing confirmation; they are not final quantities or quotations.]

## Skill Version(s):

0.9.30 (source: artifact/SKILL.md frontmatter, artifact/manifest.json, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
