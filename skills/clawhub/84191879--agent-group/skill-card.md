## Description:

A minimal Chinese-language helper for creating an agent group, adding predefined agent roles, listing members, and dissolving the group.

This skill is ready for commercial/non-commercial use.

## Publisher:

[84191879](https://clawhub.ai/user/84191879)

### License/Terms of Use:


## Use Case:

External users and developers can use this skill to manage a simple Chinese-language multi-agent group workflow with commands for creating a group, inviting supported agent roles, viewing members, and dissolving the group.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The command interface is Chinese-only, which may make group actions unclear to users who do not read Chinese.

Mitigation: Use only when operators understand the supported Chinese commands or provide translated operational guidance before deployment.

Risk: The skill stores group membership in a local OpenClaw memory JSON file until the group is dissolved.

Mitigation: Dissolve groups when they are no longer needed and review local workspace retention expectations before installation.

## Reference(s):


## Skill Output:

**Output Type(s):** [Text, Configuration]

**Output Format:** [Plain text Chinese status messages and local JSON group membership state]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Stores simple group membership locally until the group is dissolved.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
