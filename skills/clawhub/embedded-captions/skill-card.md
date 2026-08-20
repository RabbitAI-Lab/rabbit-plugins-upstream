## Description:

Add captions or subtitles to existing single-subject talking-head videos while preserving the footage, with identity-driven options for verbatim rails, cinematic embedded captions, and VFX-style caption treatments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and media operators use this skill to guide agents through selecting a caption identity, preparing a local talking-head video project, authoring caption configuration, previewing frames, and rendering a captioned MP4.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may change or update related Hyperframes skills before use.

Mitigation: Require explicit approval before running update commands and review the installed skill versions before deployment.

Risk: The workflow may download models or packages on first use and relies on networked or external code.

Mitigation: Run the workflow in a contained project directory with network access limited to approved dependency sources.

Risk: The workflow renders local project HTML with Chromium.

Mitigation: Review generated HTML and project inputs before rendering, especially when inputs or configuration are user-supplied.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/embedded-captions)
- [Caption identity catalog](CATALOG.md)
- [DNA registry](dna/README.md)
- [Theme mode guide](themes/README.md)
- [Rail guidance](references/rail.md)
- [Composition craft](references/composition-craft.md)
- [Layout heuristics](references/layout-heuristics.md)
- [Failure modes](references/failure-modes.md)
- [GSAP distribution](https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code, Markdown]

**Output Format:** [Markdown guidance with inline shell commands and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local project files and rendered video outputs through the commanded toolchain.]

## Skill Version(s):

1.0.10 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
