## Description:

Analyzes images or video of plant cuttings in transparent containers to assess rooting progress and suggest when to transplant.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Growers, home propagators, and agricultural researchers use images or video of cuttings to track root emergence without disturbing the plant, review prior reports, and inform transplant timing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Plant images, videos, or media URLs are sent to a cloud analysis service.

Mitigation: Review media before submission and avoid sensitive content until the publisher clarifies retention and deletion practices.

Risk: Reports are tied to an automatically managed identity, and session tokens are stored in the workspace data database.

Mitigation: Review the publisher's account-control practices and restrict access to the workspace and its stored session data.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-cutting-rooting-status-detection-analysis)
- [API reference](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis report or Markdown history table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include rooting-stage findings, transplant suggestions, and links to cloud reports; results can be saved to a file.]

## Skill Version(s):

1.0.12 (source: server-resolved ClawHub release; artifact frontmatter lists 1.0.17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
