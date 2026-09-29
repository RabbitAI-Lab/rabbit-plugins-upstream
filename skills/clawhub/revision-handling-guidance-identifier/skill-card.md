## Description:

Generates concise account merge guidance from a supplied revision profile.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

People handling routine account maintenance use this skill to turn a supplied revision profile into guidance on merging incoming account fields and preserving existing values.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Merge guidance may be inappropriate for a particular account or revision policy.

Mitigation: Review the guidance and account-specific preservation requirements before applying changes to real account data.

Risk: Future package or configuration changes could enable file-writing behavior.

Mitigation: Review future versions and configuration before allowing the skill to write files or update real account data.

## Reference(s):

- [Account Merge Guide on ClawHub](https://clawhub.ai/wxt-ai/skills/revision-handling-guidance-identifier)

## Skill Output:

**Output Type(s):** [Text]

**Output Format:** [JSON object containing a merge_guidance string]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns guidance only; does not update account records.]

## Skill Version(s):

1.1.0 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
