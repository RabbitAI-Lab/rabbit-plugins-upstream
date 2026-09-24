## Description:

Convert RSS or Atom feed URLs into Markdown using the bundled local converter script.

This skill is ready for commercial/non-commercial use.

## Publisher:

[myx0m0p](https://clawhub.ai/user/myx0m0p)

### License/Terms of Use:


## Use Case:

Developers and agents use this skill to fetch public RSS or Atom feeds and convert feed items into readable Markdown, either to stdout or a workspace-relative .md file.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A crafted feed URL may bypass public-only URL protection and reach internal network services.

Mitigation: Use trusted feed URLs and run the skill in an environment without reachable internal services or metadata endpoints until the DNS-rebinding issue is fixed.

Risk: The converter makes outbound HTTP(S) requests from the execution environment.

Mitigation: Install and run it only where outbound feed fetching is acceptable for the workspace and data-handling policy.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/myx0m0p/skills/feed-to-md)
- [Publisher profile](https://clawhub.ai/user/myx0m0p)

## Skill Output:

**Output Type(s):** [markdown, files, shell commands, guidance]

**Output Format:** [Markdown text written to stdout or a workspace-relative .md file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports item limits, short or full templates, optional summaries, and summary length truncation.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
