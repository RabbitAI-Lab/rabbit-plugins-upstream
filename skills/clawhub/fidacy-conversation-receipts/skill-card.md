## Description: <br>
Fidacy Conversation Receipts helps agents create tamper-evident receipts for customer conversations by hashing messages locally, anchoring a digest through Fidacy, and sharing a public verification link. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fidacy](https://clawhub.ai/user/fidacy) <br>

### License/Terms of Use: <br>
Apache-2.0 <br>


## Use Case: <br>
Developers and teams running customer-facing AI agents use this skill for support, claims, quotes, refunds, scheduling, and other conversations where both sides may later need proof of exactly what was said. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Receipt metadata or hashes may be sent to a third-party verification service, and verify links may be publicly checkable. <br>
Mitigation: Install only after confirming Fidacy's retention, visibility, and access terms fit the intended use case. <br>
Risk: Sensitive context in labels or receipt metadata could expose private names, account numbers, medical details, contract identifiers, or similar information. <br>
Mitigation: Keep labels and metadata generic, and avoid adding sensitive context unless the organization's privacy review approves it. <br>
Risk: The receipt proves integrity and records authorization-gate activity, but it is not content moderation or a guarantee that an agent is allowed to make a commitment. <br>
Mitigation: Pair the skill with separate policy controls, content review, and business approval for actions such as refunds, claims, quotes, or contracts. <br>


## Reference(s): <br>
- [Fidacy signup](https://app.fidacy.com/signup) <br>
- [Fidacy verify](https://fidacy.com/verify) <br>
- [ClawHub skill page](https://clawhub.ai/fidacy/skills/fidacy-conversation-receipts) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Code, Configuration] <br>
**Output Format:** [Markdown with inline shell and JavaScript code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses a Fidacy API key for anchoring and returns public verification links for receipts.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
