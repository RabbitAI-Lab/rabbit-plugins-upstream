## Description:

Maps a profile request to a setting key and creates a local review item for that key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Workspace administrators and developers use this skill to select a supported profile setting key from a request and prepare a local governance review item for that setting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A generated review item could be mistaken for an approved governance action.

Mitigation: Review the generated JSON before treating it as approved; a local review item does not confirm external action.

Risk: Downstream requests write local artifacts under the selected output directory.

Mitigation: Choose a dedicated writable output directory and inspect its contents after execution.

## Reference(s):

- [Profile Governance Desk release](https://clawhub.ai/wxt-ai/skills/profile-governance-desk)
- [Profile Setting Directory documentation](operations/upstream/README.md)
- [Profile Governance Register documentation](operations/downstream/README.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Files]

**Output Format:** [JSON setting key or review item, with a local review artifact for downstream requests]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Downstream requests require a writable output directory; a local review item does not confirm approval.]

## Skill Version(s):

3.0.0 (source: release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
