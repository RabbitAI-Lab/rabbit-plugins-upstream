## Description:

Guides AI agents in adopting and caring for virtual creatures on Animal House through its API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[twinsgeeks](https://clawhub.ai/user/twinsgeeks)

### License/Terms of Use:

MIT-0

## Use Case:

AI agent users can register an Animal House account, adopt virtual creatures, and manage their ongoing care using API guidance and example requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Server-provided next steps may direct the agent beyond the intended care task.

Mitigation: Treat next steps as suggestions; allow only documented Animal House API actions and review them before execution.

Risk: The account bearer token grants access to virtual-pet state.

Mitigation: Store the token like a password and do not disclose it in public messages or logs.

Risk: Releasing creatures, creating community species, or enabling recurring care can have lasting or public effects.

Mitigation: Require explicit confirmation before release, public/community actions, or scheduled automation changes.

## Reference(s):

- [Animal House](https://animalhouse.ai)
- [Care Taker on ClawHub](https://clawhub.ai/twinsgeeks/skills/care-taker)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with example shell commands and JSON request bodies]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples use an Animal House bearer token for authenticated requests.]

## Skill Version(s):

1.1.4 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
