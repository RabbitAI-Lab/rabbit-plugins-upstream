## Description:

Manage a user's Fitatu food diary, including meals, nutrition goals, body measurements, activity, and reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jezue](https://clawhub.ai/user/jezue)

### License/Terms of Use:

MIT-0

## Use Case:

Fitatu users can ask an agent to review their diary, log or update meals and activity, manage goals and measurements, and summarize nutrition progress. Developers can use the setup guidance to connect a Fitatu account through a supported MCP host.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote connections can expose the access token and private health records if traffic is unencrypted.

Mitigation: Prefer a local connection; for remote use require HTTPS or an encrypted tunnel, restrict network access, and protect the saved session and token.

Risk: Diary edits or deletions can unintentionally change personal records.

Mitigation: Use read-only mode for reports, establish Fitatu context before diary access, and keep confirmation controls enabled for changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jezue/skills/fitatu-diary)
- [Fitatu library project homepage](https://github.com/Jezue/fitatu_library)
- [Fitatu library agent guidance](https://github.com/Jezue/fitatu_library/blob/main/docs/AGENTS.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration]

**Output Format:** [Natural-language responses or Markdown; setup guidance may include YAML configuration and shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May summarize personal diary and nutrition data or guide account changes; food nutrient estimates are identified as estimates.]

## Skill Version(s):

1.1.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
