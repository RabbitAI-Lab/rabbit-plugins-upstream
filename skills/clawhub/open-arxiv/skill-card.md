## Description:

Open arXiv in the user's Brave browser and take the user to the arXiv research-paper homepage, reusing an existing arXiv tab when possible.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ruchir17-cmd](https://clawhub.ai/user/ruchir17-cmd)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to open the arXiv homepage in Brave, reuse an existing arXiv tab when available, and confirm the expected site is loaded.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can focus Brave and reuse an existing browser session, including a signed-in session if one exists.

Mitigation: Run it only when browser navigation to arXiv is intended; the skill stops at login and does not request, store, or enter credentials.

Risk: Browser automation may navigate or focus an unexpected tab if the local browser state is ambiguous.

Mitigation: Verify the visible destination is arXiv before relying on the result; the skill includes destination verification as its success condition.

## Reference(s):

- [arXiv](https://arxiv.org/)
- [ClawHub skill page](https://clawhub.ai/ruchir17-cmd/skills/open-arxiv)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Plain text browser automation guidance with configuration values]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Opens or focuses Brave, reuses a matching arXiv tab when available, and stops at login without handling credentials.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
