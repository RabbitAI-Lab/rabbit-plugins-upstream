## Description: <br>
Turns item photos into a live eBay listing by helping an agent identify the item, research sold prices, assess condition, assemble listing fields, and drive a signed-in Chrome session to publish or save a draft. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nelsonscott](https://clawhub.ai/user/nelsonscott) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External sellers and agent operators use this skill to convert item photos and seller intent into eBay listing data, then publish the listing or save it as a draft through a browser session they already control. <br>

### Deployment Geography for Use: <br>
United States (eBay.com only) <br>

## Known Risks and Mitigations: <br>
Risk: The skill can control a signed-in Chrome session and create real eBay drafts or live listings. <br>
Mitigation: Use dry-run or draft mode first, review title, price, category, shipping, photos, and condition before publishing, and use a dedicated browser profile. <br>
Risk: An optional notification command can execute a configured shell command after publish, draft, or block events. <br>
Mitigation: Leave notifyCommand unset unless the exact command is trusted and intentionally configured. <br>
Risk: Incorrect item identification, pricing, condition, or required eBay fields can create misleading listings or block publishing. <br>
Mitigation: Base pricing on sold comps, verify uncertain item details with the seller, and let unresolved required fields save as a draft for manual review. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/nelsonscott/skills/ebay-lister) <br>
- [Publisher profile](https://clawhub.ai/user/nelsonscott) <br>
- [Source homepage](https://github.com/NelsonScott/ebay-lister) <br>
- [OpenClaw](https://openclaw.ai) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, JSON, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with JSON payloads, shell commands, and listing status URLs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce live listing URLs, draft URLs, missing-field reports, and concrete review warnings for the seller.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
