## Description:

Guides an agent in operating selected logged-in websites through AgentPMT to extract information and complete browser workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agentpmt](https://clawhub.ai/user/agentpmt)

### License/Terms of Use:

MIT-0

## Use Case:

External users and their agents use this skill to work within selected authenticated websites, such as posting content, updating CRM records, submitting forms, and retrieving reports or files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An agent can post, submit forms, or change records inside logged-in accounts.

Mitigation: Connect only necessary accounts, restrict browsing policy, and require confirmation before posting, submitting, or updating records.

Risk: Downloads and session recordings can persist account content as files.

Mitigation: Require confirmation before exporting files or recording sessions and review saved artifacts.

Risk: Supporting skills installed from unpinned sources can change unexpectedly.

Mitigation: Prefer pinned or OpenClaw installation routes for supporting skills.

## Reference(s):

- [AstroBrowse on ClawHub](https://clawhub.ai/agentpmt/skills/astrobrowse-authenticated-agentic-browser)
- [AgentPMT AstroBrowse product](https://www.agentpmt.com/marketplace/astrobrowse-authenticated-agentic-browser)
- [AstroBrowse setup guide](https://www.agentpmt.com/docs/tool-specific/astrobrowse)
- [AgentPMT account setup on ClawHub](https://clawhub.ai/agentpmt/agentpmt-account-mcp-rest-api-setup)

## Skill Output:

**Output Type(s):** [Text, JSON, Files]

**Output Format:** [Browser page extracts and structured tool responses; saved file artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Screenshots, recordings, and downloaded files may be saved to File Manager.]

## Skill Version(s):

1.0.1 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
