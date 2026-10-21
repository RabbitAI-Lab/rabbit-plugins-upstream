## Description:

Produces preliminary construction finish quantity estimates and material plans from room schedules, drawings, finish specifications, and reviewed CAD measurement candidates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lisong2003-lgtm](https://clawhub.ai/user/lisong2003-lgtm)

### License/Terms of Use:

CC-BY-NC-SA-4.0

## Use Case:

Construction estimators and site engineers use this skill to draft finish-work quantities, preliminary cost estimates, and material procurement plans while tracking assumptions and items needing review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup may download, install, and run a CAD dependency despite documentation suggesting offline operation.

Mitigation: Review installation before running it; for offline use set SKILL_NO_BASE=1 and consider CAD_AUTO_SETUP=0, and avoid untrusted CAD_SKILL_DIR or CAD_FILE_READER_REPO locations.

Risk: Estimated quantities and reference prices may be mistaken for final commercial documents.

Mitigation: Verify measurements, project rules, and current prices; use the outputs as review drafts rather than final bids or settlement figures.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/lisong2003-lgtm/skills/zhuangshi-suanliang)

## Skill Output:

**Output Type(s):** [Files, Markdown, Text]

**Output Format:** [XLSX workbook, CSV tables, and Markdown report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Draft quantities and prices require review; check the stated noncommercial license before commercial reuse.]

## Skill Version(s):

0.9.20 (source: ClawHub release, SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
