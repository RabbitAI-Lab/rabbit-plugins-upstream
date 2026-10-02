## Description:

Collects completed call recordings, drafts call logs and recurring insights, and opens a reviewable pull request against a GTM repository.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales leaders, account executives, and revenue operations teams use this skill to turn recorded customer calls into reviewed repository logs and recurring GTM knowledge.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Untrusted call transcripts could influence an agent that can change repository files and open pull requests.

Mitigation: Treat transcripts as untrusted data, constrain changes to cadence and context paths, and require human review before merging.

Risk: The daily agent can access sensitive call content and a recorder API credential.

Mitigation: Limit the agent's environment and access; keep the recorder credential outside the LLM-driven scribing step where possible.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/cargo-ai/skills/call-capture)
- [Project homepage (skill metadata)](https://github.com/getcargohq/gtm-skills)
- [Recorder providers](references/providers.md)
- [Recorder API reference](references/recorder-apis.md)

## Skill Output:

**Output Type(s):** [Markdown, Code, Configuration, Shell commands]

**Output Format:** [Markdown call logs and knowledge updates in a reviewable pull request, with deployment instructions and configuration code]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scheduled daily capture; a human reviews and merges the pull request.]

## Skill Version(s):

0.1.1 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
