## Description:

Saves live webpages as high-fidelity PDFs that preserve browser layout and lazy-loaded images using the agent-browser CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers and agents use this skill to capture user-selected webpages as browser-like PDFs, especially JavaScript-heavy pages with lazy-loaded images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Opening user-provided URLs in a browser can expose the agent workflow to untrusted web content.

Mitigation: Use the skill only for user-approved URLs and keep captures isolated to the browser session used for the task.

Risk: Multiple agents sharing the same agent-browser session can interfere with each other's captures.

Mitigation: Use a unique agent-browser session for each concurrent run.

Risk: Cookie-banner removal, footer trimming, or cleanup steps can change the final PDF.

Mitigation: Review the generated PDF and report verification details such as broken-image count, page count, and file size before relying on it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tenequm/skills/download-webpage-as-pdf)
- [Skill homepage](https://github.com/tenequm/skills/tree/main/skills/download-webpage-as-pdf)

## Skill Output:

**Output Type(s):** [Files, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with bash command blocks and local PDF output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a local PDF and verification details such as broken-image count, page count, and file size.]

## Skill Version(s):

0.1.6 (source: frontmatter metadata and changelog, released 2026-08-07)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
