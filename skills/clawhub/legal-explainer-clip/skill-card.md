## Description:

Creates a labeled digital-human still, a speakable script, and a short talking clip about a public-education legal topic for law-firm marketing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Lawyers and firm marketing teams use this skill to plan and produce short, labeled public-education legal explainers. It does not address individual cases or predict outcomes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connecting a Beatra account creates a shared local Device Token that can authorize account activity.

Mitigation: Connect only an account you intend to use, protect local credentials, and revoke device authorization in the Beatra Console when no longer needed.

Risk: Approved still, speech, and video requests can spend Beatra credits.

Mitigation: Review current prices and approve each paid stage separately; do not replay an uncertain request without checking its task status.

Risk: The package silently updates its own files by default.

Mitigation: Review updates before use or disable automatic updates with `python3 scripts/mcp_client.py update --auto off`.

Risk: A legal explainer may mislead viewers if it implies legal advice or a real lawyer is speaking.

Mitigation: Keep scripts to confirmed general information, exclude identifiable cases, and check the required non-lawyer label remains readable.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/beatra-ai/skills/legal-explainer-clip)
- [Legal explainer workflow](references/workflow.md)
- [Beatra skill homepage](https://beatra.ai/skills/legal-explainer-clip)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [Text, Guidance, Media files]

**Output Format:** [Markdown still plan and narration script; generated image, audio, and video files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a visible non-lawyer presenter label and separate approval before paid generation steps.]

## Skill Version(s):

0.1.8 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
