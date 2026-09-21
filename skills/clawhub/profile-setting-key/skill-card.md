## Description:

Combines profile setting key selection with creation of a profile-setting review item.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Workspace governance operators and agents use this skill to map a profile-setting request to an approved setting key and create a matching profile-setting review item.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The referenced profile-setting tools may not be available in the target agent environment.

Mitigation: Confirm that select_profile_setting_key and create_setting_review_item are installed and callable before relying on the skill in a workflow.

Risk: A generated review item may not match the organization's governance process.

Mitigation: Review the selected setting key and expected value type against the local governance register before applying the handoff.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/profile-setting-key)

## Skill Output:

**Output Type(s):** [text, guidance, configuration]

**Output Format:** [Structured text containing a setting_key and review_item]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No credentials, persistence, private-file access, or executable code are described in the release evidence.]

## Skill Version(s):

1.0.7 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
