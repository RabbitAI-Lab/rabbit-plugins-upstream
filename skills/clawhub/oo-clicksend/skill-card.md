## Description:

Use this skill for ClickSend requests to read, create, update, and delete data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect ClickSend connector schemas and run account, contact-list, contact, pricing, and SMS actions through an OOMOL-connected ClickSend account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unverified remote installer commands may execute code on the user's machine if copied during setup.

Mitigation: Install the oo CLI only from a trusted, verified, versioned, or signed distribution path before using the skill.

Risk: The ClickSend connector can send SMS and create, update, or delete contacts and contact lists.

Mitigation: Confirm exact payloads and targets before write actions, and require explicit approval before destructive actions.

## Reference(s):

- [ClickSend homepage](https://www.clicksend.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-clicksend)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may return JSON data and execution metadata from the OOMOL connector.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
