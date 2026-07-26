## Description: <br>
SeaPortal helps an agent read and navigate static or server-rendered websites without a browser by fetching clean Markdown, JSON accessibility snapshots, links, sitemaps, feeds, and site scrape summaries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pinchtab](https://clawhub.ai/user/pinchtab) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, engineers, and agent operators use SeaPortal when an agent needs fast, read-only retrieval of public web pages, accessibility snapshots, sitemaps, feeds, or sampled site content without launching a browser. It is best suited for static or server-rendered pages and should hand off JavaScript-heavy, blocked, authenticated, or interactive flows to a browser-capable tool. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Use of internal URL access, proxies, scraping options, or MCP registration can broaden what the agent can retrieve or expose sensitive proxy credentials. <br>
Mitigation: Keep the default public, read-only posture for normal use; enable --allow-internal or proxies only for trusted targets, and avoid real proxy credentials or sensitive intranet URLs unless the operator intentionally accepts that exposure. <br>
Risk: Static HTTP retrieval can miss or under-represent JavaScript-rendered, blocked, authenticated, or interactive pages. <br>
Mitigation: Use SeaPortal for static or server-rendered pages, and hand off pages marked as SPA, dynamic, blocked, browser-needed, or validation-failed to a browser-capable tool. <br>


## Reference(s): <br>
- [SeaPortal ClawHub skill page](https://clawhub.ai/pinchtab/skills/seaportal) <br>
- [SeaPortal homepage](https://github.com/pinchtab/seaportal) <br>
- [PinchTab publisher profile](https://clawhub.ai/user/pinchtab) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown, JSON, XML, compact text snapshots, TSV manifests, shell commands, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can cap output by token or byte limits, optionally include links, images, tables, comments, chunks, ranked sections, schema extraction, or split files when requested.] <br>

## Skill Version(s): <br>
0.2.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
