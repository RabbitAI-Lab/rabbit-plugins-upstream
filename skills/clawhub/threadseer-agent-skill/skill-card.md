## Description:

Threadseer transforms transcripts, meetings, chats, interviews, voice notes, and other conversational material into evidence-backed decision briefs, recommendations, action plans, risk and insight analyses, team reports, follow-up drafts, JSON, or institutional memory while separating stated evidence from inference.

This skill is ready for commercial/non-commercial use.

## Publisher:

[antreasantoniou](https://clawhub.ai/user/antreasantoniou)

### License/Terms of Use:

MIT

## Use Case:

Employees, external collaborators, and developers use Threadseer to turn approved conversation material into source-grounded decisions, action plans, recommendations, reports, follow-up drafts, or durable memory records. It is most useful when the reader needs clear separation between what participants stated, what the analysis infers, and what action is recommended next.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installer commands or unreviewed sources could install content the user did not intend to trust.

Mitigation: Install from a reviewed source when possible, prefer a manual clone/copy route or pinned verified installer, and avoid administrator privileges.

Risk: Conversation material may contain private transcripts, identifiers, secrets, or sensitive drafts, and the agent host may transmit supplied content to its configured model provider.

Mitigation: Use only material the user is authorized to process, review the agent host's data boundary before sensitive use, and keep original evidence private and unchanged.

Risk: Generated reports, follow-ups, or memory drafts could disclose sensitive details or be mistaken for authorized external actions.

Mitigation: Review shareable reports and durable memory drafts before posting or saving them, and perform external or durable writes only with explicit user authority.

## Reference(s):

- [Evidence Policy](references/evidence-policy.md)
- [Analytical Lenses](references/lenses.md)
- [Output Contracts](references/output-contracts.md)
- [ClawHub Skill Page](https://clawhub.ai/antreasantoniou/skills/threadseer-agent-skill)
- [Publisher Profile](https://clawhub.ai/user/antreasantoniou)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, guidance, shell commands]

**Output Format:** [Markdown or JSON, with optional shell commands for local helper scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include source locators, epistemic labels, private/shareable variants, action registers, validation notes, and concise excerpts when supported by the supplied material.]

## Skill Version(s):

1.0.0 (source: release metadata and CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
