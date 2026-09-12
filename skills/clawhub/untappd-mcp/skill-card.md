## Description:

Search Untappd beers, breweries, and venues; read user profiles, check-ins, wishlists, distinct beers, badges, friends, and friend activity feeds; and post check-ins, toasts, and comments to the configured Untappd account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query Untappd beer, brewery, venue, and account activity data, then optionally prepare account actions such as check-ins, toasts, comments, wishlist changes, or friend actions with confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to provide an Untappd password and reverse-engineered mobile app credentials.

Mitigation: Install only if comfortable giving the skill those credentials, and keep them in private environment variables or secret storage.

Risk: The skill can read and cache Untappd account and activity data locally.

Mitigation: Treat the local cache as private account/activity data and protect or delete it according to the user's privacy needs.

Risk: The skill can post check-ins, comments, toasts, wishlist changes, or friend actions to the configured Untappd account after confirmation.

Mitigation: Verify every proposed account action before setting confirm: true.

Risk: The security summary reports inconsistent account-write documentation that requires review before installation.

Mitigation: Review the documented write behavior and confirmation requirements before enabling the skill.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/untappd-mcp)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with tool names, setup steps, and structured Untappd result or receipt descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read tools may return compact or full views where supported; write tools use dry-run previews unless explicitly confirmed.]

## Skill Version(s):

1.11.3 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
