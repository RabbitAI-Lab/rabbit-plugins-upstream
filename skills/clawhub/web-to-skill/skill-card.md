## Description: <br>
Converts one public website URL or an explicit batch of public URLs into a reusable skill ZIP backed by rendered HTML snapshots and a bounded JSONL retrieval index. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jarvisyaoht](https://clawhub.ai/user/jarvisyaoht) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and documentation teams use WebToSkill to turn public documentation sites, help centers, and explicit URL batches into reusable agent skills with searchable local snapshots. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill renders untrusted public web pages with Chromium sandboxing disabled by default. <br>
Mitigation: Review before installing in non-containerized or sensitive environments, and prefer Chromium sandboxing where supported by setting PLAYWRIGHT_NO_SANDBOX=0. <br>
Risk: The generated ZIP can contain copied page snapshots from crawled websites. <br>
Mitigation: Use only public URLs that the user is allowed to crawl and package, and review target site terms, robots policies, and content permissions before distribution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jarvisyaoht/skills/web-to-skill) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration] <br>
**Output Format:** [ZIP archive containing Markdown, YAML configuration, JSONL index data, rendered HTML snapshots, and Python retrieval helpers; final agent response is the ZIP path.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Public URLs only; bounded crawl validation, metadata outlining, and deterministic packaging.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
