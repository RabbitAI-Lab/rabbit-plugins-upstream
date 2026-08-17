## Description:

SlickText (slicktext.com). Use this skill for ANY SlickText request -- reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage SlickText brand and contact workflows through an OOMOL-connected SlickText account, including contact lookup, listing, creation, updates, and deletion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create or update SlickText contacts through the connected account.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions.

Risk: The skill can delete SlickText contacts by contact ID.

Mitigation: Verify the target contact and obtain explicit approval before running destructive actions.

## Reference(s):

- [SlickText homepage](https://www.slicktext.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may return JSON connector responses that include data and meta.executionId.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
