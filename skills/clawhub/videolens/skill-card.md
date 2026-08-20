## Description:

Turn videos into professional timestamped reports. Use for YouTube summaries, tutorials, meetings, bugs, UX, privacy, and creator QA.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shadoprizm](https://clawhub.ai/user/shadoprizm)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, creators, and external users use VideoLens.io to generate timestamped reports from authorized YouTube, local, or supported video sources for summaries, tutorials, meetings, bug reports, UX review, privacy review, and creator QA.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill downloads and installs external runtime code before analysis.

Mitigation: Run bootstrap only in an environment where fetching the pinned VideoLens runtime and installing Python dependencies is acceptable.

Risk: The analysis child process inherits the full parent environment.

Mitigation: Run with a minimal environment and use VIDEOLENS_SKILL_STATE_DIR for isolated state when practical.

Risk: Analysis uses the user's OpenAI API key and can spend API credits.

Mitigation: Require explicit user confirmation and set allow_credit_spend=true only after that confirmation.

Risk: Generated reports may miss privacy, compliance, or factual issues in the source video.

Mitigation: Ask users to verify consequential findings against cited timestamps and avoid promising exhaustive detection.

## Reference(s):

- [VideoLens.io](https://videolens.io)
- [Open VideoLens for Chrome](https://videolens.io/chrome)
- [VideoLens source repository](https://github.com/shadoprizm/videolens)
- [ClawHub VideoLens.io skill page](https://clawhub.ai/shadoprizm/skills/videolens)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Files, Guidance]

**Output Format:** [JSON status and artifact paths, with generated HTML, Markdown, and JSON report files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Analysis requires explicit allow_credit_spend=true; max_frames is bounded from 1 to 80.]

## Skill Version(s):

1.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
