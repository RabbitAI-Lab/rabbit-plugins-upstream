## Description:

Creates draft construction quantity takeoffs and material plans from installation DWG drawings or scan indexes, with separate estimate and procurement views.

This skill is for research and development only.

## Publisher:

[lisong2003-lgtm](https://clawhub.ai/user/lisong2003-lgtm)

### License/Terms of Use:

CC-BY-NC-SA-4.0

## Use Case:

Construction estimators and engineers use this skill to draft installation quantity schedules and material plans from DWG drawings or existing scan indexes, then review unmatched or estimated items against the drawings. It does not price work or replace detailed takeoffs or settlement measurements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may automatically download, install, and run the external cad-file-reader dependency in the user's skill directory.

Mitigation: Review and preinstall the dependency, point CAD_SKILL_DIR to a reviewed copy, or disable automatic setup with SKILL_NO_BASE=1 or CAD_AUTO_SETUP=0 where appropriate.

Risk: Draft quantities can omit vertical runs or misclassify ambiguous labels and repeated equipment across drawings.

Mitigation: Review unmatched, inferred, and duplicate entries against the drawings and verify final quantities with professional takeoff tools.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/lisong2003-lgtm/skills/anzhuang-suanliang)
- [Loss and allowance rules](references/loss_rules.json)
- [Quantity standards and scope rules](references/standard_rules.json)
- [Estimate-to-material mapping rules](references/dual_caliber_rules.json)

## Skill Output:

**Output Type(s):** [Files, Text, Guidance]

**Output Format:** [Multi-sheet XLSX takeoff and material-plan drafts, JSON scan indexes, and review notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Draft quantities only; unmatched, ambiguous, and inferred items require manual review; no prices or settlement quantities.]

## Skill Version(s):

1.0.4 (source: ClawHub release; bundled artifact identifies itself as 0.4.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
