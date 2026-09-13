## Description:

BIC-QA helps agents answer database and operating-system questions through the BIC-QA Open API with reusable multi-turn sessions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bbsyd2](https://clawhub.ai/user/bbsyd2)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, database administrators, and operations engineers use this skill to ask BIC-QA knowledge-base questions about database systems, operating systems, troubleshooting, operations, and performance optimization while preserving context across related follow-ups.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Questions are sent to the BIC-QA service using the user's API key.

Mitigation: Install and use the skill only when sending those questions to BIC-QA is acceptable for the user's environment.

Risk: API keys and local session state can be exposed if stored in shared, world-writable, or project-tracked locations.

Mitigation: Keep the API key file private, avoid shared state paths, and add project-local state directories to .gitignore.

## Reference(s):

- [BIC-QA homepage](https://www.bic-qa.com)
- [BIC-QA Open API quick reference](references/api.md)
- [ClawHub skill page](https://clawhub.ai/bbsyd2/skills/bic-qa)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown text with shell commands and BIC-QA API responses summarized for the user]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses should be based on the BIC-QA service output and may include a short local session identifier.]

## Skill Version(s):

2.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
