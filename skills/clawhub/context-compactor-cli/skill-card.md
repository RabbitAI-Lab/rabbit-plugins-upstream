## Description:

Condense a long agent session transcript into a compact handoff memo: decisions, tasks, risks, facts & links. Credential values are auto-redacted before output (best-effort - review memos before sharing; --strict drops whole suspect lines). EN/RU heuristics, zero dependencies. The CLI prints what it reads and where it writes. Use ONLY with the user's explicit consent: tell the user which transcript file will be read.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vnbochkarev-netizen](https://clawhub.ai/user/vnbochkarev-netizen)

### License/Terms of Use:

MIT

## Use Case:

Developers, agent users, and operators use Context Compactor to turn long local session transcripts into concise handoff memos that preserve decisions, open tasks, risks, facts, and links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional npx use adds an external npm package and publisher trust boundary.

Mitigation: Use the reviewed local Python command when possible; only use the pinned npx package when comfortable trusting the package and publisher.

Risk: Credential redaction is best-effort, so generated handoff memos may still contain sensitive details.

Mitigation: Review generated memos before sharing; use --strict when transcripts may contain credentials, tokens, private URLs, or other sensitive values.

Risk: The tool reads a transcript file selected by the operator.

Mitigation: Get explicit consent and state which transcript file will be read before running it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/vnbochkarev-netizen/skills/context-compactor-cli)
- [npm package @vibo-dev/context-compactor](https://www.npmjs.com/package/@vibo-dev/context-compactor)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown handoff memo with command-line status messages]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reads one user-selected transcript and optionally writes one memo file; redaction is best-effort, so generated memos should be reviewed before sharing.]

## Skill Version(s):

1.1.7 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
