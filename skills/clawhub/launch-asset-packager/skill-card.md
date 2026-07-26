## Description: <br>
Builds a tier-scoped launch asset manifest with press kit specs, demo and screenshot specs, launch FAQ outline, App Store and Play listing metadata drafts with character counts, and a technical go-live checklist manifest. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aaron-he-zhu](https://clawhub.ai/user/aaron-he-zhu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Launch, marketing, and product teams use this skill to assemble a launch-ready asset package for a declared launch tier. It tracks asset owners, production status, official store listing limits, go-live checklist items, and handoff gaps without writing the underlying marketing copy or executing technical launch changes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may read launch memory, store exports, analytics context, and user-provided drafts that contain sensitive or untrusted launch information. <br>
Mitigation: Use it only for intended launch packaging work, treat pasted exports and drafts as untrusted input, and review generated manifests before sharing or saving them. <br>
Risk: Incorrect claims, launch dates, or registry proposals could make the launch package misleading or premature. <br>
Mitigation: Review any proposed save or registry event before approval, especially entries involving product claims, dates, pricing, or publish-ready status. <br>
Risk: Store listing character limits and platform policies can change before submission. <br>
Mitigation: Verify App Store Connect and Play Console requirements at submission time and keep unresolved or unsupported claims out of launch-ready assets. <br>


## Reference(s): <br>
- [Launch Asset Specs](references/asset-specs.md) <br>
- [Project homepage](https://github.com/aaron-he-zhu/aaron-marketing-skills) <br>
- [ClawHub skill page](https://clawhub.ai/aaron-he-zhu/skills/launch-asset-packager) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown with tables, checklists, character counts, and handoff summary fields] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose saved manifests or registry events only with user permission; does not execute store submission or go-live changes.] <br>

## Skill Version(s): <br>
19.0.0 (source: server release evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
