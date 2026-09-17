## Description:

Provides an agent workflow for reading and querying Mixpanel data through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Mixpanel connector schemas, export raw events, list saved analytics objects, and query funnels, retention, segmentation, profile activity, top events, and saved reports from a connected Mixpanel account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup tells users to execute an unverified remote installer for the oo CLI.

Mitigation: Review the installer path before installing, and prefer a pinned, signed, or checksum-verified installation method.

Risk: The skill can read or export Mixpanel data from a connected account.

Mitigation: Use it only when the user intentionally wants the agent to access Mixpanel data through the connected account.

Risk: The trigger language is broader than necessary for Mixpanel-related requests.

Mitigation: Apply the skill only to Mixpanel data access or analytics tasks where the OOMOL connector is the intended path.

## Reference(s):

- [ClawHub Mixpanel Skill](https://clawhub.ai/oomol/skills/oo-mixpanel)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Mixpanel](https://mixpanel.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON connector payload/output descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill directs agents to inspect live connector action schemas before building payloads and to run Mixpanel connector actions with JSON input and output.]

## Skill Version(s):

1.0.3 (source: server evidence release.version and metadata.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
