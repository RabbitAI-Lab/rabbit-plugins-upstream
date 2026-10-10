## Description:

Connects an AI assistant to Clip2MD to save web pages as Markdown, check quota and task status, and retrieve results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[clip2md](https://clawhub.ai/user/clip2md)

### License/Terms of Use:

MIT-0

## Use Case:

People using an AI assistant can connect their Clip2MD account, submit web pages for Markdown conversion, check quota and task progress, and retrieve completed results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted URLs and processed page content are sent to the Clip2MD service.

Mitigation: Submit only pages the user intends to share with Clip2MD.

Risk: A generated authorization statement contains a sensitive one-time credential that grants assistant access.

Mitigation: Share it only with a trusted assistant, never expose the code in logs or command arguments, and disconnect when access is no longer wanted.

Risk: Submitting some links can consume permanent quota.

Mitigation: Explain quota costs before submission and report actual consumption from the service response.

## Reference(s):

- [Clip2MD skill on ClawHub](https://clawhub.ai/clip2md/skills/clip2md)
- [Clip2MD](https://clip2.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Plain text or Markdown; optional JSON for command results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports task status, task ID, and quota use when available; shares full Markdown on request.]

## Skill Version(s):

0.1.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
