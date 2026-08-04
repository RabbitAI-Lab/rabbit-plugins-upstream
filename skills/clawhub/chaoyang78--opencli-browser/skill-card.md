## Description: <br>
Guides agents in driving a real Chrome window through opencli to inspect pages, fill forms, navigate logged-in flows, extract data, handle selector and stale-reference issues, and review network captures. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chaoyang78](https://clawhub.ai/user/chaoyang78) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill when an agent needs scoped, multi-step control of a live Chrome session for page inspection, form interaction, logged-in workflows, ad-hoc extraction, or network-backed data retrieval. It is intended for browser automation gaps and debugging, not for authoring reusable site adapters. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill enables high-impact browser and session control, including bound tabs and logged-in pages. <br>
Mitigation: Review before installing and use it only for browser sessions and sites the agent is intended to control. <br>
Risk: Network capture and cached network details may expose sensitive data from logged-in pages. <br>
Mitigation: Avoid broad or raw network capture on sensitive pages and clear cached network data when needed. <br>
Risk: Upload guidance and local Read/Edit/Write authority can expose or change local files. <br>
Mitigation: Confirm any local file upload path and destination site, and account for local file authority during review. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chaoyang78/skills/opencli-browser) <br>
- [OpenCLI Chrome Web Store extension](https://chromewebstore.google.com/detail/opencli/ildkmabpimmkaediidaifkhjpohdnifk) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with inline shell command examples and JSON envelope examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guidance emphasizes named browser sessions, structured command envelopes, selector or numeric-ref targeting, verification after writes, and bounded network or cache inspection.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
