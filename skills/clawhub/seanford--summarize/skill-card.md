## Description: <br>
Summarize URLs or files with the summarize CLI (web, PDFs, images, audio, YouTube). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[seanford](https://clawhub.ai/user/seanford) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and agent users use this skill to summarize web pages, PDFs, images, audio, YouTube links, and local files through the external summarize CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Summarized content may be sent to configured AI, extraction, Firecrawl, or Apify providers and should be treated as non-private processing. <br>
Mitigation: Avoid summarizing sensitive local files, private URLs, or confidential media unless provider data handling and retention have been reviewed. <br>
Risk: The skill depends on an external summarize CLI and configured provider credentials. <br>
Mitigation: Install the CLI from the documented source, configure only intended provider keys, and review command options before use. <br>


## Reference(s): <br>
- [Summarize homepage](https://summarize.sh) <br>
- [ClawHub skill listing](https://clawhub.ai/seanford/skills/summarize) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, text, json] <br>
**Output Format:** [Markdown guidance with bash examples; the summarize CLI can return text or machine-readable JSON summaries.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports length, max token, extract-only, model selection, Firecrawl fallback, and YouTube fallback options.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and artifact _meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
