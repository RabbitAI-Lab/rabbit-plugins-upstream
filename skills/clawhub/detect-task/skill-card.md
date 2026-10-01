## Description:

Reviews AI-generated ecommerce images before publication and reports visual risks, eight itemized checks, and prompt corrections for reruns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Ecommerce creators and marketing teams use the skill to screen AI-generated product images before publishing, identify defects, and draft corrections for a rerun or manual retouching.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Inspection images may be uploaded to third-party cloud model providers, including an unexpected provider selected automatically.

Mitigation: Use only images suitable for cloud processing and explicitly choose and review the provider before sending them.

Risk: Bundled scripts can initiate generation and reruns beyond image inspection, potentially incurring charges or producing additional files.

Mitigation: Review the requested command and run a dry-run first when possible; require user approval before generation or repeated runs.

## Reference(s):

- [Provider CLI and data flow](references/provider-cli.md)
- [Model flags](references/model-flags.md)
- [Platform image specifications](references/platform-specs.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Shell commands]

**Output Format:** [Markdown report with a risk level, eight checks, publishing recommendation, and prompt corrections]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports batch screening and optional rerun guidance.]

## Skill Version(s):

1.0.16 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
