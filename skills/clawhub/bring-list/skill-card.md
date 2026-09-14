## Description:

Manage Bring! shopping lists by helping an agent set up Bring!, add, view, complete, uncomplete, remove, and batch-update grocery items through the Bring API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[maikimolto](https://clawhub.ai/user/maikimolto)

### License/Terms of Use:

MIT-0

## Use Case:

External users and their agents use this skill to set up Bring! access and manage personal or shared shopping lists from natural-language requests. It supports adding, viewing, checking off, unchecking, and removing items, including batch operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The built-in help gives unsafe password-storage guidance that conflicts with the skill's security claims.

Mitigation: Use only the interactive setup flow, do not paste a Bring password into chat, and do not add a password field to ~/.config/bring/credentials.json.

Risk: The skill stores a Bring refresh token locally.

Mitigation: Review before installing and treat the local token cache as sensitive account material.

Risk: Add, complete, and remove actions modify shopping lists immediately, including shared lists.

Mitigation: Confirm the target list and destructive actions before running commands that complete or remove items.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/maikimolto/skills/bring-list)
- [Publisher Profile](https://clawhub.ai/user/maikimolto)
- [Bring Website](https://getbring.com)
- [Bring API Endpoint](https://api.getbring.com/rest)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and optional JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires curl and jq; uses a local Bring profile and protected token cache.]

## Skill Version(s):

1.2.8 (source: package.json and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
