## Description:

Collects buyer reviews from a JD.com product page through a logged-in Chrome session and exports deduplicated review data to local Markdown and JSON files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fatmind](https://clawhub.ai/user/fatmind)

### License/Terms of Use:

MIT-0

## Use Case:

External users and commerce analysts use this skill to collect JD.com buyer-review data for product selection, review analysis, and complaint analysis. It is intended for cases where the user provides a JD.com product URL and asks an agent to export product reviews or buyer comments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill controls a logged-in Chrome session while collecting JD.com page data.

Mitigation: Run it in a separate low-privilege Chrome profile and avoid using sessions that contain sensitive account data.

Risk: The security evidence flags an obfuscated LLM helper that may pass account or page data to a local endpoint.

Mitigation: Keep WC3_LLM_ENDPOINT unset unless it is pinned to a trusted local service.

Risk: The security evidence flags unsafe file-write behavior through configurable output filenames.

Mitigation: Use simple basename output filenames and review the source before installation until file-write validation is fixed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fatmind/skills/jd-review-export)

## Skill Output:

**Output Type(s):** [text, markdown, json, files]

**Output Format:** [Markdown table files and JSON status metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes reviews.md and data.md with exported review rows, writes res.json with status and run metadata, and prints a one-line JSON status summary to stdout.]

## Skill Version(s):

1.0.1 (source: ClawHub server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
