## Description: <br>
Save a live webpage as a high-fidelity PDF that preserves layout and lazy-loaded images using the agent-browser CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tenequm](https://clawhub.ai/user/tenequm) <br>

### License/Terms of Use: <br>
Apache 2.0 <br>


## Use Case: <br>
Developers and agents use this skill to capture browser-faithful PDF archives of webpages, especially JavaScript-heavy pages where lazy-loaded images must be forced to load before printing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill opens requested URLs in a browser automation CLI and saves rendered page contents to local PDF files, which can capture private or authenticated content. <br>
Mitigation: Use it only for pages the user is comfortable archiving locally, and avoid private or authenticated pages unless capture is explicitly intended. <br>
Risk: The recipe runs page-local JavaScript and browser automation steps to load images and remove common consent overlays. <br>
Mitigation: Review the target page and generated PDF before relying on or sharing the capture, especially for pages with dynamic or sensitive content. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/tenequm/skills/download-webpage-as-pdf) <br>
- [Skill homepage](https://github.com/tenequm/skills/tree/main/skills/download-webpage-as-pdf) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with bash command blocks and operational guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local PDF files through browser automation; optional cleanup guidance may use qpdf and Ghostscript.] <br>

## Skill Version(s): <br>
0.1.5 (source: frontmatter metadata.version, release metadata, changelog released 2026-07-22) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
