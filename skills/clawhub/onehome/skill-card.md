## Description: <br>
Search OneHome (CoreLogic) portal listings and retrieve property details, photos, schools, saved searches, and listing comparisons for properties shared through OneHome links or identifiers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to search OneHome real-estate portal listings shared by an agent, inspect listing details, retrieve related property information, compare listings, and estimate mortgage or affordability values. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may require OneHome portal credentials, magic links, or captured bearer tokens to access private listing data. <br>
Mitigation: Treat ONEHOME_TOKEN, ONEHOME_MAGIC_LINK, and any captured portal bearer token as account secrets; avoid sharing them in logs or responses and rotate or refresh them if exposed. <br>
Risk: OneHome JWTs can expire, causing listing retrieval workflows to fail or return stale authentication errors. <br>
Mitigation: Run the health check before portal operations and refresh the token or magic link when expiry is near or authentication fails. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/onehome) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/chrischall) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, configuration, text, API calls] <br>
**Output Format:** [Markdown or plain text guidance with tool-call parameters and configuration notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include listing identifiers, group identifiers, search filters, property comparisons, and local mortgage or affordability calculations.] <br>

## Skill Version(s): <br>
0.13.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
