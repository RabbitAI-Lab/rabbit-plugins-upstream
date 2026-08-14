## Description:

Manages agent progress reporting and OKF-compliant memory syncing to Fulcra.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fulcra](https://clawhub.ai/user/fulcra)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and developers use this skill to keep progress reports, role files, session summaries, task records, knowledge files, and inbox archives synchronized with Fulcra as OKF-compliant Markdown.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Progress reports, session summaries, task files, or knowledge files could include sensitive user content or private agent reasoning before cloud sync.

Mitigation: Review generated summaries before upload, minimize disclosures, and exclude credentials, sensitive personal data, and private internal reasoning.

Risk: Inbox cleanup could delete a message before the useful content has been preserved.

Mitigation: Confirm the item has been archived under the timestamped archive path before allowing deletion from the inbox.

Risk: The skill stores agent memory in Fulcra-backed cloud storage.

Mitigation: Install it only when Fulcra storage is intended for progress, session, task, and selected knowledge records.

## Reference(s):

- [Fulcra Memory CLI Reference](references/fulcra-memory-cli.md)
- [Fulcra CLI documentation](https://raw.githubusercontent.com/fulcradynamics/agent-skills/main/skills/fulcra-get-started/references/fulcra-cli.md)
- [Open Knowledge Format specification](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)
- [ClawHub skill page](https://clawhub.ai/fulcra/skills/fulcra-memory)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and OKF file conventions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces Fulcra CLI command guidance and Markdown memory file structure; it does not directly execute commands without agent action.]

## Skill Version(s):

0.1.9 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
