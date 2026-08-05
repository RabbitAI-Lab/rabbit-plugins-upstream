## Description: <br>
Multi-stage deep intelligence pipeline (Search -> Filter -> Fetch -> Synthesize). Turns a query into a structured research report with full source citations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jonathanjing](https://clawhub.ai/user/jonathanjing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and external users use Deep Scout to turn a research question into a filtered, fetched, and synthesized Markdown report with citations. It is intended for web intelligence workflows where source collection, relevance filtering, and report synthesis need to be coordinated by an agent. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Research queries, target URLs, and fetched page text may be sent through search/fetch providers, optional Firecrawl/browser tooling, and LLM synthesis. <br>
Mitigation: Use the skill only for topics approved for those providers, avoid secrets and regulated data, and disable Firecrawl or browser fallback when those channels are not acceptable. <br>
Risk: Reports and resumable state may retain sensitive research content locally. <br>
Mitigation: Choose a safe output path and clean up ~/.openclaw/state/deep-scout when reports or state may contain sensitive information. <br>
Risk: Web-derived reports can be incomplete, stale, or affected by source quality. <br>
Mitigation: Review cited sources, check the Conflicts & Gaps section, and verify high-impact claims before using the report for decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jonathanjing/skills/deep-scout) <br>
- [ClawHub metadata homepage](https://clawhub.ai/jonathanjing/deep-scout) <br>
- [Example research report](artifact/examples/openclaw-acquisition.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown research reports or comparisons, with JSON action blocks during orchestration] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports include source citations, can be written to an output file, and default to stdout.] <br>

## Skill Version(s): <br>
0.1.5 (source: server release, OpenClaw metadata, and clawhub.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
