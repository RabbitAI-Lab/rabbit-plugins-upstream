## Description:

Creates mnemonic songs from exam knowledge points, starting with one song and then expanding to the rest of a syllabus as a set.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External exam candidates use the skill to turn facts they already know into a mnemonic song for one exam knowledge point, then create songs for the remaining syllabus points after approving each paid song or batch.

### Deployment Geography for Use:

Global, using Beatra's international services or its documented mainland China services.

## Known Risks and Mitigations:

Risk: The skill requests broader account permissions than its music-generation task needs.

Mitigation: Review permissions before connecting; prefer music-only access if available, and revoke access in the Beatra Console when appropriate.

Risk: Approved lyrics are sent to Beatra and installation analytics are sent automatically.

Mitigation: Avoid confidential inputs and account for automatic installation analytics.

Risk: Song generation is paid, and removal may disrupt other Beatra skills.

Mitigation: Approve each paid song or batch, and check for other Beatra skills before removal; access can also be revoked in the Beatra Console.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/beatra-ai/skills/exam-mnemonic-song)
- [Beatra skill page](https://beatra.ai/skills/exam-mnemonic-song)
- [Exam mnemonic workflow](artifact/references/workflow.md)
- [Billing, errors, and recovery](artifact/references/billing-errors-and-recovery.md)
- [Updates and security](artifact/references/updates-and-security.md)
- [Beatra MCP service](https://mcp.beatra.ai/mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Audio]

**Output Format:** [Markdown lyric sheets and generated mnemonic-song audio]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Songs are prepared one knowledge point at a time; the user reviews and approves each paid song or batch.]

## Skill Version(s):

0.2.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
