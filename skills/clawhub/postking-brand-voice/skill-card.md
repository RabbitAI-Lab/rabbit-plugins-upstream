## Description:

List and apply saved PostKing voice profiles when generating or rewriting content, then run a de-slop pass that removes LLM cliches and filler.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bitsandtea](https://clawhub.ai/user/bitsandtea)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing teams, founders, and content operators use this skill to find an existing PostKing voice profile, apply it to generated or rewritten copy, and make the result plainer and more specific before publication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-selected text is sent to PostKing tools for rewriting and style cleanup.

Mitigation: Avoid submitting confidential text unless the user's PostKing account and data-handling expectations allow it.

Risk: Brand-voice rewriting and de-slop passes can make AI-assisted writing sound more natural, which may create disclosure risk.

Mitigation: Do not use the skill to conceal AI authorship where a platform, client, publisher, or law requires disclosure.

Risk: AI-content checks can be misused as detector-score optimization instead of writing review.

Mitigation: Treat check_ai_content as a diagnostic that points to generic or templated passages for human revision.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bitsandtea/skills/postking-brand-voice)
- [Publisher profile](https://clawhub.ai/user/bitsandtea)
- [PostKing MCP endpoint](https://mcp.postking.app/mcp)
- [Skill icon asset](https://raw.githubusercontent.com/bitsandtea/postking-skills/main/assets/icons/postking-brand-voice.svg)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown guidance with PostKing tool-call examples, optional shell commands, and rewritten text returned by PostKing tools.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an authenticated PostKing account with credits and an existing voice profile; AI-content checks are diagnostic signals for human review.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
