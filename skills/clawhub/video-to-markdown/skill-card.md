## Description:

Analyzes YouTube, Facebook, and Instagram video URLs by combining extracted frames, transcripts, and Claude vision to generate a comprehensive Markdown reference document.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gmdeep](https://clawhub.ai/user/gmdeep)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, educators, and other external users use this skill to turn supported video URLs into structured notes that capture both narration and important visual content. It is especially useful for tutorials, technical demos, trading videos, and other content where on-screen visuals add context beyond the transcript.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles an Anthropic API key and the artifact suggests printing the key during setup.

Mitigation: Set secrets through the shell environment or a secret manager, avoid echoing API keys, and rotate any key that may have been exposed.

Risk: Facebook, Instagram, and some YouTube runs may require browser cookies from a logged-in session.

Mitigation: Avoid personal-account cookies when possible, use a dedicated browser profile or account, keep cookie files out of version control, and delete them after use.

Risk: Video frames and transcripts are sent to an external AI service for analysis.

Mitigation: Analyze only videos the user is allowed to process and send externally, and avoid sensitive or private video content unless policy permits it.

Risk: The generated Markdown is model output from arbitrary video content and may contain inaccurate or misleading statements.

Mitigation: Review generated notes before relying on them, especially for technical, financial, legal, or operational decisions.

Risk: Setup installs Python dependencies and uses command-line download tools.

Mitigation: Review the package list before installation, use a virtual environment, and pin dependencies for repeatable deployments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gmdeep/skills/video-to-markdown)
- [Publisher profile](https://clawhub.ai/user/gmdeep)
- [Server-resolved GitHub repository](https://github.com/GMDEEP/video-to-markdown)
- [Platform notes](references/platforms.md)
- [yt-dlp supported sites](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown file with YAML frontmatter, plus setup and execution commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The generated Markdown includes overview, visual summary, section breakdown, key visuals, takeaways, terms, and visual-narration gaps.]

## Skill Version(s):

0.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
