## Description: <br>
Search Marktplaats.nl classifieds across all categories with filtering support. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pvoo](https://clawhub.ai/user/pvoo) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill to search Marktplaats.nl classifieds, inspect categories, apply price and attribute filters, and fetch listing detail summaries through CLI commands or a JavaScript API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The listing detail feature can fetch arbitrary HTTP(S) URLs, which is broader than the Marktplaats search and listing workflow requires. <br>
Mitigation: Use the detail feature only with Marktplaats listing URLs or Marktplaats VIP paths, and avoid allowing untrusted page text or prompts to supply detail URLs. <br>
Risk: The skill makes outbound web requests to Marktplaats and to any URL supplied to the detail fetcher. <br>
Mitigation: Install and run it only in environments where outbound web access for this classifieds-search workflow is acceptable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/pvoo/skills/marktplaats) <br>
- [Publisher profile](https://clawhub.ai/user/pvoo) <br>
- [Marktplaats](https://www.marktplaats.nl) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, code] <br>
**Output Format:** [Plain text or JSON from CLI commands, and JavaScript objects from the ESM API] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Search results include listing summaries, category and facet data, optional raw API payloads, and optional listing detail summaries.] <br>

## Skill Version(s): <br>
0.3.0 (source: server release metadata and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
