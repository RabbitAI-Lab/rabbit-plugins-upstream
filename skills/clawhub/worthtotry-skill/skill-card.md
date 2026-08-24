## Description:

Submit AI tools to WorthToTry by sending their URL and owner email for a draft listing and founder note review link via email.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fspecii](https://clawhub.ai/user/fspecii)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, founders, and launch teams use this skill to audit an AI product page, draft a WorthToTry listing, submit the product URL and owner email, and hand the owner a review flow to finish. The skill also guides agents on readiness checks, listing field limits, badge messaging, and what cannot be completed by an agent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The REST fallback workflow may require a personal access token, which could be exposed if pasted into normal chat.

Mitigation: Prefer the OAuth/MCP path where the agent never handles a token. If REST is necessary, provide only a minimal token through a secure secret mechanism and revoke it after the task.

Risk: Submitting a listing sends the product URL and owner email to WorthToTry.

Mitigation: Install and use the skill only when the user is comfortable sharing those fields with WorthToTry.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/fspecii/worthtotry-skill)
- [ClawHub skill page](https://clawhub.ai/fspecii/skills/worthtotry-skill)
- [WorthToTry directory](https://worthtotry.com)
- [WorthToTry hosted skill](https://worthtotry.com/skill.md)
- [WorthToTry API documentation](https://worthtotry.com/api-docs)
- [WorthToTry OpenAPI specification](https://worthtotry.com/api/v1/openapi.json)
- [Listing fields reference](references/listing-fields.md)
- [Readiness checks reference](references/readiness-checks.md)
- [REST API reference](references/rest-api.md)
- [MCP tools reference](references/mcp-tools.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include API request bodies, review links, readiness warnings, badge guidance, and owner handoff steps.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
