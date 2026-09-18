## Description:

Render Url renders one URL in headless Chromium and extracts deterministic structured JSON from the post-JavaScript DOM.

This skill is ready for commercial/non-commercial use.

## Publisher:

[umerkha2007](https://clawhub.ai/user/umerkha2007)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use Render Url to capture post-JavaScript web page content and convert it into structured JSON for inspection, analysis, or downstream extraction workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill opens user-provided URLs in Chromium and saves rendered HTML or parsed page data locally.

Mitigation: Avoid internal, authenticated, or token-bearing URLs unless intended, and clean up generated JSON files after use.

Risk: Dependency versions are range-based, which can affect reproducible installs.

Mitigation: Pin package versions when reproducible installation behavior matters.

## Reference(s):

- [Source repository](https://github.com/umerkha2007/PlaywrightURLScraper)
- [ClawHub skill page](https://clawhub.ai/umerkha2007/skills/playwrighturlscraper)

## Skill Output:

**Output Type(s):** [JSON, Files, Shell commands]

**Output Format:** [JSON objects printed to stdout and written to auto-incremented files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One URL per invocation; diagnostics are written to stderr.]

## Skill Version(s):

0.1.0 (source: server release metadata; artifact pyproject.toml reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
