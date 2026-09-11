## Description:

Starts a local AI reading companion for Chinese readers, with no-key demo mode, WeRead deep reading, Socratic dialogue, and a local Reader Memory Graph.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to run a local reading coach, diagnose configuration, search and analyze WeRead books, hold structured Socratic reading sessions, and organize cross-book concepts, stances, and unresolved questions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The local web app stores reading memory on disk and can include personal reading notes or copyrighted excerpts.

Mitigation: Use the local memory export and delete controls deliberately, keep the configured data directory private, and do not redistribute exported notes containing book excerpts.

Risk: Online mode can call WeRead and the user's selected model provider after consent.

Mitigation: Run demo mode when external calls are not desired, review provider settings before use, and avoid saving high-value model API keys in an untrusted local browser environment.

Risk: The release security summary flags process-stopping behavior for review before installation.

Mitigation: Review PID-file handling before deployment where accidental termination of another local process would be costly.

## Reference(s):

- [WeRead Agent API Reference](references/weread-api.md)
- [Project Homepage](https://github.com/bonniegeng-max/weread-socrates)
- [ClawHub Skill Page](https://clawhub.ai/bonniegeng-max/skills/weread-socrates)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and local web application output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May export reading notes and Reader Memory data as Markdown, JSON, or PNG from the local web app.]

## Skill Version(s):

1.3.1 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
