## Description:

Creates a set of four to eight materials stills answering Xiaohongshu hall FAQ complaints using confirmed document facts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Hall and public-service teams use this skill to turn public Xiaohongshu FAQ complaints and verified materials requirements into a reviewable set of still graphics. It does not publish posts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A shared account token and generic remote tool access may expose broad account permissions.

Mitigation: Install only if you trust Beatra's remote service; review the requested permissions and limit access to a trusted environment.

Risk: Confirmed image requests can spend account credits.

Mitigation: Review the planned stills and live costs before approving paid requests; check actual charges afterward.

Risk: Automatic updates can change installed behavior without separate confirmation.

Mitigation: Disable automatic updates if changes require explicit review.

Risk: Uninstalling may affect connection state shared with other Beatra skills.

Mitigation: Use the bundled uninstall flow and confirm the status of other installed Beatra skills before removing the connection.

Risk: Generated small text may misstate hall requirements.

Mitigation: Check each still against confirmed document facts before distribution.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/beatra-ai/skills/xiaohongshu-hall-faq-stills)
- [Hall FAQ still workflow](artifact/references/workflow.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)
- [Billing, errors, and recovery](artifact/references/billing-errors-and-recovery.md)
- [Uninstall and disconnect](artifact/references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Markdown, Guidance, Image artifacts]

**Output Format:** [Markdown with generated still-image artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Typically four to eight stills, with available image details and actual credit charges reported after each completed task.]

## Skill Version(s):

0.1.7 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
