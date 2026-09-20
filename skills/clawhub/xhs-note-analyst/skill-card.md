## Description:

Analyzes an XHS creator's own official backend metrics, benchmarks recent notes against public high-performing notes, and produces an HTML/Markdown diagnosis with funnel health and improvement actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fatmind](https://clawhub.ai/user/fatmind)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and their agents use this skill to analyze recent XHS note performance from official creator-backend exports, identify funnel weaknesses, compare against public high-performing notes, and plan concrete follow-up actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill automates a logged-in XHS Chrome session.

Mitigation: Review before installing, use only with accounts you are comfortable automating, and prefer an isolated browser profile for sensitive accounts.

Risk: The skill exports creator analytics and writes reports and intermediate files locally.

Mitigation: Run it in a trusted local environment, choose output paths deliberately, and review generated files before sharing them.

Risk: The skill sends analysis prompts through the webclaw3 local pipeline and has a configurable LLM endpoint.

Mitigation: Verify that WC3_LLM_ENDPOINT is unset or points only to an endpoint you trust before running the skill.

Risk: The release includes an obfuscated LLM helper.

Mitigation: Prefer pinned or verified install commands and scan/review the package before deployment.

## Reference(s):

- [ClawHub listing: xhs-note-analyst](https://clawhub.ai/fatmind/skills/xhs-note-analyst)
- [webclaw3 browser automation dependency](https://clawhub.ai/fatmind/skills/webclaw3-browser-automation)
- [webclaw3 source and install guide](https://github.com/fatmind/webclaw3)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [HTML report, Markdown data file, JSON status summary, and stdout JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes local report artifacts to configured output paths; status may be success, partial, or failed.]

## Skill Version(s):

1.1.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
