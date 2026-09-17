## Description:

Operates Wit.ai through an OOMOL-connected account using the oo CLI for app, intent, entity, trait, utterance, language detection, and message analysis workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Wit.ai apps and NLP assets through an OOMOL-connected account, including reads, writes, destructive utterance deletion, language detection, and message analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that can execute local code.

Mitigation: Prefer verified official release or package-manager installation paths for the oo CLI, and run remote installer commands only after trusting the OOMOL source.

Risk: Write and destructive Wit.ai actions can change or delete app data.

Mitigation: Confirm the exact action, target, and payload with the user before write actions, and require explicit approval before destructive deletion.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-wit-ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Wit.ai homepage](https://wit.ai)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands should fetch the live connector schema before execution; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
