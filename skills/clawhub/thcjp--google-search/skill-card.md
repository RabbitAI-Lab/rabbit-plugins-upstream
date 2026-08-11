## Description:

Guides agents through Google Custom Search Engine setup and search workflows for current information gathering, SEO research, keyword analysis, and market research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, site operators, and agent users use this skill to configure Google Custom Search and run search workflows for fast information lookup, SEO optimization, keyword analysis, market research, and automated research tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Google Custom Search requires a Google API key and search engine ID, and mishandling those values can expose credentials.

Mitigation: Store credentials in a secret-safe .env file, do not commit them, and restrict API key access to the required Google API and expected environments.

Risk: The artifact includes an example command for a search script, but the evidence does not include that script.

Mitigation: Confirm the referenced script exists or adapt the command to the local implementation before executing it.

Risk: Search results can include sensitive, personal, copyrighted, or policy-restricted content.

Mitigation: Review retrieved content before using or redistributing it, and apply the relevant privacy, copyright, and platform policies for the use case.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/google-search)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with inline shell commands and environment variable examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Live searches require a Google API key and custom search engine ID.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
