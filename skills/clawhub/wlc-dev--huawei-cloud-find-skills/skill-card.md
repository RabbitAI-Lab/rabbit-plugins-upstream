## Description:

Searches, browses, and retrieves details for Huawei Cloud agent skills, then guides users through installing a selected skill.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wlc-dev](https://clawhub.ai/user/wlc-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI agents use this skill to find Huawei Cloud skills by keyword or category, review skill details, and get installation commands for a selected skill.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan rates this release suspicious with high confidence, reporting exposed cloud credentials, behavior beyond skill discovery, default-on telemetry, and persistent installation of an auxiliary CLI; inspection was incomplete.

Mitigation: Review the skill and scan guidance before use, inspect any credentials and behavior outside discovery, set SKILL_QUALITY_REPORT=0 to disable the documented telemetry, and review the auxiliary CLI installer before allowing it to run.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/wlc-dev/skills/huawei-cloud-find-skills)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands]

**Output Format:** [Markdown search results, skill details, and installation guidance with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results and commands depend on the requested skill and available network sources.]

## Skill Version(s):

1.0.8 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
